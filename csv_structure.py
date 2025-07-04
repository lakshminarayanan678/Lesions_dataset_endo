import pandas as pd

# Load the second CSV using tab as separator (since it looks like tab-delimited)
df_custom = pd.read_csv("/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data/capsulevision/converted_train_val.csv", sep="\t", engine='python')

# Strip leading/trailing whitespaces from column names
df_custom.columns = [col.strip() for col in df_custom.columns]

# Ensure columns are in the correct order as expected by the model
expected_columns = [
    "dataset", "patient_id", "frame_path", "proposed_name", "class", "fold", "original_class"
]

# Reorder and fill missing columns if necessary
for col in expected_columns:
    if col not in df_custom.columns:
        df_custom[col] = ""

df_custom = df_custom[expected_columns]

# Save the new aligned CSV with comma as separator
output_path = "/home/endodl/PHASE-1/mln/lesions_cv24/lesions_cv24.csv"
df_custom.to_csv(output_path, index=False)

print(f"Cleaned and aligned CSV saved to: {output_path}")
