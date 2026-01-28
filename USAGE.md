# AAVARTAN Merchandise Toolkit - Usage Guide

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
python -m PyInstaller --onefile --name "TShirt-Converter" tshirt_converter.py
```

The executable will be created in the `dist` folder.

## Using the Application

### Method 1: Interactive Mode (Recommended)
Double-click `TShirt-Converter.exe` or run it without arguments:
```bash
TShirt-Converter.exe
```

The app will guide you through:
1. Selecting the tool (Cores/Exes/VOA/Sizes/Summary)
2. Entering input file path
3. Entering output file path (or using default)

### Method 2: Command-Line Mode

**For Core Team:**
```bash
TShirt-Converter.exe cores input.csv output.csv
```

**For Executives:**
```bash
TShirt-Converter.exe exes input.csv output.csv
```

**For VOA Orders:**
```bash
TShirt-Converter.exe voa VOA.csv voa_orders.csv
```

**For Size Extraction:**
```bash
TShirt-Converter.exe sizes cores cores.csv sizes.csv
TShirt-Converter.exe sizes exes exes.csv sizes.csv
```

**For Printing Summary:**
```bash
TShirt-Converter.exe summary voa_orders.csv printing_summary.csv
```

If you don't specify an output file, it will use defaults:
- Cores: `cores_photoshop.csv`
- Exes: `exes_photoshop.csv`
- VOA: `voa_orders.csv`
- Sizes: `sizes.csv`
- Summary: `printing_summary.csv`

## Quick Examples

### Interactive Mode
```
> TShirt-Converter.exe

======================================================================
  AAVARTAN Merchandise Toolkit v2.0.0
  Complete workflow for committee & public merchandise
======================================================================

Select tool:
1. Core Team Converter (with numbers)
2. Executive Team Converter (no numbers)
3. VOA Orders Converter (volunteers/public)
4. Size Extraction (distribution lists)
5. Printing Summary Generator
6. Exit

Enter your choice (1-6): 3

Enter input CSV file path: VOA.csv

Enter output CSV file path (press Enter for 'voa_orders.csv'): 

📋 Reading VOA data from: VOA.csv
✓ Found 25 entries
💾 Saving to voa_orders.csv...
✅ Conversion complete! 86 order items from 25 people (2 entries skipped).

📊 Design breakdown:
Technocracy    34
Dharma         22
Abyss          26
Jacket          4
```

### Command-Line Mode
```bash
# Complete workflow
TShirt-Converter.exe cores "files/cores.csv" cores_photoshop.csv
TShirt-Converter.exe exes "files/exes.csv" exes_photoshop.csv
TShirt-Converter.exe voa "files/VOA.csv" voa_orders.csv
TShirt-Converter.exe sizes cores "files/cores.csv" cores_sizes.csv
TShirt-Converter.exe summary voa_orders.csv printing_summary.csv
```

## Features

✅ **5 integrated tools** - Complete merchandising workflow  
✅ **Interactive menu** - No need to remember commands  
✅ **VOA support** - Handles both legacy and new form formats  
✅ **Size extraction** - Generate distribution lists  
✅ **Printing summaries** - Design×size quantity matrix  
✅ **Automatic domain mapping** - Converts form domains to Photoshop names  
✅ **Number conflict resolution** - First-come-first-served with auto-reassignment  
✅ **Smart name shortening** - Keeps names under 12 characters  
✅ **Progress feedback** - See what's happening in real-time  
✅ **Error handling** - Clear error messages with suggestions  

## Complete Workflow

### Step 1: Convert Committee Data
```bash
# Cores with jersey numbers
TShirt-Converter.exe cores cores_form.csv cores_photoshop.csv

# Exes without numbers
TShirt-Converter.exe exes exes_form.csv exes_photoshop.csv
```

### Step 2: Extract Distribution Lists
```bash
# For distribution planning
TShirt-Converter.exe sizes cores cores_form.csv cores_sizes.csv
TShirt-Converter.exe sizes exes exes_form.csv exes_sizes.csv
```

### Step 3: Process Public Orders
```bash
# VOA orders from volunteers/public
TShirt-Converter.exe voa VOA_form.csv voa_orders.csv
```

### Step 4: Generate Printing Summary
```bash
# Create design-wise summary for printers
TShirt-Converter.exe summary voa_orders.csv printing_summary.csv
```

## Distribution

You can share just the executable file (`TShirt-Converter.exe`) with your team. They don't need Python installed!

### What to share:
- `TShirt-Converter.exe` (from the `dist` folder)
- This `USAGE.md` file for instructions
- Example files from `examples/` folder (optional)

No other files needed! The executable is completely standalone.
