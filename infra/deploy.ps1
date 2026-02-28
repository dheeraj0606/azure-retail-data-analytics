param (
    [string]$resourceGroupName = "rg-retail-analytics-dev",
    [string]$location = "East US"
)

Write-Host "Logging into Azure..."
Connect-AzAccount

Write-Host "Creating resource group..."
New-AzResourceGroup -Name $resourceGroupName -Location $location -ErrorAction SilentlyContinue

Write-Host "Deploying Bicep template..."
New-AzResourceGroupDeployment `
  -ResourceGroupName $resourceGroupName `
  -TemplateFile "main.bicep" `
  -TemplateParameterFile "parameters.dev.json"

Write-Host "Deployment completed."
