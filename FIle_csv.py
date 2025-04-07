import os
import csv

root_dir = r'/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/Train+Val' 
output_csv = '/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/Train+Val/lesion_dataset.csv'
lesion_classes = [
    'angioectasia', 'bleeding', 'erosion', 'erythema', 'foreign_body',
    'lymphangiectasia', 'normal', 'polyp', 'ulcers', 'worms'
]

rows = []
header = ['image_path', 'Dataset'] + lesion_classes

# Sanity check: is root directory valid?
if not os.path.isdir(root_dir):
    raise FileNotFoundError(f"Root directory not found: {root_dir}")

# Walk through class folders
for lesion in lesion_classes:
    lesion_path = os.path.join(root_dir, lesion)
    if not os.path.isdir(lesion_path):
        print(f"Skipping missing lesion folder: {lesion_path}")
        continue
    
    # Inside lesion folder, e.g., KID or seeai
    for dataset_source in os.listdir(lesion_path):
        source_path = os.path.join(lesion_path, dataset_source)
        if not os.path.isdir(source_path):
            print(f"Skipping non-folder: {source_path}")
            continue
        
        for img in os.listdir(source_path):
            if img.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root_dir, lesion, dataset_source, img).replace('/', '\\')
                dataset = dataset_source
                one_hot = [1 if cls == lesion else 0 for cls in lesion_classes]
                row = [image_path, dataset] + one_hot
                rows.append(row)
            else:
                print(f"Skipping non-image file: {img}")

with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(header)
    writer.writerows(rows)

print(f"CSV saved as {output_csv} with {len(rows)} image entries.")
