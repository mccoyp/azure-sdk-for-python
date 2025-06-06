# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.monitor import MonitorManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMonitorManagementAutoscaleSettingsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(MonitorManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_autoscale_settings_list_by_resource_group(self, resource_group):
        response = self.client.autoscale_settings.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2022-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_autoscale_settings_create_or_update(self, resource_group):
        response = self.client.autoscale_settings.create_or_update(
            resource_group_name=resource_group.name,
            autoscale_setting_name="str",
            parameters={
                "location": "str",
                "profiles": [
                    {
                        "capacity": {"default": "str", "maximum": "str", "minimum": "str"},
                        "name": "str",
                        "rules": [
                            {
                                "metricTrigger": {
                                    "metricName": "str",
                                    "metricResourceUri": "str",
                                    "operator": "str",
                                    "statistic": "str",
                                    "threshold": 0.0,
                                    "timeAggregation": "str",
                                    "timeGrain": "1 day, 0:00:00",
                                    "timeWindow": "1 day, 0:00:00",
                                    "dimensions": [{"DimensionName": "str", "Operator": "str", "Values": ["str"]}],
                                    "dividePerInstance": bool,
                                    "metricNamespace": "str",
                                    "metricResourceLocation": "str",
                                },
                                "scaleAction": {
                                    "cooldown": "1 day, 0:00:00",
                                    "direction": "str",
                                    "type": "str",
                                    "value": "1",
                                },
                            }
                        ],
                        "fixedDate": {"end": "2020-02-20 00:00:00", "start": "2020-02-20 00:00:00", "timeZone": "str"},
                        "recurrence": {
                            "frequency": "str",
                            "schedule": {"days": ["str"], "hours": [0], "minutes": [0], "timeZone": "str"},
                        },
                    }
                ],
                "enabled": False,
                "id": "str",
                "name": "str",
                "notifications": [
                    {
                        "operation": "Scale",
                        "email": {
                            "customEmails": ["str"],
                            "sendToSubscriptionAdministrator": False,
                            "sendToSubscriptionCoAdministrators": False,
                        },
                        "webhooks": [{"properties": {"str": "str"}, "serviceUri": "str"}],
                    }
                ],
                "predictiveAutoscalePolicy": {"scaleMode": "str", "scaleLookAheadTime": "1 day, 0:00:00"},
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "targetResourceLocation": "str",
                "targetResourceUri": "str",
                "type": "str",
            },
            api_version="2022-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_autoscale_settings_delete(self, resource_group):
        response = self.client.autoscale_settings.delete(
            resource_group_name=resource_group.name,
            autoscale_setting_name="str",
            api_version="2022-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_autoscale_settings_get(self, resource_group):
        response = self.client.autoscale_settings.get(
            resource_group_name=resource_group.name,
            autoscale_setting_name="str",
            api_version="2022-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_autoscale_settings_update(self, resource_group):
        response = self.client.autoscale_settings.update(
            resource_group_name=resource_group.name,
            autoscale_setting_name="str",
            autoscale_setting_resource={
                "enabled": False,
                "name": "str",
                "notifications": [
                    {
                        "operation": "Scale",
                        "email": {
                            "customEmails": ["str"],
                            "sendToSubscriptionAdministrator": False,
                            "sendToSubscriptionCoAdministrators": False,
                        },
                        "webhooks": [{"properties": {"str": "str"}, "serviceUri": "str"}],
                    }
                ],
                "predictiveAutoscalePolicy": {"scaleMode": "str", "scaleLookAheadTime": "1 day, 0:00:00"},
                "profiles": [
                    {
                        "capacity": {"default": "str", "maximum": "str", "minimum": "str"},
                        "name": "str",
                        "rules": [
                            {
                                "metricTrigger": {
                                    "metricName": "str",
                                    "metricResourceUri": "str",
                                    "operator": "str",
                                    "statistic": "str",
                                    "threshold": 0.0,
                                    "timeAggregation": "str",
                                    "timeGrain": "1 day, 0:00:00",
                                    "timeWindow": "1 day, 0:00:00",
                                    "dimensions": [{"DimensionName": "str", "Operator": "str", "Values": ["str"]}],
                                    "dividePerInstance": bool,
                                    "metricNamespace": "str",
                                    "metricResourceLocation": "str",
                                },
                                "scaleAction": {
                                    "cooldown": "1 day, 0:00:00",
                                    "direction": "str",
                                    "type": "str",
                                    "value": "1",
                                },
                            }
                        ],
                        "fixedDate": {"end": "2020-02-20 00:00:00", "start": "2020-02-20 00:00:00", "timeZone": "str"},
                        "recurrence": {
                            "frequency": "str",
                            "schedule": {"days": ["str"], "hours": [0], "minutes": [0], "timeZone": "str"},
                        },
                    }
                ],
                "tags": {"str": "str"},
                "targetResourceLocation": "str",
                "targetResourceUri": "str",
            },
            api_version="2022-10-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_autoscale_settings_list_by_subscription(self, resource_group):
        response = self.client.autoscale_settings.list_by_subscription(
            api_version="2022-10-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
