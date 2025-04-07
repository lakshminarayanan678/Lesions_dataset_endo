import os
import shutil
import pandas as pd
from pathlib import Path

csv_path = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/Train+Val/lesion_dataset_with_split.csv"
base_output_dir = "/home/endodl/PHASE-1/mln/lesions_cv24/data/capsulevision"
missing_log_path = "missing_files.txt"

df = pd.read_csv(csv_path, sep="\t")

df.columns = df.columns.str.strip().str.lower()

image_col = "image_path"
split_col = "split"
dataset_col = "dataset"
non_lesion_cols = ['image_path', 'dataset', 'split']
lesion_cols = [col for col in df.columns if col not in non_lesion_cols]

missing_log = open(missing_log_path, "w")
missing_count = 0
copied_count = 0

for idx, row in df.iterrows():
    img_path = row[image_col].replace("\\", "/")
    img_path_obj = Path(img_path)
    
    lesion_classes = [col for col in lesion_cols if row[col] == 1]
    if not lesion_classes:
        continue
    lesion_class = lesion_classes[0].capitalize() 

    dataset = row[dataset_col]
    split = row[split_col].lower()
    

    dest_dir = os.path.join(base_output_dir, f"{split}ing", lesion_class, dataset)
    os.makedirs(dest_dir, exist_ok=True)

    if img_path_obj.exists():
        try:
            shutil.copy(str(img_path_obj), dest_dir)
            copied_count += 1
        except Exception as e:
            print(f"Failed to copy {img_path} → {dest_dir}: {e}")
            missing_log.write(f"{img_path}  # Copy error: {e}\n")
            missing_count += 1
    else:
        print(f"Missing: {img_path}")
        missing_log.write(f"{img_path}  # File not found\n")
        missing_count += 1

missing_log.close()

print(f"\n Done! {copied_count} images copied.")
print(f"{missing_count} missing or failed. See `{missing_log_path}`.")