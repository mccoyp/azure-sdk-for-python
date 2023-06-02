# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureResourceBase
from ._models_py3 import DenySettings
from ._models_py3 import DeploymentStack
from ._models_py3 import DeploymentStackListResult
from ._models_py3 import DeploymentStackProperties
from ._models_py3 import DeploymentStackPropertiesActionOnUnmanage
from ._models_py3 import DeploymentStackTemplateDefinition
from ._models_py3 import DeploymentStacksDebugSetting
from ._models_py3 import DeploymentStacksError
from ._models_py3 import DeploymentStacksParametersLink
from ._models_py3 import DeploymentStacksTemplateLink
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ManagedResourceReference
from ._models_py3 import ResourceReference
from ._models_py3 import ResourceReferenceExtended
from ._models_py3 import SystemData

from ._deployment_stacks_client_enums import CreatedByType
from ._deployment_stacks_client_enums import DenySettingsMode
from ._deployment_stacks_client_enums import DenyStatusMode
from ._deployment_stacks_client_enums import DeploymentStackProvisioningState
from ._deployment_stacks_client_enums import DeploymentStacksDeleteDetachEnum
from ._deployment_stacks_client_enums import ResourceStatusMode
from ._deployment_stacks_client_enums import UnmanageActionManagementGroupMode
from ._deployment_stacks_client_enums import UnmanageActionResourceGroupMode
from ._deployment_stacks_client_enums import UnmanageActionResourceMode
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureResourceBase",
    "DenySettings",
    "DeploymentStack",
    "DeploymentStackListResult",
    "DeploymentStackProperties",
    "DeploymentStackPropertiesActionOnUnmanage",
    "DeploymentStackTemplateDefinition",
    "DeploymentStacksDebugSetting",
    "DeploymentStacksError",
    "DeploymentStacksParametersLink",
    "DeploymentStacksTemplateLink",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ManagedResourceReference",
    "ResourceReference",
    "ResourceReferenceExtended",
    "SystemData",
    "CreatedByType",
    "DenySettingsMode",
    "DenyStatusMode",
    "DeploymentStackProvisioningState",
    "DeploymentStacksDeleteDetachEnum",
    "ResourceStatusMode",
    "UnmanageActionManagementGroupMode",
    "UnmanageActionResourceGroupMode",
    "UnmanageActionResourceMode",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()