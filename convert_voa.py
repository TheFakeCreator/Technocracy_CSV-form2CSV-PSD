import pandas as pd
import sys
import os
import re

def print_banner():
    """Print application banner"""
    print("\n" + "="*60)
    print("  VOA Merchandise Order Converter - AAVARTAN")
    print("  Convert volunteer/public orders to printing format")
    print("="*60 + "\n")

def parse_size_entry(entry):
    """Parse size entries like 'M,M,S' or '1 L' or '1'M'' or 'S.' into list"""
    if pd.isna(entry) or str(entry).strip().lower() in ['none', 'nan', '']:
        return []
    
    entry_str = str(entry).strip()
    # Remove quotes, numbers, periods, and extra spaces
    entry_str = entry_str.replace("'", "").replace('"', '').replace('.', '').strip()
    
    # Split by comma
    sizes = [s.strip().upper() for s in entry_str.split(',') if s.strip()]
    
    # Clean each size entry
    cleaned_sizes = []
    for size in sizes:
        # Remove any leading/trailing whitespace and digits
        size_clean = size.strip()
        
        # Extract just the size letter(s) using regex
        # This handles: "1 L", "1'M'", "S ", "XL ", etc.
        match = re.search(r'(XXL|XL|[SMLX])', size_clean.upper())
        if match:
            cleaned_sizes.append(match.group(1))
        elif size_clean and size_clean.isalpha() and len(size_clean) <= 3:
            # Fallback: if it's just letters and short, assume it's a size
            cleaned_sizes.append(size_clean.upper())
    
    return cleaned_sizes

def get_design_name(design_option):
    """Simplify design names"""
    design_map = {
        'Technocracy Blending': 'Technocracy',
        'Dharma Warrior': 'Dharma',
        'Conquering The Abyss': 'Abyss'
    }
    for key, value in design_map.items():
        if key.lower() in design_option.lower():
            return value
    return design_option

def convert_voa_data(input_file, output_file):
    """Convert VOA merchandise orders to printing format"""
    print(f"\n📋 Reading VOA data from: {input_file}")
    
    df = pd.read_csv(input_file)
    print(f"✓ Found {len(df)} entries")
    
    output_data = []
    skipped = 0
    
    # Column mappings for size entries
    tshirt_cols = {
        'S': 'Sizes X Quantities (Oversized T-shirt) [S]',
        'M': 'Sizes X Quantities (Oversized T-shirt) [M]',
        'L': 'Sizes X Quantities (Oversized T-shirt) [L]',
        'XL': 'Sizes X Quantities (Oversized T-shirt) [XL]',
        'XXL': 'Sizes X Quantities (Oversized T-shirt) [XXL]'
    }
    
    # Text field columns
    text_fields = {
        'Technocracy': 'For Technocracy Blending Merch, enter quantity and Size.\n\nExample: Suppose you want to order 3 \'M\' sized black T-shirts, enter them as M,M,M.\nSimilarly, if you want 5 \'XL\' sized tees, enter them as \nXL,XL,XL,XL,XL\nIf you want to order 2 \'M\' sized and 1 \'L\' sized tee, \nenter them as M,M,L.\n\nEnter \'None\', in case you do not wish to order for this design.',
        'Dharma': 'For Dharma Warrior Merch, enter quantity and Size.\n\nExample: Suppose you want to order 3 \'M\' sized black T-shirts, enter them as M,M,M.\nSimilarly, if you want 5 \'XL\' sized tees, enter them as \nXL,XL,XL,XL,XL\nIf you want to order 2 \'M\' sized and 1 \'L\' sized tee, \nenter them as M,M,L.\n\nEnter \'None\', in case you do not wish to order for this design.',
        'Abyss': 'For Conquering The Abyss Merch, enter quantity and Size.\n\nExample: Suppose you want to order 3 \'M\' sized black T-shirts, enter them as M,M,M.\nSimilarly, if you want 5 \'XL\' sized tees, enter them as \nXL,XL,XL,XL,XL\nIf you want to order 2 \'M\' sized and 1 \'L\' sized tee, \nenter them as M,M,L.\n\nEnter \'None\', in case you do not wish to order for this design.',
        'Jacket': 'For Jacket, enter quantity and Size.\n\nExample: Suppose you want to order 3 \'M\' sized black T-shirts, enter them as M,M,M.\nSimilarly, if you want 5 \'XL\' sized tees, enter them as \nXL,XL,XL,XL,XL\nIf you want to order 2 \'M\' sized and 1 \'L\' sized tee, \nenter them as M,M,L.\n\nEnter \'None\', in case you do not wish to order for this design.'
    }
    
    for idx, row in df.iterrows():
        name = str(row['NAME']).strip()
        
        # Skip rows with missing name
        if name == 'nan' or name == '':
            print(f"⚠️  Skipping row {idx+2} - missing name")
            skipped += 1
            continue
        
        # Extract contact info
        contact = str(row['CONTACT NUMBER']).strip()
        email = str(row.get('Email Address', row.get('E-MAIL', ''))).strip()
        residency = str(row['Choose your place of residency (FOR DISTRIBUTION PURPOSES)']).strip()
        
        # Collect all orders
        orders = []
        
        # Method 1: Check legacy numerical columns first
        legacy_orders = False
        aesthetics = str(row.get('Choose your aesthetics! (Offers are available at specific order quantities. For combo order select multiple options)', '')).strip()
        
        # Parse multiple designs from aesthetics ONCE (outside the size loop)
        designs_list = []
        if 'Technocracy' in aesthetics:
            designs_list.append('Technocracy')
        if 'Dharma' in aesthetics:
            designs_list.append('Dharma')
        if 'Abyss' in aesthetics or 'Conquering' in aesthetics:
            designs_list.append('Abyss')
        
        # If no design specified, assume Technocracy (default)
        if not designs_list:
            designs_list = ['Technocracy']
        
        for size_key, col_name in tshirt_cols.items():
            if col_name in df.columns:
                try:
                    quantity = int(float(row[col_name])) if pd.notna(row[col_name]) and str(row[col_name]).strip() != '' else 0
                    if quantity > 0:
                        legacy_orders = True
                        
                        # Distribute quantity across selected designs
                        # If quantity matches or is multiple of designs, distribute evenly
                        num_designs = len(designs_list)
                        
                        if quantity % num_designs == 0:
                            # Evenly divisible - each design gets equal share
                            per_design = quantity // num_designs
                            for design in designs_list:
                                for _ in range(per_design):
                                    orders.append({
                                        'design': design,
                                        'size': size_key
                                    })
                        else:
                            # Not evenly divisible - distribute as evenly as possible
                            base_qty = quantity // num_designs
                            extra = quantity % num_designs
                            
                            for i, design in enumerate(designs_list):
                                # First 'extra' designs get one additional item
                                design_qty = base_qty + (1 if i < extra else 0)
                                for _ in range(design_qty):
                                    orders.append({
                                        'design': design,
                                        'size': size_key
                                    })
                            
                            if extra > 0:
                                print(f"📝 {name}: {quantity} items across {num_designs} designs - distributed unevenly")
                except (ValueError, TypeError):
                    pass
        
        # Method 2: If no legacy orders, check text field entries
        if not legacy_orders:
            for design, col_name in text_fields.items():
                if col_name in df.columns and col_name in row.index:
                    sizes = parse_size_entry(row[col_name])
                    for size in sizes:
                        orders.append({
                            'design': design,
                            'size': size
                        })
        
        # If no orders found, skip
        if not orders:
            print(f"⚠️  {name}: No orders found")
            skipped += 1
            continue
        
        # Create one row per order item
        for order in orders:
            output_row = {
                'name': name,
                'email': email if email != 'nan' else '',
                'contact': contact if contact != 'nan' else '',
                'residency': residency if residency != 'nan' else '',
                'design': order['design'],
                'size': order['size']
            }
            output_data.append(output_row)
    
    # Create DataFrame
    output_df = pd.DataFrame(output_data)
    
    if len(output_df) == 0:
        print("\n❌ No valid orders found!")
        return
    
    # Save to CSV
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Conversion complete! {len(output_df)} order items from {len(output_df['name'].unique())} people ({skipped} entries skipped).")
    
    # Show breakdowns
    print(f"\n📊 Design breakdown:")
    print(output_df['design'].value_counts().to_string())
    
    print(f"\n📊 Size breakdown:")
    print(output_df['size'].value_counts().to_string())
    
    print(f"\n📊 Residency breakdown:")
    print(output_df['residency'].value_counts().to_string())

def interactive_mode():
    """Run in interactive mode"""
    print_banner()
    
    input_file = input("Enter VOA CSV file path: ").strip().strip('"')
    
    if not os.path.exists(input_file):
        print(f"\n❌ Error: File '{input_file}' not found!")
        return
    
    default_output = "voa_orders.csv"
    output_file = input(f"Enter output CSV file path (press Enter for '{default_output}'): ").strip().strip('"')
    
    if not output_file:
        output_file = default_output
    
    try:
        convert_voa_data(input_file, output_file)
        print(f"\n✨ Output saved to: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"\n❌ Error during conversion: {e}")
        import traceback
        traceback.print_exc()
    
    input("\nPress Enter to exit...")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Command-line mode
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "voa_orders.csv"
        
        try:
            convert_voa_data(input_file, output_file)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()
