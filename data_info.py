# This script processes a CSV file containing dataset information and generates a summary CSV file
import pandas as pd

# Load the CSV
df = pd.read_csv("/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/updated_train_val.csv")

# Normalize the class labels
df['original_class'] = df['original_class'].str.strip().str.lower()

# Define relevant class columns
ordered_columns = ["erosion", "normal", "ulcers"]

# Group by dataset and original_class
grouped = df.groupby(['dataset', 'original_class']).size().unstack(fill_value=0)

# Add missing columns with 0
for col in ordered_columns:
    if col not in grouped.columns:
        grouped[col] = 0

# Keep only the ordered columns
grouped = grouped[ordered_columns]

# Add Total Images column (sum across rows)
grouped["Total Images"] = grouped.sum(axis=1)

# Add Total Images row (sum across columns)
grouped.loc["Total Images"] = grouped.sum()

# Save to CSV
output_path = "dataset_distribution_from_uploaded.csv"
grouped.to_csv(output_path)

print(f"Saved to {output_path}")
