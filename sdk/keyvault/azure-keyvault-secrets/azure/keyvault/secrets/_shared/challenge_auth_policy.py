# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Policy implementing Key Vault's challenge authentication protocol.

Normally the protocol is only used for the client's first service request, upon which:
1. The challenge authentication policy sends a copy of the request, without authorization or content.
2. Key Vault responds 401 with a header (the 'challenge') detailing how the client should authenticate such a request.
3. The policy authenticates according to the challenge and sends the original request with authorization.

The policy caches the challenge and thus knows how to authenticate future requests. However, authentication
requirements can change. For example, a vault may move to a new tenant. In such a case the policy will attempt the
protocol again.
"""

import time

from azure.core.exceptions import ServiceRequestError
from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import BearerTokenChallengePolicy

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    from azure.core.pipeline import PipelineRequest, PipelineResponse


def _enforce_tls(request):
    # type: (PipelineRequest) -> None
    if not request.http_request.url.lower().startswith("https"):
        raise ServiceRequestError(
            "Bearer token authentication is not permitted for non-TLS protected (non-https) URLs."
        )


class ChallengeAuthPolicy(BearerTokenChallengePolicy):
    """policy for handling HTTP authentication challenges"""

    def on_request(self, request):
        # type: (PipelineRequest) -> None
        """Called before the policy sends a request.

        :param ~azure.core.pipeline.PipelineRequest request: the request
        """
        _enforce_tls(request)
        challenge = self.challenge_cache.get_challenge_for_url(request.http_request.url)
        if challenge:
            # Note that if the vault has moved to a new tenant since our last request for it, this request will fail.
            if self._need_new_token:
                # azure-identity credentials require an AADv2 scope but the challenge may specify an AADv1 resource
                scope = challenge.scope or challenge.resource + "/.default"
                self._token = self._credential.get_token(scope, tenant_id=challenge.tenant_id)

            # ignore mypy's warning -- although self._token is Optional, get_token raises when it fails to get a token
            request.http_request.headers["Authorization"] = "Bearer {}".format(self._token.token)  # type: ignore
            return

        # else: discover authentication information by eliciting a challenge from Key Vault. Remove any request data,
        # saving it for later. Key Vault will reject the request as unauthorized and respond with a challenge.
        # on_challenge will parse that challenge, reattach any body removed here, authorize the request, and tell
        # super to send it again.
        if request.http_request.body:
            request.context["key_vault_request_data"] = request.http_request.body
            request.http_request.set_json_body(None)
            request.http_request.headers["Content-Length"] = "0"

    def on_challenge(self, request: "PipelineRequest", response: "PipelineResponse") -> bool:
        """Authorize request according to an authentication challenge

        This method is called when the resource provider responds 401 with a WWW-Authenticate header.

        :param ~azure.core.pipeline.PipelineRequest request: the request which elicited an authentication challenge
        :param ~azure.core.pipeline.PipelineResponse response: the resource provider's response
        :returns: a bool indicating whether the policy should send the request
        """
        # super attempts to fetch a token and add it to the request's Authorization header
        result = super().on_challenge(request, response)
        if result:
            body = request.context.pop("key_vault_request_data", None)
            request.http_request.set_text_body(body)  # no-op when text is None
        return result

    @property
    def _need_new_token(self):
        # type: () -> bool
        return not self._token or self._token.expires_on - time.time() < 300
