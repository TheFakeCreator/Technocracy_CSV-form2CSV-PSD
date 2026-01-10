import pandas as pd
import random
import sys
import os

def print_banner():
    """Print application banner"""
    print("\n" + "="*60)
    print("  AAVARTAN T-Shirt Design Data Converter")
    print("  Convert Google Form data to Photoshop format")
    print("="*60 + "\n")

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

def interactive_mode():
    """Run in interactive mode"""
    print_banner()
    
    print("Select conversion type:")
    print("1. Cores (with number field)")
    print("2. Executives (no number field)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '3':
        print("\n👋 Goodbye!")
        return
    
    if choice not in ['1', '2']:
        print("\n❌ Invalid choice. Please run again.")
        return
    
    input_file = input("\nEnter input CSV file path: ").strip().strip('"')
    
    if not os.path.exists(input_file):
        print(f"\n❌ Error: File '{input_file}' not found!")
        return
    
    default_output = "cores_photoshop.csv" if choice == '1' else "exes_photoshop.csv"
    output_file = input(f"Enter output CSV file path (press Enter for '{default_output}'): ").strip().strip('"')
    
    if not output_file:
        output_file = default_output
    
    try:
        if choice == '1':
            convert_cores_data(input_file, output_file)
        else:
            convert_exes_data(input_file, output_file)
        
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
        if sys.argv[1] == 'cores':
            if len(sys.argv) < 3:
                print("Usage: tshirt_converter cores <input_file> [output_file]")
                sys.exit(1)
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else "cores_photoshop.csv"
            convert_cores_data(input_file, output_file)
        elif sys.argv[1] == 'exes':
            if len(sys.argv) < 3:
                print("Usage: tshirt_converter exes <input_file> [output_file]")
                sys.exit(1)
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else "exes_photoshop.csv"
            convert_exes_data(input_file, output_file)
        else:
            print("Unknown command. Use 'cores' or 'exes'")
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()
