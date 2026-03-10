function Get-PublicIP {
    return (Invoke-WebRequest -Uri "https://api.ipify.org").Content
}

Write-Host "Utility functions loaded"
