$gitCmd = "git"
if (Get-Command git -ErrorAction SilentlyContinue) {
    Write-Host "Git found in global PATH."
}
elseif (Test-Path "C:\Program Files\Git\cmd\git.exe") {
    $gitCmd = "& 'C:\Program Files\Git\cmd\git.exe'"
    Write-Host "Git found at standard path."
}
else {
    Write-Host "Error: Git not found. Please install Git and restart your terminal." -ForegroundColor Red
    exit 1
}

Write-Host "Configuring Git Identity..."
# Set local config so it doesn't affect global settings, but allows commit to proceed
Invoke-Expression "$gitCmd config user.email 'automation@local.test'"
Invoke-Expression "$gitCmd config user.name 'Automation Bot'"

Write-Host "Initializing Git Repository..."
Invoke-Expression "$gitCmd init"

Write-Host "Adding files..."
Invoke-Expression "$gitCmd add ."

Write-Host "Committing..."
Invoke-Expression "$gitCmd commit -m 'Initial commit: B.L.A.S.T. Local Test Case Generator'"

Write-Host "Renaming branch to main..."
Invoke-Expression "$gitCmd branch -M main"

Write-Host "Adding remote origin..."
# Try to catch error if origin doesn't exist, suppressing stderr manually if needed, 
# but simply running it and ignoring the "error" state is easiest in PS for this simple script
Invoke-Expression "$gitCmd remote remove origin" 
Invoke-Expression "$gitCmd remote add origin https://github.com/nivassrig-testing/sri_testing_repo.git"

Write-Host "Pushing to GitHub..."
Invoke-Expression "$gitCmd push -u origin main"

Write-Host "Deployment Complete."
