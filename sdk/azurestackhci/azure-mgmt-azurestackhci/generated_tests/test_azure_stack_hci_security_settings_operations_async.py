# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.azurestackhci.aio import AzureStackHCIClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAzureStackHCISecuritySettingsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AzureStackHCIClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_clusters(self, resource_group):
        response = self.client.security_settings.list_by_clusters(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-04-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.security_settings.get(
            resource_group_name=resource_group.name,
            cluster_name="str",
            security_settings_name="default",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.security_settings.begin_create_or_update(
                resource_group_name=resource_group.name,
                cluster_name="str",
                resource={
                    "id": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "securedCoreComplianceAssignment": "str",
                    "securityComplianceStatus": {
                        "dataAtRestEncrypted": "str",
                        "dataInTransitProtected": "str",
                        "lastUpdated": "2020-02-20 00:00:00",
                        "securedCoreCompliance": "str",
                        "wdacCompliance": "str",
                    },
                    "smbEncryptionForIntraClusterTrafficComplianceAssignment": "str",
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "type": "str",
                    "wdacComplianceAssignment": "str",
                },
                security_settings_name="default",
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.security_settings.begin_delete(
                resource_group_name=resource_group.name,
                cluster_name="str",
                security_settings_name="default",
                api_version="2024-04-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
