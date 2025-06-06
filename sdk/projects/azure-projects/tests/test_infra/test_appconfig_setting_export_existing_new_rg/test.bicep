param location string
param environmentName string
param defaultNamePrefix string
param defaultName string
param principalId string
param tenantId string
param azdTags object

resource configurationstore 'Microsoft.AppConfiguration/configurationStores@2024-05-01' = {
  name: defaultName
  sku: {
    name: 'Standard'
  }
  properties: {
    disableLocalAuth: true
    createMode: 'Default'
    dataPlaneProxy: {
      authenticationMode: 'Pass-through'
      privateLinkDelegation: 'Disabled'
    }
    publicNetworkAccess: 'Enabled'
  }
  location: location
  tags: azdTags
}

output AZURE_APPCONFIG_ID string = configurationstore.id
output AZURE_APPCONFIG_NAME string = configurationstore.name
output AZURE_APPCONFIG_RESOURCE_GROUP string = resourceGroup().name
output AZURE_APPCONFIG_ENDPOINT string = configurationstore.properties.endpoint


resource resourcegroup_rgtest 'Microsoft.Resources/resourceGroups@2021-04-01' existing = {
  name: 'rgtest'
  scope: subscription()
}

resource configurationstore_configtest 'Microsoft.AppConfiguration/configurationStores@2024-05-01' existing = {
  name: 'configtest'
  scope: resourcegroup_rgtest
}

output AZURE_APPCONFIG_ID_R string = configurationstore_configtest.id
output AZURE_APPCONFIG_NAME_R string = configurationstore_configtest.name
output AZURE_APPCONFIG_RESOURCE_GROUP_R string = 'rgtest'
output AZURE_APPCONFIG_ENDPOINT_R string = configurationstore_configtest.properties.endpoint


resource keyvalue_configtest_test 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' existing = {
  name: 'test'
  parent: configurationstore_configtest
}



resource keyvalue_azureappconfigid 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_ID'
  properties: {
    value: configurationstore.id
  }
}



resource keyvalue_azureappconfigname 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_NAME'
  properties: {
    value: configurationstore.name
  }
}



resource keyvalue_azureappconfigresourcegroup 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_RESOURCE_GROUP'
  properties: {
    value: resourceGroup().name
  }
}



resource keyvalue_azureappconfigendpoint 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_ENDPOINT'
  properties: {
    value: configurationstore.properties.endpoint
  }
}



resource keyvalue_azureappconfigidr 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_ID_R'
  properties: {
    value: configurationstore_configtest.id
  }
}



resource keyvalue_azureappconfignamer 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_NAME_R'
  properties: {
    value: configurationstore_configtest.name
  }
}



resource keyvalue_azureappconfigresourcegroupr 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_RESOURCE_GROUP_R'
  properties: {
    value: 'rgtest'
  }
}



resource keyvalue_azureappconfigendpointr 'Microsoft.AppConfiguration/configurationStores/keyValues@2024-05-01' = {
  parent: configurationstore_configtest
  name: 'AZURE_APPCONFIG_ENDPOINT_R'
  properties: {
    value: configurationstore_configtest.properties.endpoint
  }
}



resource roleassignment_unxsuzdqhucrcsmcfuyc 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid('MicrosoftAppConfigurationconfigurationStores', environmentName, defaultName, 'User', 'App Configuration Data Owner')
  properties: {
    principalId: principalId
    principalType: 'User'
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      '5ae67dd6-50cb-40e7-96ff-dc2bfa4b606b'
    )

  }
  scope: configurationstore
}



resource roleassignment_cmjdzwakpcfdaqqbaykp 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid('MicrosoftResourcesresourceGroups', environmentName, 'configtest', 'User', 'App Configuration Data Owner')
  properties: {
    principalId: principalId
    principalType: 'User'
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      '5ae67dd6-50cb-40e7-96ff-dc2bfa4b606b'
    )

  }
  scope: resourceGroup()
}



