#!/usr/bin/env python3
import json
import glob

# Fix all notebooks
notebook_files = glob.glob('notebooks/*.ipynb')

for notebook_file in notebook_files:
    print(f"Fixing {notebook_file}...")

    with open(notebook_file, 'r') as f:
        nb = json.load(f)

    # Fix each cell
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            # Add outputs if missing
            if 'outputs' not in cell:
                cell['outputs'] = []
            # Add execution_count if missing
            if 'execution_count' not in cell:
                cell['execution_count'] = None

    # Write back
    with open(notebook_file, 'w') as f:
        json.dump(nb, f, indent=1)

    print(f"  ✓ Fixed {notebook_file}")

print("\nAll notebooks fixed!")
