# Example Input Files

This folder contains example CSV files showing the expected input format for each converter script.

## Files

### 1. cores_example.csv
Example input for **Core Team Members**

**Used with:** 
- `convert_cores.py`
- `tshirt_converter.py cores`

**Key fields:**
- `Name On Merch:` - Name to be printed
- `Number on Merch (0 to 99)` - Jersey number
- `Domain` - Team domain (will be mapped)
- `Mention Your Size:` - T-shirt size

**Output:** Creates file with name, domain, number, and TRUE/FALSE flags for each domain.

---

### 2. exes_example.csv
Example input for **Executive Team Members**

**Used with:**
- `convert_exes.py`
- `tshirt_converter.py exes`

**Key fields:**
- `Name On Merch:` - Name to be printed
- `Domain` - Team domain (will be mapped)
- `Mention Your Size:` - T-shirt size

**Note:** No "Number on Merch" field for executives.

**Output:** Creates file with name, domain, and TRUE/FALSE flags for each domain.

---

### 3. voa_example.csv
Example input for **Volunteers and General Public Orders**

**Used with:**
- `convert_voa.py`

**Key fields:**
- `NAME` - Customer name
- `CONTACT NUMBER` - Phone number
- `Choose your place of residency` - For distribution
- Legacy format: `Sizes X Quantities (Oversized T-shirt) [S/M/L/XL/XXL]`
- New format: Text fields like "For Technocracy Blending Merch, enter quantity and Size"

**Output:** One row per order item with name, contact, design, and size.

---

## Usage

Replace the example data with your actual Google Form exports and run the corresponding converter:

```bash
# For cores
python convert_cores.py your_cores_data.csv output.csv

# For executives  
python convert_exes.py your_exes_data.csv output.csv

# For VOA orders
python convert_voa.py your_voa_data.csv voa_orders.csv
```

## Additional Tools

### Extract Sizes
Get distribution list with names, domains, and sizes:
```bash
python extract_sizes.py cores your_cores_data.csv
```

### Generate Printing Summary
Get design-wise and size-wise counts:
```bash
python generate_printing_summary.py voa_orders.csv printing_summary.csv
```
