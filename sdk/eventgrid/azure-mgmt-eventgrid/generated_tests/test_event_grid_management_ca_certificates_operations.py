# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.eventgrid import EventGridManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEventGridManagementCaCertificatesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(EventGridManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_ca_certificates_get(self, resource_group):
        response = self.client.ca_certificates.get(
            resource_group_name=resource_group.name,
            namespace_name="str",
            ca_certificate_name="str",
            api_version="2025-04-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_ca_certificates_begin_create_or_update(self, resource_group):
        response = self.client.ca_certificates.begin_create_or_update(
            resource_group_name=resource_group.name,
            namespace_name="str",
            ca_certificate_name="str",
            ca_certificate_info={
                "description": "str",
                "encodedCertificate": "str",
                "expiryTimeInUtc": "2020-02-20 00:00:00",
                "id": "str",
                "issueTimeInUtc": "2020-02-20 00:00:00",
                "name": "str",
                "provisioningState": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2025-04-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_ca_certificates_begin_delete(self, resource_group):
        response = self.client.ca_certificates.begin_delete(
            resource_group_name=resource_group.name,
            namespace_name="str",
            ca_certificate_name="str",
            api_version="2025-04-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_ca_certificates_list_by_namespace(self, resource_group):
        response = self.client.ca_certificates.list_by_namespace(
            resource_group_name=resource_group.name,
            namespace_name="str",
            api_version="2025-04-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
