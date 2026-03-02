param (
    [string]$resourceGroupName = "rg-retail-analytics-dev",
    [string]$location = "East US"
)

Connect-AzAccount

$securePassword = Read-Host -Prompt "Enter SQL Admin Password" -AsSecureString

New-AzResourceGroup -Name $resourceGroupName -Location $location -ErrorAction SilentlyContinue

New-AzResourceGroupDeployment `
  -ResourceGroupName $resourceGroupName `
  -TemplateFile "main.bicep" `
  -sqlAdminLogin "retailadmin" `
  -sqlAdminPassword $securePassword `
  -clientIp (Invoke-WebRequest -Uri "https://api.ipify.org").Content
