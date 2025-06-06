# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute.aio import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementCloudServicesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_create_or_update(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_update(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_update(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_delete(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_delete(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_get(self, resource_group):
        response = await self.client.cloud_services.get(
            resource_group_name=resource_group.name,
            cloud_service_name="str",
            api_version="2024-11-04",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_get_instance_view(self, resource_group):
        response = await self.client.cloud_services.get_instance_view(
            resource_group_name=resource_group.name,
            cloud_service_name="str",
            api_version="2024-11-04",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_list_all(self, resource_group):
        response = self.client.cloud_services.list_all(
            api_version="2024-11-04",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_list(self, resource_group):
        response = self.client.cloud_services.list(
            resource_group_name=resource_group.name,
            api_version="2024-11-04",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_start(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_start(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_power_off(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_power_off(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_restart(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_restart(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_reimage(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_reimage(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_rebuild(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_rebuild(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_cloud_services_begin_delete_instances(self, resource_group):
        response = await (
            await self.client.cloud_services.begin_delete_instances(
                resource_group_name=resource_group.name,
                cloud_service_name="str",
                api_version="2024-11-04",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
