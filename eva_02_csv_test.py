import os
import pandas as pd

# ✅ Update this path to your actual testing folder
testing_dir = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1/split_data_eva02/testing/Images"
output_csv = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1/split_data_eva02/test.csv"

data = []

for img_file in os.listdir(testing_dir):
    if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        full_path = os.path.join(testing_dir, img_file)
        data.append({
            'dataset': '',
            'patient_id': '',
            'frame_path': full_path,
            'proposed_name': img_file,
            'class': '',
            'fold': -1,
            'original_class': ''
        })

df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)
print(f"Testing CSV saved to: {output_csv}")
