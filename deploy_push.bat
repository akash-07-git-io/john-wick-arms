@echo off
echo ========================================================
echo Pushing John Wick Arms to GitHub Repository...
echo Target: https://github.com/akash-07-git-io/john-wick-arms.git
echo ========================================================
git branch -M main
git push origin main
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] Code pushed successfully to GitHub!
    echo Repository: https://github.com/akash-07-git-io/john-wick-arms
) else (
    echo.
    echo [ERROR] Push failed. Please check your network connection or Git credentials.
)
pause
