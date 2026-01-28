# 🎨 AAVARTAN T-Shirt Design Data Converter

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-2.0.0-orange.svg)

A comprehensive CLI toolkit to convert Google Form data into Photoshop-ready CSV format for variable data printing. Built for AAVARTAN committee merchandising workflow.

## 🚀 Quick Start

### Option 1: Use the Standalone Executable (Recommended)
1. Download `TShirt-Converter.exe` from the [releases](../../releases)
2. Double-click to run in interactive mode
3. No Python installation required!

### Option 2: Run from Source
```bash
# Clone the repository
git clone <repository-url>
cd "Printing data"

# Install dependencies
pip install -r requirements.txt

# Run any converter
python tshirt_converter.py
```

## 📦 Building the Executable

```bash
# Windows
build_executable.bat

# Or manually
pip install -r requirements.txt
python -m PyInstaller --onefile --name "TShirt-Converter" tshirt_converter.py
```

The executable will be created in the `dist/` folder.

## 💡 Usage

### All-in-One Converter (Interactive Mode)
```bash
TShirt-Converter.exe
# or
python tshirt_converter.py
```

### Individual Converters

#### 1. Core Team Members
```bash
# With number field for printing
python convert_cores.py cores.csv output_cores.csv

# Command line
TShirt-Converter.exe cores cores.csv output.csv
```

#### 2. Executive Team Members  
```bash
# Without number field
python convert_exes.py exes.csv output_exes.csv

# Command line
TShirt-Converter.exe exes exes.csv output.csv
```

#### 3. VOA (Volunteers/Public) Orders
```bash
# Handles both legacy and new form formats
python convert_voa.py VOA.csv voa_orders.csv
```

#### 4. Size Extraction (Distribution Lists)
```bash
# Extract name, domain, and size for distribution
python extract_sizes.py cores cores.csv cores_sizes.csv
python extract_sizes.py exes exes.csv exes_sizes.csv
```

#### 5. Printing Summary Generator
```bash
# Generate design-wise and size-wise counts
python generate_printing_summary.py voa_orders.csv printing_summary.csv
```

## ✨ Features

### Core Converters
- 🎯 **Smart Domain Mapping** - Auto-converts form domains to Photoshop names
- 🔢 **Number Conflict Resolution** - First-come-first-served with intelligent reassignment
- ✂️ **Name Shortening** - Auto-truncates names longer than 12 characters
- 🚫 **Data Validation** - Skips incomplete rows and validates input
- 📊 **Progress Feedback** - Real-time updates and domain breakdowns
- 💾 **Standalone Executable** - Share with team, no setup needed

### VOA Converter (New!)
- 📋 **Dual Format Support** - Handles both legacy (numerical) and new (text) form formats
- 🎨 **Multiple Designs** - Technocracy, Dharma, Abyss, and Jacket support
- 🔄 **Smart Distribution** - Evenly distributes quantities across selected designs
- 🧹 **Typo Handling** - Cleans up size entries like "1 'M'", "S.", "1L", etc.
- 📱 **Contact Info** - Preserves email, phone, and residency for distribution

### Size Extraction
- 📦 **Distribution Lists** - Extract name, domain, and size for easy distribution
- 📊 **Size Breakdowns** - Shows counts by size for ordering

### Printing Summary
- 🖨️ **Production Ready** - Design × Size quantity matrix
- 📈 **Multiple Views** - By design, by size, and grand totals
- 📋 **Printer Friendly** - Ready to send to printing service

## 📋 Input Formats

### Cores (Core Team Members)
Google Form CSV with these columns:
- Timestamp, Email Address, NAME, CONTACT NUMBER, E-MAIL
- **Name On Merch:**
- **Number on Merch (0 to 99)**
- BRANCH, Residency, **Mention Your Size:**
- Payment details
- **Domain**

### Executives
Same as cores but **WITHOUT** "Number on Merch (0 to 99)" column.

### VOA (Volunteers & Public)
**Legacy Format:**
- Numerical columns: `Sizes X Quantities (Oversized T-shirt) [S/M/L/XL/XXL]`
- Aesthetics column with design selections

**New Format:**
- Text fields: "For Technocracy Blending Merch, enter quantity and Size"
- Format: "M,M,S" or "L,L,XL"

See [examples/](examples/) folder for complete samples.

## 📤 Output Formats

### Cores
```csv
name,domain,number,design,tech,spons,pr,em,doc,vigyaan
John,Design & Editing,5,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE
Jane,Event Management,7,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE
```

### Executives
```csv
name,domain,design,tech,spons,pr,em,doc,vigyaan
John,Design & Editing,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE
```

### VOA Orders
```csv
name,email,contact,residency,design,size
Student One,student1@gmail.com,9876543210,BOYS HOSTEL,Technocracy,M
Student One,student1@gmail.com,9876543210,BOYS HOSTEL,Dharma,M
```

### Size Distribution
```csv
name,domain,size
John,Design & Editing,M
Jane,Event Management,S
```

### Printing Summary
```csv
design,size,quantity
Technocracy,S,8
Technocracy,M,14
Abyss,L,6
```

## 🗺️ Domain Mapping

| Google Form Option          | Photoshop Value    |
|----------------------------|--------------------|
| Sponsorship & Marketing    | Sponsorship        |
| Media & Public Relations   | Media and PR       |
| Design & Editing           | Design & Editing   |
| Vigyaan                    | Vigyaan            |
| Event Management           | Event Management   |
| Tech                       | Tech               |
| Documentation              | Documentation      |

## 🔢 Number Conflict Resolution (Cores Only)

When multiple people choose the same number:
1. ✅ First person (earliest timestamp) gets their requested number
2. 🎲 Others get randomly assigned numbers (1-99) that don't conflict
3. 📢 Console shows which numbers were reassigned

## 📁 Project Structure

```
.
├── tshirt_converter.py      # Main unified CLI application
├── convert_cores.py          # Cores converter
├── convert_exes.py           # Executives converter
├── convert_voa.py            # VOA/Public orders converter
├── extract_sizes.py          # Size extraction for distribution
├── generate_printing_summary.py  # Printing quantity summary
├── build_executable.bat      # One-click build script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── USAGE.md                  # Detailed usage guide
├── .gitignore               # Git ignore rules
├── examples/                 # Sample input files
│   ├── cores_example.csv
│   ├── exes_example.csv
│   ├── voa_example.csv
│   └── README.md
└── dist/                     # Built executables (generated)
    └── TShirt-Converter.exe
```

## 🛠️ Requirements

- Python 3.8+
- pandas >= 2.0.0
- pyinstaller >= 6.0.0 (for building executable)

## 📖 Documentation

- [USAGE.md](USAGE.md) - Comprehensive usage guide
- [examples/](examples/) - Sample input CSV files
- [examples/README.md](examples/README.md) - Input format documentation

## 🤝 Contributing

This project is built for AAVARTAN NIT Raipur. For improvements or issues:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📝 Example Workflow

```bash
# 1. Convert committee member data
python convert_cores.py cores.csv output_cores.csv
python convert_exes.py exes.csv output_exes.csv

# 2. Extract size lists for distribution
python extract_sizes.py cores cores.csv cores_sizes.csv
python extract_sizes.py exes exes.csv exes_sizes.csv

# 3. Convert public orders
python convert_voa.py VOA.csv voa_orders.csv

# 4. Generate printing summary for vendors
python generate_printing_summary.py voa_orders.csv printing_summary.csv
```

## 📊 Example Output

```
========================================
  AAVARTAN T-Shirt Design Data Converter
========================================

📋 Reading input file...
✓ Found 25 entries

📝 Shortened 'Prashast Sidhant' to 'Prashast'

🔍 Checking for number conflicts...
⚠️  Conflict: PRANAV requested #7 but it was taken. Assigned #43

💾 Saving to cores_photoshop.csv...
✅ Conversion complete! 25 records processed.

📊 Domain breakdown:
Vigyaan              6
Event Management     5
Sponsorship          2
Design & Editing     1
```

## 🆕 What's New in v2.0.0

- ✨ VOA (Volunteers/Public) order converter
- 📦 Size extraction tool for distribution
- 🖨️ Printing summary generator
- 🧹 Enhanced typo handling for size entries
- 📋 Dual format support (legacy + new)
- 📁 Example files for all converters
- 📚 Comprehensive documentation

## 📄 License

MIT License - feel free to use and modify for your needs.

## 🎓 About AAVARTAN

AAVARTAN is the annual techno-management fest of NIT Raipur. This toolkit streamlines the merchandise printing workflow for committee members and public orders.

---

Made with ❤️ for AAVARTAN 2025-26

## 🚀 Quick Start

### Option 1: Use the Standalone Executable (Recommended)
1. Download `TShirt-Converter.exe` from the [releases](../../releases)
2. Double-click to run in interactive mode
3. No Python installation required!

### Option 2: Run from Source
```bash
# Clone the repository
git clone <repository-url>
cd "Printing data"

# Install dependencies
pip install -r requirements.txt

# Run the unified converter
python tshirt_converter.py
```

## 📦 Building the Executable

```bash
# Windows
build_executable.bat

# Or manually
pip install -r requirements.txt
python -m PyInstaller --onefile --name "TShirt-Converter" tshirt_converter.py
```

The executable will be created in the `dist/` folder.

## 💡 Usage

### Interactive Mode (Easiest)
```bash
TShirt-Converter.exe
```
Follow the on-screen prompts to select your conversion type and files.

### Command-Line Mode
```bash
# For Cores (with number field)
TShirt-Converter.exe cores input.csv output.csv

# For Executives (no number field)
TShirt-Converter.exe exes input.csv output.csv
```

### Python Scripts (Legacy)
```bash
# Cores
python convert_cores.py cores_data.csv output.csv

# Executives
python convert_exes.py exes_data.csv output.csv
```

## ✨ Features

- 🎯 **Smart Domain Mapping** - Automatically converts form domains to Photoshop variable names
- 🔢 **Number Conflict Resolution** - First-come-first-served with intelligent reassignment
- ✂️ **Name Shortening** - Automatically truncates names longer than 12 characters
- 🚫 **Data Validation** - Skips incomplete rows and validates input
- 📊 **Progress Feedback** - Real-time updates and domain breakdowns
- 💾 **Standalone Executable** - Share with your team, no setup needed
- 🎨 **Photoshop Ready** - Direct CSV import with proper column headers

## 📋 Input Format

### Cores (Core Team Members)
Google Form CSV with these columns:
- Timestamp
- Email Address
- NAME
- CONTACT NUMBER
- E-MAIL
- **Name On Merch:**
- **Number on Merch (0 to 99)**
- BRANCH
- Choose your place of residency
- Mention Your Size:
- Enter Total Amount paid
- Payment screenshot
- **Domain**

### Executives
Same as cores but **WITHOUT** "Number on Merch (0 to 99)" column.

## 📤 Output Format

### Cores
```csv
name,domain,number,design,tech,spons,pr,em,doc,vigyaan
TARUNA,Design & Editing,3,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE
Sanskar,Event Management,7,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE
```

### Executives
```csv
name,domain,design,tech,spons,pr,em,doc,vigyaan
TARUNA,Design & Editing,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE
```

## 🗺️ Domain Mapping

| Google Form Option          | Photoshop Value    |
|----------------------------|--------------------|
| Sponsorship & Marketing    | Sponsorship        |
| Media & Public Relations   | Media and PR       |
| Design & Editing           | Design & Editing   |
| Vigyaan                    | Vigyaan            |
| Event Management           | Event Management   |
| Tech                       | Tech               |
| Documentation              | Documentation      |

## 🔢 Number Conflict Resolution (Cores Only)

When multiple people choose the same number:
1. ✅ First person (earliest timestamp) gets their requested number
2. 🎲 Others get randomly assigned numbers (1-99) that don't conflict
3. 📢 Console shows which numbers were reassigned

## 📁 Project Structure

```
.
├── tshirt_converter.py      # Main unified CLI application
├── convert_cores.py          # Legacy cores converter
├── convert_exes.py           # Legacy executives converter
├── build_executable.bat      # One-click build script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── USAGE.md                  # Detailed usage guide
├── .gitignore               # Git ignore rules
└── dist/                     # Built executables (generated)
    └── TShirt-Converter.exe
```

## 🛠️ Requirements

- Python 3.8+
- pandas >= 2.0.0
- pyinstaller >= 6.0.0 (for building executable)

## 📖 Documentation

- [USAGE.md](USAGE.md) - Comprehensive usage guide
- [Example Data](cores.csv) - Sample input format

## 🤝 Contributing

This project is built for AAVARTAN NIT Raipur. For improvements or issues:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📝 Example Output

```
========================================
  AAVARTAN T-Shirt Design Data Converter
  Convert Google Form data to Photoshop format
========================================

📋 Reading input file...
✓ Found 15 entries

📝 Shortened 'Prashast Sidhant' to 'Prashast'

🔍 Checking for number conflicts...
⚠️  Conflict: PRANAV requested #7 but it was taken. Assigned #43

💾 Saving to cores_photoshop.csv...
✅ Conversion complete! 15 records processed.

📊 Domain breakdown:
Vigyaan              6
Event Management     5
Sponsorship          2
Design & Editing     1
Tech                 1
```

## 📄 License

MIT License - feel free to use and modify for your needs.

## 🎓 About AAVARTAN

AAVARTAN is the annual techno-management fest of NIT Raipur. This tool streamlines the merchandise printing workflow for committee members.

---

Made with ❤️ for AAVARTAN 2025-26
