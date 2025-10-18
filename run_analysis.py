#!/usr/bin/env python3
"""
LEGO Analysis Project Launcher
Run this script to execute the complete LEGO dataset analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    print("=" * 60)
    print("🧱 LEGO DATASET ANALYSIS PROJECT")
    print("=" * 60)
    
    # Check if data files exist
    data_files = ['data/colors.csv', 'data/sets.csv', 'data/themes.csv']
    for file in data_files:
        if not os.path.exists(file):
            print(f"❌ Error: {file} not found!")
            return
    
    print("✅ All data files found!")
    print("\n📊 Loading datasets...")
    
    # Load datasets
    colors = pd.read_csv('data/colors.csv')
    sets = pd.read_csv('data/sets.csv')
    themes = pd.read_csv('data/themes.csv')
    
    print(f"   • Colors: {len(colors)} rows")
    print(f"   • Sets: {len(sets)} rows") 
    print(f"   • Themes: {len(themes)} rows")
    
    print("\n🎨 LEGO COLORS ANALYSIS")
    print("-" * 30)
    print(f"Total unique colors: {colors['name'].nunique()}")
    print("Transparency breakdown:")
    transparency_counts = colors['is_trans'].value_counts()
    print(f"   • Opaque colors: {transparency_counts.get('f', 0)}")
    print(f"   • Transparent colors: {transparency_counts.get('t', 0)}")
    
    print("\n🏗️ LEGO SETS ANALYSIS")
    print("-" * 30)
    
    # First LEGO sets
    first_year = sets['year'].min()
    first_sets = sets[sets['year'] == first_year]
    print(f"First LEGO sets released in: {first_year}")
    print(f"Number of sets in first year: {len(first_sets)}")
    
    # Largest sets
    print("\nTop 5 largest LEGO sets:")
    largest_sets = sets.nlargest(5, 'num_parts')[['name', 'year', 'num_parts']]
    for idx, row in largest_sets.iterrows():
        print(f"   • {row['name']} ({row['year']}): {row['num_parts']} parts")
    
    # Sets by year analysis
    sets_by_year = sets.groupby('year').size()
    print(f"\nSets released in 1955: {sets_by_year.get(1955, 0)}")
    print(f"Sets released in 2019: {sets_by_year.get(2019, 0)}")
    
    print("\n📈 GROWTH ANALYSIS")
    print("-" * 30)
    growth_ratio = sets_by_year.get(2019, 0) / max(sets_by_year.get(1955, 1), 1)
    print(f"LEGO has grown {growth_ratio:.1f}x from 1955 to 2019!")
    
    print("\n🎯 ANALYSIS COMPLETE!")
    print("=" * 60)
    print("💡 To run the full interactive analysis:")
    print("   1. Run: python -m jupyter notebook")
    print("   2. Open: Lego_Analysis_for_Course.ipynb")
    print("   3. Click: Cell → Run All")
    print("=" * 60)

if __name__ == "__main__":
    main()