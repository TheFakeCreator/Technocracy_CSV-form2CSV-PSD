import pandas as pd
import sys
import os

def print_banner():
    """Print application banner"""
    print("\n" + "="*60)
    print("  Printing Summary Generator - AAVARTAN")
    print("  Generate size counts for each design")
    print("="*60 + "\n")

def generate_printing_summary(input_file, output_file):
    """Generate printing summary from VOA orders"""
    print(f"\n📋 Reading orders from: {input_file}")
    
    # Read the orders file
    df = pd.read_csv(input_file)
    print(f"✓ Found {len(df)} order items")
    
    # Group by design and size, count occurrences
    summary = df.groupby(['design', 'size']).size().reset_index(name='quantity')
    
    # Sort by design and size
    size_order = {'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
    summary['size_order'] = summary['size'].map(lambda x: size_order.get(x, 999))
    summary = summary.sort_values(['design', 'size_order'])
    summary = summary.drop('size_order', axis=1)
    
    # Save to CSV
    print(f"\n💾 Saving to {output_file}...")
    summary.to_csv(output_file, index=False)
    
    print(f"✅ Summary complete!\n")
    
    # Display the summary
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
    
    # Show breakdown by size across all designs
    print("\n📊 Size breakdown (all designs):")
    size_totals = summary.groupby('size')['quantity'].sum().sort_index()
    for size, count in size_totals.items():
        print(f"  {size:6s} : {count:3d} pcs")

def interactive_mode():
    """Run in interactive mode"""
    print_banner()
    
    input_file = input("Enter VOA orders CSV file path (e.g., voa_orders.csv): ").strip().strip('"')
    
    if not os.path.exists(input_file):
        print(f"\n❌ Error: File '{input_file}' not found!")
        return
    
    default_output = "printing_summary.csv"
    output_file = input(f"Enter output CSV file path (press Enter for '{default_output}'): ").strip().strip('"')
    
    if not output_file:
        output_file = default_output
    
    try:
        generate_printing_summary(input_file, output_file)
        print(f"\n✨ Output saved to: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"\n❌ Error during generation: {e}")
        import traceback
        traceback.print_exc()
    
    input("\nPress Enter to exit...")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Command-line mode
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "printing_summary.csv"
        
        try:
            generate_printing_summary(input_file, output_file)
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
