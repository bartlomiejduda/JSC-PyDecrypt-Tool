
:: JSC BATCH DECRYPT SCRIPT
:: It can decrypt all files from INPUT directory

:: Ver    Date        Name
:: v1.0   04.09.2022  Bartlomiej Duda

@ECHO OFF
echo JSC Decrypt Script by Bartlomiej Duda
echo Starting program...
echo.
echo.

setlocal enabledelayedexpansion

set ENCRYPTION_KEY="f86f2406-6ef3-45"

echo Activating venv...
CALL .\venv\Scripts\activate.bat

echo Decrypting files...
for %%f in (.\INPUT\*.jsc) do (

set input_file=%%f
set output_file=!input_file:jsc=js!
set output_file=!output_file:INPUT=OUTPUT!
echo !input_file!
echo !output_file!
python ".\jsc_pydecrypt_tool.py" "-d" !input_file! !ENCRYPTION_KEY! !output_file!

)

echo Program has finished!
pause

