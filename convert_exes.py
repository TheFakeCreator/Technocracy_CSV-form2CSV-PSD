import pandas as pd
import sys

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

def convert_exes_data(input_file, output_file):
    """Convert Google Form data for executives to Photoshop format"""
    print("📋 Reading input file...")
    
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    print(f"✓ Found {len(df)} entries")
    
    # Create output dataframe
    output_data = []
    
    for idx, row in df.iterrows():
        # Extract name and domain
        name_full = str(row['Name On Merch:']).strip()
        domain_raw = str(row['Domain']).strip()
        
        # Skip rows with missing critical data
        if name_full == 'nan' or name_full == '' or domain_raw == 'nan' or domain_raw == '':
            print(f"⚠️  Skipping row {idx+2} - missing name or domain")
            continue
        
        # Extract first name only if name is too long (more than 12 characters)
        if len(name_full) > 12:
            name = name_full.split()[0]
            print(f"📝 Shortened '{name_full}' to '{name}'")
        else:
            name = name_full
        
        domain = map_domain(domain_raw)
        
        # Get domain columns
        domain_cols = get_domain_columns(domain)
        
        # Create row (no number column for exes)
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
    
    # Create DataFrame
    output_df = pd.DataFrame(output_data)
    
    # Save to CSV
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Conversion complete! {len(output_df)} records processed.")
    print(f"\n📊 Domain breakdown:")
    print(output_df['domain'].value_counts())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_exes.py <input_file.csv> [output_file.csv]")
        print("\nExample: python convert_exes.py form_data_exes.csv output_exes.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "exes_photoshop.csv"
    
    try:
        convert_exes_data(input_file, output_file)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
