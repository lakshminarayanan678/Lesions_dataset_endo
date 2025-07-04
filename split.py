import os
import shutil
import random
from pathlib import Path

random.seed(42)  # Reproducibility

# Input and output directories
source_dir = Path("/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1/capsulevision/data/testing")
output_base = Path("/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data1/capsulevision/data/testing_split")

# Define split ratios
split_ratios = {
    "training": 0.7,
    "validation": 0.15,
    "testing": 0.15,
}

# Lesion class folders to process
lesion_classes = ["Erosion", "Normal", "Ulcers"]

def split_images():
    for lesion in lesion_classes:
        class_path = source_dir / lesion
        if not class_path.exists():
            print(f"[WARNING] Missing folder: {class_path}")
            continue

        images = list(class_path.glob("*"))
        images = [img for img in images if img.is_file()]
        random.shuffle(images)

        n_total = len(images)
        n_train = int(n_total * split_ratios["training"])
        n_val = int(n_total * split_ratios["validation"])
        n_test = n_total - n_train - n_val

        split_map = {
            "training": images[:n_train],
            "validation": images[n_train:n_train + n_val],
            "testing": images[n_train + n_val:],
        }

        for split, imgs in split_map.items():
            out_dir = output_base / split / lesion
            out_dir.mkdir(parents=True, exist_ok=True)
            for img_path in imgs:
                shutil.copy(img_path, out_dir / img_path.name)

        print(f"[INFO] {lesion}: Total={n_total}, Train={n_train}, Val={n_val}, Test={n_test}")

def main():
    print("[INFO] Splitting testing/ dataset into 70-15-15...")
    split_images()
    print(f"[SUCCESS] Output saved at: {output_base}")

if __name__ == "__main__":
    main()
