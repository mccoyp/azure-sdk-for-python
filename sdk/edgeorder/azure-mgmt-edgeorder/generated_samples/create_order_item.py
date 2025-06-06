# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.edgeorder import EdgeOrderManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-edgeorder
# USAGE
    python create_order_item.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = EdgeOrderManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="YourSubscriptionId",
    )

    response = client.begin_create_order_item(
        order_item_name="TestOrderItemName2",
        resource_group_name="YourResourceGroupName",
        order_item_resource={
            "location": "eastus",
            "properties": {
                "addressDetails": {
                    "forwardAddress": {
                        "contactDetails": {
                            "contactName": "XXXX XXXX",
                            "emailList": ["xxxx@xxxx.xxx"],
                            "phone": "0000000000",
                            "phoneExtension": "",
                        },
                        "shippingAddress": {
                            "addressType": "None",
                            "city": "San Francisco",
                            "companyName": "Microsoft",
                            "country": "US",
                            "postalCode": "94107",
                            "stateOrProvince": "CA",
                            "streetAddress1": "16 TOWNSEND ST",
                            "streetAddress2": "UNIT 1",
                        },
                    }
                },
                "orderId": "/subscriptions/YourSubscriptionId/resourceGroups/YourResourceGroupName/providers/Microsoft.EdgeOrder/locations/eastus/orders/TestOrderName2",
                "orderItemDetails": {
                    "orderItemType": "Purchase",
                    "preferences": {"transportPreferences": {"preferredShipmentType": "MicrosoftManaged"}},
                    "productDetails": {
                        "hierarchyInformation": {
                            "configurationName": "edgep_base",
                            "productFamilyName": "azurestackedge",
                            "productLineName": "azurestackedge",
                            "productName": "azurestackedgegpu",
                        }
                    },
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/edgeorder/resource-manager/Microsoft.EdgeOrder/stable/2021-12-01/examples/CreateOrderItem.json
if __name__ == "__main__":
    main()
