'''
This script converts the custom csv file (tab seprated) to the expected csv file (comma separated),
as per the CE24 Challenge dataset.
'''

import pandas as pd

# Paths
csv_model_expected = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/codes/capsule_vision_challenge_2024/datasets/ce24/train_val.csv"
csv_your_data = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data/capsulevision/train_val.csv"  

# Load both CSVs
df_expected = pd.read_csv(csv_model_expected)
df_custom = pd.read_csv(csv_your_data)

# Get column structure from expected CSV
expected_columns = df_expected.columns.tolist()

# Create a new DataFrame with expected columns
# Fill in with values from your custom CSV if the column exists, else keep NaN
df_aligned = pd.DataFrame(columns=expected_columns)

for col in expected_columns:
    if col in df_custom.columns:
        df_aligned[col] = df_custom[col]
    else:
        df_aligned[col] = pd.NA  # Fill missing columns with NaN (or some default if needed)

# Save the aligned CSV
output_path = "/mnt/data/aligned_train_val.csv"
df_aligned.to_csv(output_path, index=False)

print(f"Aligned CSV saved to: {output_path}")
