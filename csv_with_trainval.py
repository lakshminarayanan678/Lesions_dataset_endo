import pandas as pd
from sklearn.model_selection import train_test_split

csv_path = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/Train+Val/lesion_dataset.csv"
df = pd.read_csv(csv_path, sep='\t')

df.columns = df.columns.str.strip().str.lower()

required_columns = {'image_path', 'dataset'}
if not required_columns.issubset(df.columns):
    raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

df['dataset_lower'] = df['dataset'].str.lower()

df['split'] = None

df.loc[df['dataset_lower'] == 'kid', 'split'] = 'train'
df.loc[df['dataset_lower'] == 'aiims', 'split'] = 'train'
df.loc[df['dataset_lower'] == 'kid_v', 'split'] = 'val'
df.loc[df['dataset_lower'] == 'aiims_v', 'split'] = 'val'

non_lesion_cols = ['image_path', 'dataset', 'dataset_lower', 'split']
lesion_cols = [col for col in df.columns if col not in non_lesion_cols]

remaining = df[df['split'].isna()]
split_chunks = []

for (dataset, label), group in remaining.groupby(
    ['dataset'] + [df[lesion_cols].idxmax(axis=1)]
):
    if len(group) < 2:
        group['split'] = 'train'
    else:
        train_df, val_df = train_test_split(
            group, test_size=0.2, random_state=42, shuffle=True
        )
        train_df['split'] = 'train'
        val_df['split'] = 'val'
        group = pd.concat([train_df, val_df])
    split_chunks.append(group)

split_df = pd.concat(split_chunks) if split_chunks else pd.DataFrame()
final_df = pd.concat([df[df['split'].notna()], split_df])

final_df.drop(columns=['dataset_lower'], inplace=True)

output_csv = "/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/Train+Val/lesion_dataset_with_split.csv"
final_df.to_csv(output_csv, sep='\t', index=False)

print(f"Done! Split column added and saved to:\n{output_csv}")
print(final_df[['image_path', 'dataset', 'split']].sample(5))
