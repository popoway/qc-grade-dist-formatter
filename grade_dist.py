# Copyright 2025 Ming Lei (popoway).
# Licensed under the MIT License (see LICENSE).

import pandas as pd
import argparse
import warnings

# Suppress openpyxl warning caused by Excel files exported from PeopleSoft
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Argument parser
parser = argparse.ArgumentParser(description="Generate grade summary by instructor and section.")
parser.add_argument('--grade', required=True, help='Path to the Excel file with grade records')
parser.add_argument('--term', required=True, help='Academic term label, e.g., SP24')
parser.add_argument('--details', required=True, help='Path to class details Excel file')
args = parser.parse_args()

# Load files
grades_df = pd.read_excel(args.grade, skiprows=1)
details_df = pd.read_excel(args.details, skiprows=1)

# Clean column names
grades_df.columns = [col.strip() for col in grades_df.columns]
details_df.columns = [col.strip() for col in details_df.columns]

# Normalize fields
grades_df['Grade'] = grades_df['Grade'].astype(str).str.strip().str.upper()
grades_df['Subject'] = grades_df['Subject'].astype(str).str.strip()
grades_df['Catalog'] = grades_df['Catalog'].astype(str).str.strip()
grades_df['Class Nbr'] = grades_df['Class Nbr'].astype(str).str.strip()

details_df['Catalog#'] = details_df['Catalog#'].astype(str).str.strip()
details_df['Class#'] = details_df['Class#'].astype(str).str.strip()
details_df['Section'] = details_df['Section'].astype(str).str.strip()
details_df['Class Title'] = details_df['Class Title'].astype(str).str.strip()

# Instructor normalization
def normalize_instructor(name):
    parts = str(name).split(',')
    if len(parts) == 2:
        last = parts[0].strip().upper()
        first_initial = parts[1].strip()[0].upper() if parts[1].strip() else ''
        return f"{last}, {first_initial}"
    return name.strip().upper()

grades_df['Instructor'] = grades_df['Instructor'].apply(normalize_instructor)

# Map original grades to aggregated categories
grade_map = {
    'A+': 'A+',
    'A': 'A',
    'A-': 'A-',
    'B+': 'B+',
    'B': 'B',
    'B-': 'B-',
    'C+': 'C+',
    'C': 'C',
    'C-': 'C-',
    'D+': 'D+',
    'D': 'D',
    'F': 'F',
    'NC': 'F',
    'W': 'W',
    'WD': 'W',
    'WN': 'W',
    'WU': 'W',
    'INC': 'INC/NA',
    'PEN': 'INC/NA'
}

grades_df['Grade'] = grades_df['Grade'].map(grade_map)

# Remove rows with grades not in map (if any were unmapped)
grades_df = grades_df.dropna(subset=['Grade'])

# Define final expected grade categories
final_grades = [
    'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-',
    'D+', 'D', 'F', 'W', 'INC/NA'
]

# Pivot table with new aggregated grades
pivot = grades_df.pivot_table(
    index=['Subject', 'Catalog', 'Class Nbr', 'Instructor'],
    columns='Grade',
    aggfunc='size',
    fill_value=0
).reset_index()

# Ensure all grade columns exist
for grade in final_grades:
    if grade not in pivot.columns:
        pivot[grade] = 0

# Add TOTAL and TERM
pivot['TOTAL'] = pivot[final_grades].sum(axis=1)
pivot['TERM'] = args.term

# Merge in Section and Course Name
merged = pivot.merge(
    details_df[['Class#', 'Section', 'Class Title']],
    left_on='Class Nbr',
    right_on='Class#',
    how='left'
)

# Final column order
final_columns = ['TERM', 'Subject', 'Catalog', 'Class Title', 'Section', 'Instructor', 'TOTAL'] + final_grades
merged = merged[final_columns]
merged.columns = ['TERM', 'SUBJECT', 'NBR', 'COURSE NAME', 'SECTION', 'PROF', 'TOTAL'] + final_grades

# Export to Excel
output_file = f"grade_summary_{args.term}.xlsx"
merged.to_excel(output_file, index=False)

# Print summary
print(f"✅ Exported {len(merged)} rows to: {output_file}")