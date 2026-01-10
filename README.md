# 🎨 AAVARTAN T-Shirt Design Data Converter

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A powerful CLI tool to convert Google Form data into Photoshop-ready CSV format for variable data printing. Built for AAVARTAN committee merchandising workflow.

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
