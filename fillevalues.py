import pandas as pd

# Load the CSV file
csv_path = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data/capsulevision/train_val.csv"
df = pd.read_csv(csv_path)

# Fill missing values in 'class' and 'patient_id' with the value from 'original_class' of the same row
df["class"] = df["class"].fillna(df["original_class"])
df["patient_id"] = df["patient_id"].fillna(df["original_class"])

# Save the updated CSV
output_path = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data/capsulevision/new_train_val.csv"
df.to_csv(output_path, index=False)

print(f"✅ Missing values filled from 'original_class' and saved to: {output_path}")
