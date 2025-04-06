import pandas as pd
import os
import shutil

csv_path = "/home/endodl/PHASE-1/mln/lesions_cv24/SEE-AI/all_annotation.csv"  
images_dir = "/home/endodl/PHASE-1/mln/lesions_cv24/SEE-AI/SEE_AI_project_all_images"         
output_dir = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/seeai_sorted"   
normal_folder = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/seeai_sorted/normal"    

df = pd.read_csv(csv_path, skiprows=2)  
df.fillna(0, inplace=True)
df.columns = ['index', 'image_number', 'angiodysplasia', 'erosion', 'stenosis',
              'lymphangiectasia', 'lymph_follicle', 'SMT', 'polyp-like', 'bleeding',
              'diverticulum', 'erythema', 'foreign_body', 'vein', 'annotation_number']              
class_names = df.columns[2:-1]
df = df.iloc[:-1]                         

for cls in class_names:
    os.makedirs(os.path.join(output_dir, cls), exist_ok=True)

missing_images = 0
copied_images = 0
normal_images = 0

# Iterate through rows
for _, row in df.iterrows():
    img_number = int(row["image_number"])
    img_filename = f"image{img_number:05d}.jpg"
    src_path = os.path.join(images_dir, img_filename)

    if not os.path.exists(src_path):
        print(f"⚠️ Warning: Image not found -> {src_path}")
        missing_images += 1
        continue

    # Check for class presence
    has_class = False
    for cls in class_names:
        if int(row[cls]) > 0:
            dst_path = os.path.join(output_dir, cls, img_filename)
            shutil.copy2(src_path, dst_path)
            has_class = True

    # If no class, move to 'normal'
    if not has_class:
        dst_path = os.path.join(output_dir, normal_folder, img_filename)
        shutil.copy2(src_path, dst_path)
        normal_images += 1

    copied_images += 1
    
print(f"Done organizing.")
print(f"Total images processed: {copied_images}")
print(f"Moved to 'normal': {normal_images}")
print(f"Missing images: {missing_images}")