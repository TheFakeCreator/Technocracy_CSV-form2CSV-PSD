# T-Shirt Converter - Usage Guide

## Building the Executable

### Step 1: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 2: Build Executable
**On Windows:**
```bash
build_executable.bat
```

**Or manually:**
```bash
pyinstaller --onefile --name "TShirt-Converter" tshirt_converter.py
```

The executable will be created in the `dist` folder.

## Using the Application

### Method 1: Interactive Mode (Recommended)
Double-click `TShirt-Converter.exe` or run it without arguments:
```bash
TShirt-Converter.exe
```

The app will guide you through:
1. Selecting conversion type (Cores or Exes)
2. Entering input file path
3. Entering output file path (or using default)

### Method 2: Command-Line Mode

**For Cores:**
```bash
TShirt-Converter.exe cores input.csv output.csv
```

**For Executives:**
```bash
TShirt-Converter.exe exes input.csv output.csv
```

If you don't specify an output file, it will use defaults:
- Cores: `cores_photoshop.csv`
- Exes: `exes_photoshop.csv`

## Quick Examples

### Interactive Mode
```
> TShirt-Converter.exe

Select conversion type:
1. Cores (with number field)
2. Executives (no number field)
3. Exit

Enter your choice (1-3): 1

Enter input CSV file path: cores_data.csv

Enter output CSV file path (press Enter for 'cores_photoshop.csv'): 

[Processing happens...]
✅ Conversion complete!
```

### Command-Line Mode
```bash
# Convert cores data
TShirt-Converter.exe cores "D:\data\cores.csv" "D:\output\final.csv"

# Convert exes data with default output name
TShirt-Converter.exe exes exes_data.csv
```

## Features

✅ **Interactive GUI-like experience** - No need to remember commands  
✅ **Automatic domain mapping** - Converts form domains to Photoshop names  
✅ **Number conflict resolution** - First-come-first-served with auto-reassignment  
✅ **Smart name shortening** - Keeps names under 12 characters  
✅ **Progress feedback** - See what's happening in real-time  
✅ **Error handling** - Clear error messages with suggestions  

## Distribution

You can share just the executable file (`TShirt-Converter.exe`) with your team. They don't need Python installed!

### What to share:
- `TShirt-Converter.exe` (from the `dist` folder)
- This `USAGE.md` file for instructions

No other files needed! The executable is completely standalone.
