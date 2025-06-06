# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, Type, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_by_id_request(
    resource_group_name: str,
    automation_account_name: str,
    software_update_configuration_run_id: str,
    subscription_id: str,
    *,
    client_request_id: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-08"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns/{softwareUpdateConfigurationRunId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._]+$"
        ),
        "automationAccountName": _SERIALIZER.url("automation_account_name", automation_account_name, "str"),
        "softwareUpdateConfigurationRunId": _SERIALIZER.url(
            "software_update_configuration_run_id", software_update_configuration_run_id, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["clientRequestId"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(
    resource_group_name: str,
    automation_account_name: str,
    subscription_id: str,
    *,
    client_request_id: Optional[str] = None,
    filter: Optional[str] = None,
    skip: Optional[str] = None,
    top: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-08"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._]+$"
        ),
        "automationAccountName": _SERIALIZER.url("automation_account_name", automation_account_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if skip is not None:
        _params["$skip"] = _SERIALIZER.query("skip", skip, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["clientRequestId"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class SoftwareUpdateConfigurationRunsOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.automation.AutomationClient`'s
        :attr:`software_update_configuration_runs` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_by_id(
        self,
        resource_group_name: str,
        automation_account_name: str,
        software_update_configuration_run_id: str,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> _models.SoftwareUpdateConfigurationRun:
        """Get a single software update configuration Run by Id.

        .. seealso::
           - http://aka.ms/azureautomationsdk/softwareupdateconfigurationrunoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param software_update_configuration_run_id: The Id of the software update configuration run.
         Required.
        :type software_update_configuration_run_id: str
        :param client_request_id: Identifies this specific client request. Default value is None.
        :type client_request_id: str
        :return: SoftwareUpdateConfigurationRun or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SoftwareUpdateConfigurationRun
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-08"))
        cls: ClsType[_models.SoftwareUpdateConfigurationRun] = kwargs.pop("cls", None)

        _request = build_get_by_id_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            software_update_configuration_run_id=software_update_configuration_run_id,
            subscription_id=self._config.subscription_id,
            client_request_id=client_request_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SoftwareUpdateConfigurationRun", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        automation_account_name: str,
        client_request_id: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
        **kwargs: Any
    ) -> _models.SoftwareUpdateConfigurationRunListResult:
        """Return list of software update configuration runs.

        .. seealso::
           - http://aka.ms/azureautomationsdk/softwareupdateconfigurationoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param client_request_id: Identifies this specific client request. Default value is None.
        :type client_request_id: str
        :param filter: The filter to apply on the operation. You can use the following filters:
         'properties/osType', 'properties/status', 'properties/startTime', and
         'properties/softwareUpdateConfiguration/name'. Default value is None.
        :type filter: str
        :param skip: Number of entries you skip before returning results. Default value is None.
        :type skip: str
        :param top: Maximum number of entries returned in the results collection. Default value is
         None.
        :type top: str
        :return: SoftwareUpdateConfigurationRunListResult or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SoftwareUpdateConfigurationRunListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-08"))
        cls: ClsType[_models.SoftwareUpdateConfigurationRunListResult] = kwargs.pop("cls", None)

        _request = build_list_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            subscription_id=self._config.subscription_id,
            client_request_id=client_request_id,
            filter=filter,
            skip=skip,
            top=top,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SoftwareUpdateConfigurationRunListResult", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
