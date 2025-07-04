import os
import pandas as pd

base_dir = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1/split_data_eva02"
output_csv = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1/split_data_eva02/train_val.csv"

data = []

for split in ['training', 'validation']:
    fold = 1 if split == 'training' else 0
    split_path = os.path.join(base_dir, split)

    for class_name in ['Erosion', 'Normal', 'Ulcers']:
        class_path = os.path.join(split_path, class_name)
        if not os.path.exists(class_path):
            continue

        for dataset_name in os.listdir(class_path):
            dataset_path = os.path.join(class_path, dataset_name)
            if not os.path.isdir(dataset_path):
                continue

            for img_file in os.listdir(dataset_path):
                if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    img_full_path = os.path.join(dataset_path, img_file)
                    data.append({
                        'dataset': '',  # empty as requested
                        'patient_id': '',  # empty as requested
                        'frame_path': img_full_path,
                        'proposed_name': img_file,
                        'class': class_name,
                        'fold': fold,
                        'original_class': class_name
                    })

df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)
print(f"CSV saved to: {output_csv}")
