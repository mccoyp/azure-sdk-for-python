# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import Optional, Any, cast

from azure.core.exceptions import ClientAuthenticationError
from azure.core.credentials import AccessToken, AccessTokenInfo, TokenRequestOptions
from .._internal import AadClient, AsyncContextManager
from .._internal.get_token_mixin import GetTokenMixin


class AuthorizationCodeCredential(AsyncContextManager, GetTokenMixin):
    """Authenticates by redeeming an authorization code previously obtained from Microsoft Entra ID.

    See `Microsoft Entra ID documentation
    <https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow>`__ for more information
    about the authentication flow.

    :param str tenant_id: ID of the application's Microsoft Entra tenant. Also called its "directory" ID.
    :param str client_id: The application's client ID
    :param str authorization_code: The authorization code from the user's log-in
    :param str redirect_uri: The application's redirect URI. Must match the URI used to request the authorization code.

    :keyword str authority: Authority of a Microsoft Entra endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str client_secret: One of the application's client secrets. Required only for web apps and web APIs.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_authorization_code_credential_async]
            :end-before: [END create_authorization_code_credential_async]
            :language: python
            :dedent: 4
            :caption: Create an AuthorizationCodeCredential.
    """

    async def __aenter__(self) -> "AuthorizationCodeCredential":
        if self._client:
            await self._client.__aenter__()
        return self

    async def close(self) -> None:
        """Close the credential's transport session."""

        if self._client:
            await self._client.__aexit__()

    def __init__(
        self,
        tenant_id: str,
        client_id: str,
        authorization_code: str,
        redirect_uri: str,
        *,
        client_secret: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        self._authorization_code: Optional[str] = authorization_code
        self._client_id = client_id
        self._client_secret = client_secret
        self._client = kwargs.pop("client", None) or AadClient(tenant_id, client_id, **kwargs)
        self._redirect_uri = redirect_uri
        super().__init__()

    async def get_token(
        self, *scopes: str, claims: Optional[str] = None, tenant_id: Optional[str] = None, **kwargs: Any
    ) -> AccessToken:
        """Request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        The first time this method is called, the credential will redeem its authorization code. On subsequent calls
        the credential will return a cached access token or redeem a refresh token, if it acquired a refresh token upon
        redeeming the authorization code.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/entra/identity-platform/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
          attribute gives a reason. Any error response from Microsoft Entra ID is available as the error's
          ``response`` attribute.
        """
        return await super(AuthorizationCodeCredential, self).get_token(
            *scopes, claims=claims, tenant_id=tenant_id, client_secret=self._client_secret, **kwargs
        )

    async def get_token_info(self, *scopes: str, options: Optional[TokenRequestOptions] = None) -> AccessTokenInfo:
        """Request an access token for `scopes`.

        This is an alternative to `get_token` to enable certain scenarios that require additional properties
        on the token. This method is called automatically by Azure SDK clients.

        The first time this method is called, the credential will redeem its authorization code. On subsequent calls
        the credential will return a cached access token or redeem a refresh token, if it acquired a refresh token upon
        redeeming the authorization code.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see https://learn.microsoft.com/entra/identity-platform/scopes-oidc.
        :keyword options: A dictionary of options for the token request. Unknown options will be ignored. Optional.
        :paramtype options: ~azure.core.credentials.TokenRequestOptions

        :rtype: ~azure.core.credentials.AccessTokenInfo
        :return: An AccessTokenInfo instance containing information about the token.
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
          attribute gives a reason. Any error response from Microsoft Entra ID is available as the error's
          ``response`` attribute.
        """
        return await super()._get_token_base(
            *scopes, options=options, client_secret=self._client_secret, base_method_name="get_token_info"
        )

    async def _acquire_token_silently(self, *scopes: str, **kwargs: Any) -> Optional[AccessTokenInfo]:
        return self._client.get_cached_access_token(scopes, **kwargs)

    async def _request_token(self, *scopes: str, **kwargs: Any) -> AccessTokenInfo:
        if self._authorization_code:
            token = await self._client.obtain_token_by_authorization_code(
                scopes=scopes, code=self._authorization_code, redirect_uri=self._redirect_uri, **kwargs
            )
            self._authorization_code = None  # auth codes are single-use
            return token

        token = cast(AccessTokenInfo, None)
        for refresh_token in self._client.get_cached_refresh_tokens(scopes, **kwargs):
            if "secret" in refresh_token:
                token = await self._client.obtain_token_by_refresh_token(scopes, refresh_token["secret"], **kwargs)
                if token:
                    break

        if not token:
            raise ClientAuthenticationError(
                message="No authorization code, cached access token, or refresh token available."
            )

        return token
