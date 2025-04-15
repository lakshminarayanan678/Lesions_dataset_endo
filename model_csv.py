import pandas as pd
import os

# Load the original lesion CSV with tab separation
df_input = pd.read_csv("/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/Train+Val/lesion_dataset_with_split.csv", sep="\t")

# Create the new DataFrame
df_converted = pd.DataFrame()

# Copy frame_path and dataset
df_converted["frame_path"] = df_input["image_path"]
df_converted["dataset"] = df_input["dataset"]

# Define all lesion types
lesion_types = [
    "angioectasia", "bleeding", "erosion", "erythema", "foreign_body",
    "lymphangiectasia", "normal", "polyp", "ulcers", "worms"
]

# Extract lesion type from image path
df_converted["original_class"] = df_input["image_path"].apply(
    lambda x: next((cls for cls in lesion_types if cls in x.lower()), "unknown")
)

# Extract just the image filename
df_converted["proposed_name"] = df_input["image_path"].apply(lambda x: os.path.basename(x))

# Map split to fold
df_converted["fold"] = df_input["split"].apply(lambda x: 1 if x.lower() == "train" else 0)

# Add empty columns for patient_id and class
df_converted["patient_id"] = ""
df_converted["class"] = ""

# Reorder columns
column_order = ["dataset", "patient_id", "frame_path", "proposed_name", "class", "fold", "original_class"]
df_converted = df_converted[column_order]

# Save to a new CSV
df_converted.to_csv("converted_train_val.csv", index=False, sep="\t")
