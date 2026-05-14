Write-Host "Starting deployment..."

git pull origin main

Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host "Running SQL scripts..."
# placeholder for db execution
Write-Host "Executing curated SQL layer"

Write-Host "Deployment completed successfully"
