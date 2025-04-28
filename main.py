from datasets import load_dataset, Dataset
import os
import pandas as pd

# Create directory to save dataset
output_dir = os.path.join(os.getcwd(), "local_dataset")
csv_dir = os.path.join(os.getcwd(), "csv_dataset")
os.makedirs(output_dir, exist_ok=True)
os.makedirs(csv_dir, exist_ok=True)

# Load from Hugging Face
dataset = load_dataset("ReliableAI/Leaving_Cert_2024")

# Save dataset to local directory in HF format
dataset.save_to_disk(output_dir)

# Export to CSV files (one per split)
for split, data in dataset.items():
    csv_path = os.path.join(csv_dir, f"{split}.csv")
    df = data.to_pandas()
    df.to_csv(csv_path, index=False)
    print(f"CSV exported to: {csv_path}")

# To verify it worked, print dataset info
print(f"Dataset saved to: {output_dir}")
print(dataset)

# Example of how to load CSV back into a dataset
# Uncomment and modify after you've edited the CSV files
"""
def load_csv_dataset():
    dataset_dict = {}
    for split in ['train', 'validation', 'test']:  # Adjust based on your splits
        csv_path = os.path.join(csv_dir, f"{split}.csv")
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            dataset_dict[split] = Dataset.from_pandas(df)
    
    return DatasetDict(dataset_dict)

# Load your modified CSV files back into a dataset
modified_dataset = load_csv_dataset()
print(modified_dataset)
"""