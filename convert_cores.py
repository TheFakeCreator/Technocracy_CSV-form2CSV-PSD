import pandas as pd
import random
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

def resolve_number_conflicts(df):
    """Resolve conflicts when multiple people choose the same number"""
    # Sort by timestamp to determine who filled first
    df = df.sort_values('Timestamp')
    
    used_numbers = set()
    final_numbers = []
    
    for idx, row in df.iterrows():
        requested_number = row['number']
        
        if requested_number not in used_numbers:
            # Number is available, assign it
            final_numbers.append(requested_number)
            used_numbers.add(requested_number)
        else:
            # Number conflict - assign a random number
            available_numbers = set(range(1, 100)) - used_numbers
            new_number = random.choice(list(available_numbers))
            final_numbers.append(new_number)
            used_numbers.add(new_number)
            print(f"⚠️  Conflict: {row['name']} requested #{requested_number} but it was taken. Assigned #{new_number}")
    
    df['number'] = final_numbers
    return df

def convert_cores_data(input_file, output_file):
    """Convert Google Form data for cores to Photoshop format"""
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
        
        # Get number (handle various formats)
        try:
            number = int(float(row['Number on Merch (0 to 99)']))
        except:
            number = random.randint(1, 99)
            print(f"⚠️  Invalid number for {name}, assigned random: {number}")
        
        # Get domain columns
        domain_cols = get_domain_columns(domain)
        
        # Create row
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
    
    # Create DataFrame
    output_df = pd.DataFrame(output_data)
    
    # Resolve number conflicts
    print("\n🔍 Checking for number conflicts...")
    output_df = resolve_number_conflicts(output_df)
    
    # Remove timestamp column (was only used for sorting)
    output_df = output_df.drop('Timestamp', axis=1)
    
    # Reorder columns to match required format
    output_df = output_df[['name', 'domain', 'number', 'design', 'tech', 'spons', 'pr', 'em', 'doc', 'vigyaan']]
    
    # Save to CSV
    print(f"\n💾 Saving to {output_file}...")
    output_df.to_csv(output_file, index=False)
    
    print(f"✅ Conversion complete! {len(output_df)} records processed.")
    print(f"\n📊 Domain breakdown:")
    print(output_df['domain'].value_counts())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_cores.py <input_file.csv> [output_file.csv]")
        print("\nExample: python convert_cores.py form_data.csv output.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "cores_photoshop.csv"
    
    try:
        convert_cores_data(input_file, output_file)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
