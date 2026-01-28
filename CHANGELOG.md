# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2026-01-28

### 🎉 Major Release - Complete Merchandising Workflow

### Added
- **VOA Converter** (`convert_voa.py`) - Converts volunteer and public merchandise orders
  - Supports both legacy (numerical) and new (text-based) Google Form formats
  - Handles multiple design selections (Technocracy, Dharma, Abyss, Jacket)
  - Intelligent quantity distribution across selected designs
  - Advanced typo handling for size entries
  - Contact information preservation for distribution
  
- **Size Extraction Tool** (`extract_sizes.py`) - Extracts distribution lists
  - Generates name, domain, and size CSV for easy distribution
  - Supports both cores and executives formats
  - Interactive and command-line modes
  
- **Printing Summary Generator** (`generate_printing_summary.py`)
  - Creates design × size quantity matrix for printers
  - Shows breakdowns by design and size
  - Grand totals and detailed statistics
  - Production-ready format
  
- **Example Files** - Sample CSV files for all converters
  - `examples/cores_example.csv`
  - `examples/exes_example.csv`
  - `examples/voa_example.csv`
  - `examples/README.md` with format documentation

### Enhanced
- **Name Shortening Logic** - Only shortens names longer than 12 characters
  - Preserves reasonable-length names like "D. Rahul"
  - Smart first-name extraction for long names
  
- **Size Parser** - Robust handling of typos and variations
  - Handles "1 'M'", "1'L'", "S. ", "XL ", etc.
  - Removes quotes, numbers, and periods
  - Regex-based extraction for accuracy
  
- **Data Validation** - Enhanced error handling
  - Skips rows with missing critical data
  - Warns about invalid entries
  - Progress feedback during conversion

### Fixed
- Comma-separated CSV output (was using tabs)
- Legacy form quantity distribution logic
- Email field mapping inconsistencies

### Documentation
- Complete README overhaul with all tools
- CHANGELOG.md (this file)
- Updated USAGE.md
- Example file documentation
- Comprehensive workflow guide

### Project Structure
- Added `files/` folder to .gitignore
- Created `examples/` folder for sample files
- Better organization of output files

## [1.0.0] - 2026-01-10

### Initial Release

### Added
- **Core Team Converter** (`convert_cores.py`)
  - Number conflict resolution
  - First-come-first-served with random reassignment
  - Domain mapping support
  
- **Executive Converter** (`convert_exes.py`)
  - Same as cores without number field
  
- **Unified CLI** (`tshirt_converter.py`)
  - Interactive mode
  - Command-line mode
  - Both cores and exes support
  
- **Build System**
  - PyInstaller configuration
  - `build_executable.bat`
  - Standalone executable generation
  
- **Domain Mapping**
  - "Sponsorship & Marketing" → "Sponsorship"
  - "Media & Public Relations" → "Media and PR"
  - Other domains preserved
  
- **TRUE/FALSE Flags** - Domain visibility columns
  - design, tech, spons, pr, em, doc, vigyaan
  
- **Documentation**
  - README.md
  - USAGE.md
  - requirements.txt
  - .gitignore

### Features
- Tab-separated CSV output for Photoshop
- Progress indicators and statistics
- Error handling and validation
- Python 3.8+ compatibility

---

## Version History

- **v2.0.0** (2026-01-28) - Complete workflow with VOA support
- **v1.0.0** (2026-01-10) - Initial release with core/exec converters
