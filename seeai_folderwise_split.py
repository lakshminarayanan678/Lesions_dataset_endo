import pandas as pd
import os
import shutil

csv_path = "/home/endodl/PHASE-1/mln/lesions_cv24/SEE-AI/all_annotation.csv"  
images_dir = "path/to/your/images"         
output_dir = "path/to/output/folder"       

df = pd.read_csv(csv_path, skiprows=2)  
df.fillna(0, inplace=True)              

class_names = df.columns[2:-1]

for cls in class_names:
    os.makedirs(os.path.join(output_dir, cls), exist_ok=True)

# Iterate over each row in the dataframe
for _, row in df.iterrows():
    try:
        img_number = int(row['image_number'])
    except ValueError:
        continue

    img_filename = f"{img_number}.jpg"
    src_path = os.path.join(images_dir, img_filename)

    for cls in class_names:
        try:
            if int(row[cls]) > 0:
                dst_path = os.path.join(output_dir, cls, img_filename)
                if os.path.exists(src_path):
                    shutil.copy2(src_path, dst_path)
                else:
                    print(f"⚠️ Warning: Image not found -> {src_path}")
        except ValueError:
            continue  

print("All images organized successfully")
