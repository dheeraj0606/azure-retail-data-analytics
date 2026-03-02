param location string = 'East US'
param environment string = 'dev'
param sqlAdminLogin string
@secure()
param sqlAdminPassword string
param clientIp string

var sqlServerName = 'sql-retail-${environment}'
var sqlDbName = 'sqldb-retail-${environment}'
var storageAccountName = 'stretail${environment}'
var keyVaultName = 'kv-retail-${environment}'
var synapseName = 'syn-retail-${environment}'

module storage './modules/storage.bicep' = {
  name: 'storageModule'
  params: {
    location: location
    storageAccountName: storageAccountName
  }
}

module sql './modules/sql.bicep' = {
  name: 'sqlModule'
  params: {
    location: location
    sqlServerName: sqlServerName
    sqlDbName: sqlDbName
    sqlAdminLogin: sqlAdminLogin
    sqlAdminPassword: sqlAdminPassword
    clientIp: clientIp
  }
}

module keyvault './modules/keyvault.bicep' = {
  name: 'keyvaultModule'
  params: {
    location: location
    keyVaultName: keyVaultName
  }
}

module synapse './modules/synapse.bicep' = {
  name: 'synapseModule'
  params: {
    location: location
    synapseName: synapseName
    storageAccountName: storageAccountName
  }
}
