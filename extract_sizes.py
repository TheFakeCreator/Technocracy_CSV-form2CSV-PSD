import pandas as pd
import sys
import os

def print_banner():
    """Print application banner"""
    print("\n" + "="*60)
    print("  Size Extraction Tool - AAVARTAN")
    print("  Extract name, domain, and size for distribution")
    print("="*60 + "\n")

def map_domain(domain):
    """Map domain names from Google Form to standard format"""
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

def extract_size_data(input_file, output_file, file_type='cores'):
    """Extract name, domain, and size from Google Form data"""
    print(f"\n📋 Reading {file_type} data from: {input_file}")
    
    # Read the CSV file
    df = pd.read_csv(input_file)
    print(f"✓ Found {len(df)} entries")
    
    output_data = []
    skipped = 0
    
    for idx, row in df.iterrows():
        # Extract fields
        name_full = str(row['Name On Merch:']).strip()
        domain_raw = str(row['Domain']).strip()
        size = str(row['Mention Your Size:']).strip()
        
        # Skip rows with missing critical data
        if name_full == 'nan' or name_full == '' or domain_raw == 'nan' or domain_raw == '':
            print(f"⚠️  Skipping row {idx+2} - missing name or domain")
            skipped += 1
            continue
        
        # Shorten name if too long
        if len(name_full) > 12:
            name = name_full.split()[0]
        else:
            name = name_full
        
        domain = map_domain(domain_raw)
        
        # Handle invalid size
        if size == 'nan' or size == '':
            size = 'NOT SPECIFIED'
            print(f"⚠️  {name}: Size not specified")
        
        # Create output row
        output_row = {
            'name': name,
            'domain': domain,
            'size': size.upper()
        }
        
        output_data.append(output_row)
    
    # Create DataFrame
    output_df = pd.DataFrame(output_data)
    
    # Save to CSV
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Extraction complete! {len(output_df)} records processed ({skipped} skipped).")
    
    # Show size breakdown
    print(f"\n📊 Size breakdown:")
    print(output_df['size'].value_counts().to_string())
    
    print(f"\n📊 Domain breakdown:")
    print(output_df['domain'].value_counts().to_string())

def interactive_mode():
    """Run in interactive mode"""
    print_banner()
    
    print("Select file type:")
    print("1. Cores")
    print("2. Executives")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '3':
        print("\n👋 Goodbye!")
        return
    
    if choice not in ['1', '2']:
        print("\n❌ Invalid choice. Please run again.")
        return
    
    file_type = 'cores' if choice == '1' else 'exes'
    
    input_file = input(f"\nEnter input CSV file path (e.g., {file_type}1.csv): ").strip().strip('"')
    
    if not os.path.exists(input_file):
        print(f"\n❌ Error: File '{input_file}' not found!")
        return
    
    default_output = f"{file_type}_sizes.csv"
    output_file = input(f"Enter output CSV file path (press Enter for '{default_output}'): ").strip().strip('"')
    
    if not output_file:
        output_file = default_output
    
    try:
        extract_size_data(input_file, output_file, file_type)
        print(f"\n✨ Output saved to: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"\n❌ Error during extraction: {e}")
        import traceback
        traceback.print_exc()
    
    input("\nPress Enter to exit...")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Command-line mode
        if sys.argv[1] in ['cores', 'exes']:
            if len(sys.argv) < 3:
                print(f"Usage: python extract_sizes.py {sys.argv[1]} <input_file> [output_file]")
                sys.exit(1)
            
            file_type = sys.argv[1]
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else f"{file_type}_sizes.csv"
            
            extract_size_data(input_file, output_file, file_type)
        else:
            print("Unknown command. Use 'cores' or 'exes'")
            print("\nExamples:")
            print("  python extract_sizes.py cores cores1.csv cores_sizes.csv")
            print("  python extract_sizes.py exes exes1.csv exes_sizes.csv")
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()

if __name__ == "__main__":
    main()
