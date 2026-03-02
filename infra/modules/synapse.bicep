param location string
param synapseName string
param storageAccountName string

resource synapse 'Microsoft.Synapse/workspaces@2021-06-01' = {
  name: synapseName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    defaultDataLakeStorage: {
      accountUrl: 'https://${storageAccountName}.dfs.core.windows.net'
      filesystem: 'synapse'
    }
    sqlAdministratorLogin: 'synadminuser'
    sqlAdministratorLoginPassword: 'TempPassword123!'
  }
}
