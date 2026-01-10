@echo off
echo ========================================
echo Building T-Shirt Converter Executable
echo ========================================
echo.

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Building executable...
python -m PyInstaller --onefile --name "TShirt-Converter" tshirt_converter.py

echo.
echo ========================================
echo Build Complete!
echo ========================================
echo.
echo Your executable is located at:
echo dist\TShirt-Converter.exe
echo.
pause
