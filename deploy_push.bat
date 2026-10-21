@echo off
echo ========================================================
echo Pushing John Wick Arms to GitHub Repository...
echo Target: https://github.com/akash-07-git-io/john-wick-arms.git
echo ========================================================
git branch -M main
git push -u origin main
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] Code pushed successfully to GitHub!
) else (
    echo.
    echo [NOTICE] If the repository does not exist on GitHub yet:
    echo 1. Go to your open browser tab at https://github.com/new
    echo 2. Repository name: john-wick-arms
    echo 3. Visibility: Public
    echo 4. Leave "Add a README file" UNCHECKED
    echo 5. Click "Create repository"
    echo 6. Re-run this script: .\deploy_push.bat
)
pause
