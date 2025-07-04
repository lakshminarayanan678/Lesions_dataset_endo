import pandas as pd

# Load the CSV file
df = pd.read_csv('/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data/capsulevision/train_val.csv')

# Define the classes to keep
keep_classes = ['ulcers', 'erosion', 'normal']

# Filter the DataFrame
filtered_df = df[df['original_class'].isin(keep_classes)]

# Save the filtered DataFrame to a new CSV (optional)
filtered_df.to_csv('/home/endodl/PHASE-1/mln/lesions_cv24/MAIN/data/capsulevision/ulcers_erosions_normal_train_val.csv', index=False)

# Display a preview
print(filtered_df.head())