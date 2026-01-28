import pandas as pd
import random
import sys
import os
import re

def print_banner():
    """Print application banner"""
    print("\n" + "="*70)
    print("  AAVARTAN Merchandise Toolkit v2.0.0")
    print("  Complete workflow for committee & public merchandise")
    print("="*70 + "\n")

def map_domain(domain):
    """Map domain names from Google Form to Photoshop format"""
    domain_mapping = {
        'Sponsorship & Marketing': 'Sponsorship',
        'Media & Public Relations': 'Media and PR',
        'Design & Editing': 'Design & Editing',
        'Vigyaan': 'Vigyaan',
        'Event Management': 'Event Management',
        'Tech': 'Tech',
        'Documentation': 'Documentation'
    }
    return domain_mapping.get(domain.strip(), domain.strip())

def get_domain_columns(domain):
    """Return TRUE/FALSE values for each domain column based on person's domain"""
    domain_cols = {
        'design': False,
        'tech': False,
        'spons': False,
        'pr': False,
        'em': False,
        'doc': False,
        'vigyaan': False
    }
    
    domain_lower = domain.lower()
    
    if 'design' in domain_lower:
        domain_cols['design'] = True
    elif 'tech' in domain_lower:
        domain_cols['tech'] = True
    elif 'sponsorship' in domain_lower or 'spons' in domain_lower:
        domain_cols['spons'] = True
    elif 'media' in domain_lower or 'pr' in domain_lower or 'public relations' in domain_lower:
        domain_cols['pr'] = True
    elif 'event' in domain_lower or 'em' in domain_lower:
        domain_cols['em'] = True
    elif 'doc' in domain_lower:
        domain_cols['doc'] = True
    elif 'vigyaan' in domain_lower:
        domain_cols['vigyaan'] = True
    
    return domain_cols

def resolve_number_conflicts(df):
    """Resolve conflicts when multiple people choose the same number"""
    df = df.sort_values('Timestamp')
    
    used_numbers = set()
    final_numbers = []
    
    for idx, row in df.iterrows():
        requested_number = row['number']
        
        if requested_number not in used_numbers:
            final_numbers.append(requested_number)
            used_numbers.add(requested_number)
        else:
            available_numbers = set(range(1, 100)) - used_numbers
            new_number = random.choice(list(available_numbers))
            final_numbers.append(new_number)
            used_numbers.add(new_number)
            print(f"⚠️  Conflict: {row['name']} requested #{requested_number} but it was taken. Assigned #{new_number}")
    
    df['number'] = final_numbers
    return df

def convert_cores_data(input_file, output_file):
    """Convert Google Form data for cores to Photoshop format"""
    print("\n📋 Reading input file...")
    
    df = pd.read_csv(input_file)
    print(f"✓ Found {len(df)} entries")
    
    output_data = []
    
    for idx, row in df.iterrows():
        name_full = str(row['Name On Merch:']).strip()
        domain_raw = str(row['Domain']).strip()
        
        if name_full == 'nan' or name_full == '' or domain_raw == 'nan' or domain_raw == '':
            print(f"⚠️  Skipping row {idx+2} - missing name or domain")
            continue
        
        if len(name_full) > 12:
            name = name_full.split()[0]
            print(f"📝 Shortened '{name_full}' to '{name}'")
        else:
            name = name_full
        
        domain = map_domain(domain_raw)
        
        try:
            number = int(float(row['Number on Merch (0 to 99)']))
        except:
            number = random.randint(1, 99)
            print(f"⚠️  Invalid number for {name}, assigned random: {number}")
        
        domain_cols = get_domain_columns(domain)
        
        output_row = {
            'name': name,
            'domain': domain,
            'number': number,
            'design': 'TRUE' if domain_cols['design'] else 'FALSE',
            'tech': 'TRUE' if domain_cols['tech'] else 'FALSE',
            'spons': 'TRUE' if domain_cols['spons'] else 'FALSE',
            'pr': 'TRUE' if domain_cols['pr'] else 'FALSE',
            'em': 'TRUE' if domain_cols['em'] else 'FALSE',
            'doc': 'TRUE' if domain_cols['doc'] else 'FALSE',
            'vigyaan': 'TRUE' if domain_cols['vigyaan'] else 'FALSE',
            'Timestamp': row['Timestamp']
        }
        
        output_data.append(output_row)
    
    output_df = pd.DataFrame(output_data)
    
    print("\n🔍 Checking for number conflicts...")
    output_df = resolve_number_conflicts(output_df)
    
    output_df = output_df.drop('Timestamp', axis=1)
    output_df = output_df[['name', 'domain', 'number', 'design', 'tech', 'spons', 'pr', 'em', 'doc', 'vigyaan']]
    
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Conversion complete! {len(output_df)} records processed.")
    print(f"\n📊 Domain breakdown:")
    print(output_df['domain'].value_counts().to_string())

def convert_exes_data(input_file, output_file):
    """Convert Google Form data for executives to Photoshop format"""
    print("\n📋 Reading input file...")
    
    df = pd.read_csv(input_file)
    print(f"✓ Found {len(df)} entries")
    
    output_data = []
    
    for idx, row in df.iterrows():
        name_full = str(row['Name On Merch:']).strip()
        domain_raw = str(row['Domain']).strip()
        
        if name_full == 'nan' or name_full == '' or domain_raw == 'nan' or domain_raw == '':
            print(f"⚠️  Skipping row {idx+2} - missing name or domain")
            continue
        
        if len(name_full) > 12:
            name = name_full.split()[0]
            print(f"📝 Shortened '{name_full}' to '{name}'")
        else:
            name = name_full
        
        domain = map_domain(domain_raw)
        domain_cols = get_domain_columns(domain)
        
        output_row = {
            'name': name,
            'domain': domain,
            'design': 'TRUE' if domain_cols['design'] else 'FALSE',
            'tech': 'TRUE' if domain_cols['tech'] else 'FALSE',
            'spons': 'TRUE' if domain_cols['spons'] else 'FALSE',
            'pr': 'TRUE' if domain_cols['pr'] else 'FALSE',
            'em': 'TRUE' if domain_cols['em'] else 'FALSE',
            'doc': 'TRUE' if domain_cols['doc'] else 'FALSE',
            'vigyaan': 'TRUE' if domain_cols['vigyaan'] else 'FALSE'
        }
        
        output_data.append(output_row)
    
    output_df = pd.DataFrame(output_data)
    
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Conversion complete! {len(output_df)} records processed.")
    print(f"\n📊 Domain breakdown:")
    print(output_df['domain'].value_counts().to_string())

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
        match = re.search(r'(XXL|XL|[SMLX])', size_clean.upper())
        if match:
            cleaned_sizes.append(match.group(1))
        elif size_clean and size_clean.isalpha() and len(size_clean) <= 3:
            cleaned_sizes.append(size_clean.upper())
    
    return cleaned_sizes

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
        
        if name == 'nan' or name == '':
            skipped += 1
            continue
        
        contact = str(row['CONTACT NUMBER']).strip()
        email = str(row.get('Email Address', row.get('E-MAIL', ''))).strip()
        residency = str(row['Choose your place of residency (FOR DISTRIBUTION PURPOSES)']).strip()
        
        orders = []
        
        # Method 1: Check legacy numerical columns
        legacy_orders = False
        aesthetics = str(row.get('Choose your aesthetics! (Offers are available at specific order quantities. For combo order select multiple options)', '')).strip()
        
        designs_list = []
        if 'Technocracy' in aesthetics:
            designs_list.append('Technocracy')
        if 'Dharma' in aesthetics:
            designs_list.append('Dharma')
        if 'Abyss' in aesthetics or 'Conquering' in aesthetics:
            designs_list.append('Abyss')
        
        if not designs_list:
            designs_list = ['Technocracy']
        
        for size_key, col_name in tshirt_cols.items():
            if col_name in df.columns:
                try:
                    quantity = int(float(row[col_name])) if pd.notna(row[col_name]) and str(row[col_name]).strip() != '' else 0
                    if quantity > 0:
                        legacy_orders = True
                        num_designs = len(designs_list)
                        
                        if quantity % num_designs == 0:
                            per_design = quantity // num_designs
                            for design in designs_list:
                                for _ in range(per_design):
                                    orders.append({'design': design, 'size': size_key})
                        else:
                            base_qty = quantity // num_designs
                            extra = quantity % num_designs
                            
                            for i, design in enumerate(designs_list):
                                design_qty = base_qty + (1 if i < extra else 0)
                                for _ in range(design_qty):
                                    orders.append({'design': design, 'size': size_key})
                except (ValueError, TypeError):
                    pass
        
        # Method 2: Check text field entries
        if not legacy_orders:
            for design, col_name in text_fields.items():
                if col_name in df.columns and col_name in row.index:
                    sizes = parse_size_entry(row[col_name])
                    for size in sizes:
                        orders.append({'design': design, 'size': size})
        
        if not orders:
            skipped += 1
            continue
        
        for order in orders:
            output_data.append({
                'name': name,
                'email': email if email != 'nan' else '',
                'contact': contact if contact != 'nan' else '',
                'residency': residency if residency != 'nan' else '',
                'design': order['design'],
                'size': order['size']
            })
    
    output_df = pd.DataFrame(output_data)
    
    if len(output_df) == 0:
        print("\n❌ No valid orders found!")
        return
    
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Conversion complete! {len(output_df)} order items from {len(output_df['name'].unique())} people ({skipped} entries skipped).")
    print(f"\n📊 Design breakdown:")
    print(output_df['design'].value_counts().to_string())

def extract_sizes(input_file, output_file, file_type='cores'):
    """Extract name, domain, and size from Google Form data"""
    print(f"\n📋 Reading {file_type} data from: {input_file}")
    
    df = pd.read_csv(input_file)
    print(f"✓ Found {len(df)} entries")
    
    output_data = []
    skipped = 0
    
    for idx, row in df.iterrows():
        name_full = str(row['Name On Merch:']).strip()
        domain_raw = str(row['Domain']).strip()
        size = str(row['Mention Your Size:']).strip()
        
        if name_full == 'nan' or name_full == '' or domain_raw == 'nan' or domain_raw == '':
            skipped += 1
            continue
        
        if len(name_full) > 12:
            name = name_full.split()[0]
        else:
            name = name_full
        
        domain = map_domain(domain_raw)
        
        if size == 'nan' or size == '':
            size = 'NOT SPECIFIED'
        
        output_data.append({
            'name': name,
            'domain': domain,
            'size': size.upper()
        })
    
    output_df = pd.DataFrame(output_data)
    
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Extraction complete! {len(output_df)} records processed ({skipped} skipped).")
    print(f"\n📊 Size breakdown:")
    print(output_df['size'].value_counts().to_string())

def generate_printing_summary(input_file, output_file):
    """Generate printing summary from VOA orders"""
    print(f"\n📋 Reading orders from: {input_file}")
    
    df = pd.read_csv(input_file)
    print(f"✓ Found {len(df)} order items")
    
    summary = df.groupby(['design', 'size']).size().reset_index(name='quantity')
    
    size_order = {'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
    summary['size_order'] = summary['size'].map(lambda x: size_order.get(x, 999))
    summary = summary.sort_values(['design', 'size_order'])
    summary = summary.drop('size_order', axis=1)
    
    print(f"\n💾 Saving to {output_file}...")
    summary.to_csv(output_file, index=False)
    
    print(f"✅ Summary complete!\n")
    print("=" * 50)
    print("PRINTING SUMMARY BY DESIGN")
    print("=" * 50)
    
    for design in summary['design'].unique():
        design_data = summary[summary['design'] == design]
        total = design_data['quantity'].sum()
        
        print(f"\n📦 {design} (Total: {total} items)")
        print("-" * 40)
        for _, row in design_data.iterrows():
            print(f"  {row['size']:6s} : {row['quantity']:3d} pcs")
    
    print("\n" + "=" * 50)
    print(f"GRAND TOTAL: {summary['quantity'].sum()} items")
    print("=" * 50)

def interactive_mode():
    """Run in interactive mode"""
    print_banner()
    
    print("Select tool:")
    print("1. Core Team Converter (with numbers)")
    print("2. Executive Team Converter (no numbers)")
    print("3. VOA Orders Converter (volunteers/public)")
    print("4. Size Extraction (distribution lists)")
    print("5. Printing Summary Generator")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice == '6':
        print("\n👋 Goodbye!")
        return
    
    if choice not in ['1', '2', '3', '4', '5']:
        print("\n❌ Invalid choice. Please run again.")
        return
    
    input_file = input("\nEnter input CSV file path: ").strip().strip('"')
    
    if not os.path.exists(input_file):
        print(f"\n❌ Error: File '{input_file}' not found!")
        return
    
    # Set default output based on choice
    default_outputs = {
        '1': 'cores_photoshop.csv',
        '2': 'exes_photoshop.csv',
        '3': 'voa_orders.csv',
        '4': 'sizes.csv',
        '5': 'printing_summary.csv'
    }
    
    default_output = default_outputs[choice]
    output_file = input(f"Enter output CSV file path (press Enter for '{default_output}'): ").strip().strip('"')
    
    if not output_file:
        output_file = default_output
    
    try:
        if choice == '1':
            convert_cores_data(input_file, output_file)
        elif choice == '2':
            convert_exes_data(input_file, output_file)
        elif choice == '3':
            convert_voa_data(input_file, output_file)
        elif choice == '4':
            file_type = input("Is this for cores or exes? (cores/exes): ").strip().lower()
            if file_type not in ['cores', 'exes']:
                print("Invalid type. Using 'cores'")
                file_type = 'cores'
            extract_sizes(input_file, output_file, file_type)
        elif choice == '5':
            generate_printing_summary(input_file, output_file)
        
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
        command = sys.argv[1]
        
        if command == 'cores':
            if len(sys.argv) < 3:
                print("Usage: tshirt_converter cores <input_file> [output_file]")
                sys.exit(1)
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else "cores_photoshop.csv"
            convert_cores_data(input_file, output_file)
            
        elif command == 'exes':
            if len(sys.argv) < 3:
                print("Usage: tshirt_converter exes <input_file> [output_file]")
                sys.exit(1)
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else "exes_photoshop.csv"
            convert_exes_data(input_file, output_file)
            
        elif command == 'voa':
            if len(sys.argv) < 3:
                print("Usage: tshirt_converter voa <input_file> [output_file]")
                sys.exit(1)
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else "voa_orders.csv"
            convert_voa_data(input_file, output_file)
            
        elif command == 'sizes':
            if len(sys.argv) < 4:
                print("Usage: tshirt_converter sizes <cores|exes> <input_file> [output_file]")
                sys.exit(1)
            file_type = sys.argv[2]
            input_file = sys.argv[3]
            output_file = sys.argv[4] if len(sys.argv) > 4 else "sizes.csv"
            extract_sizes(input_file, output_file, file_type)
            
        elif command == 'summary':
            if len(sys.argv) < 3:
                print("Usage: tshirt_converter summary <input_file> [output_file]")
                sys.exit(1)
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else "printing_summary.csv"
            generate_printing_summary(input_file, output_file)
            
        else:
            print("Unknown command. Use: cores, exes, voa, sizes, or summary")
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()
