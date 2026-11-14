@echo off
title ZenithMart - QA Testing Portfolio Launcher
color 0B
cls

echo =====================================================================
echo           ZENITHMART E-COMMERCE QA TESTING PROJECT LAUNCHER
echo =====================================================================
echo.
echo   [1] Open Demo Web Application in Browser (Default)
echo   [2] Open Test Summary Report (PDF)
echo   [3] Open Manual Test Cases (Excel .xlsx)
echo   [4] Open Bug Reports (Excel .xlsx)
echo   [5] Run Selenium Automated Test Suite (Pytest)
echo   [6] Open Automation HTML Test Report
echo   [7] Start Local HTTP Server (http://localhost:8000)
echo   [0] Exit
echo.
echo =====================================================================
set /p choice="Enter your choice [1-7, or press Enter for 1]: "

if "%choice%"=="" set choice=1
if "%choice%"=="1" goto open_app
if "%choice%"=="2" goto open_pdf
if "%choice%"=="3" goto open_testcases
if "%choice%"=="4" goto open_bugs
if "%choice%"=="5" goto run_tests
if "%choice%"=="6" goto open_report
if "%choice%"=="7" goto start_server
if "%choice%"=="0" goto exit

:open_app
echo.
echo Opening ZenithMart Demo Application in default browser...
start "" "%~dp0application\index.html"
goto end

:open_pdf
echo.
echo Opening Test Summary Report PDF...
start "" "%~dp0reports\test-summary-report.pdf"
goto end

:open_testcases
echo.
echo Opening Manual Test Cases in Excel...
start "" "%~dp0test-cases\test-cases.xlsx"
goto end

:open_bugs
echo.
echo Opening Bug Reports in Excel...
start "" "%~dp0bug-reports\bug-report.xlsx"
goto end

:run_tests
echo.
echo =====================================================================
echo Running Selenium Automated Test Suite (Pytest)...
echo =====================================================================
python -m pytest "%~dp0automation\tests" --html="%~dp0automation\reports\automation-report.html" --self-contained-html
echo.
echo Automation execution completed! Opening HTML report...
start "" "%~dp0automation\reports\automation-report.html"
pause
goto end

:open_report
echo.
echo Opening Pytest HTML Automation Report...
start "" "%~dp0automation\reports\automation-report.html"
goto end

:start_server
echo.
echo Starting local web server at http://localhost:8000/application/ ...
start "" "http://localhost:8000/application/"
cd /d "%~dp0"
python -m http.server 8000
goto end

:exit
exit

:end
