# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.apimanagement.aio import ApiManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApiManagementNotificationRecipientUserOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ApiManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notification_recipient_user_list_by_notification(self, resource_group):
        response = await self.client.notification_recipient_user.list_by_notification(
            resource_group_name=resource_group.name,
            service_name="str",
            notification_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notification_recipient_user_check_entity_exists(self, resource_group):
        response = await self.client.notification_recipient_user.check_entity_exists(
            resource_group_name=resource_group.name,
            service_name="str",
            notification_name="str",
            user_id="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notification_recipient_user_create_or_update(self, resource_group):
        response = await self.client.notification_recipient_user.create_or_update(
            resource_group_name=resource_group.name,
            service_name="str",
            notification_name="str",
            user_id="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_notification_recipient_user_delete(self, resource_group):
        response = await self.client.notification_recipient_user.delete(
            resource_group_name=resource_group.name,
            service_name="str",
            notification_name="str",
            user_id="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...
