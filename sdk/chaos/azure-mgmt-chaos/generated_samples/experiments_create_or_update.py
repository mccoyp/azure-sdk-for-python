# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.chaos import ChaosManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-chaos
# USAGE
    python experiments_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ChaosManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="6b052e15-03d3-4f17-b2e1-be7f07588291",
    )

    response = client.experiments.begin_create_or_update(
        resource_group_name="exampleRG",
        experiment_name="exampleExperiment",
        resource={
            "identity": {"type": "SystemAssigned"},
            "location": "eastus2euap",
            "properties": {
                "selectors": [
                    {
                        "id": "selector1",
                        "targets": [
                            {
                                "id": "/subscriptions/6b052e15-03d3-4f17-b2e1-be7f07588291/resourceGroups/exampleRG/providers/Microsoft.Compute/virtualMachines/exampleVM/providers/Microsoft.Chaos/targets/Microsoft-VirtualMachine",
                                "type": "ChaosTarget",
                            }
                        ],
                        "type": "List",
                    }
                ],
                "steps": [
                    {
                        "branches": [
                            {
                                "actions": [
                                    {
                                        "duration": "PT10M",
                                        "name": "urn:csci:microsoft:virtualMachine:shutdown/1.0",
                                        "parameters": [{"key": "abruptShutdown", "value": "false"}],
                                        "selectorId": "selector1",
                                        "type": "continuous",
                                    }
                                ],
                                "name": "branch1",
                            }
                        ],
                        "name": "step1",
                    }
                ],
            },
            "tags": {"key2138": "fjaeecgnvqd", "key7131": "ryohwcoiccwsnewjigfmijz"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/chaos/resource-manager/Microsoft.Chaos/stable/2025-01-01/examples/Experiments_CreateOrUpdate.json
if __name__ == "__main__":
    main()
