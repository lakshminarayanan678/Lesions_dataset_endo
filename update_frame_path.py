import pandas as pd
import os

# === CONFIGURATION ===
input_file = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1/capsulevision/train_val.csv"  # Change this as needed
new_base = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1"       # This will be prepended before 'capsulevision/...'

# === Load CSV or Excel file ===
file_ext = os.path.splitext(input_file)[-1].lower()
if file_ext == ".csv":
    df = pd.read_csv(input_file)
elif file_ext in [".xls", ".xlsx"]:
    df = pd.read_excel(input_file)
else:
    raise ValueError("Unsupported file type: must be .csv or .xlsx")

# === Define path-updating function ===
def update_path(path):
    if isinstance(path, str) and 'capsulevision/' in path:
        relative_path = path.split('capsulevision/', 1)[1]
        return os.path.join(new_base.rstrip('/'), 'capsulevision', relative_path)
    return path  # fallback if no 'capsulevision/' found

# === Apply update to columns ===
df['frame_path'] = df['frame_path'].apply(update_path)
df['proposed_name'] = df['proposed_name'].apply(update_path)

# === Output file path ===
output_file = f"updated_{os.path.basename(input_file)}"

# === Save to new CSV or Excel ===
if file_ext == ".csv":
    df.to_csv(output_file, index=False)
else:
    df.to_excel(output_file, index=False)

# === Done ===
print(f"Updated {len(df)} rows.")
print(f"New file saved as: {output_file}")
