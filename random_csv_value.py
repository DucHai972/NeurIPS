import os
import pandas as pd

# Define paths
csv_dir = r"C:\Users\Computer\Desktop\NeurIPS\csv_dataset_updated"
parquet_dir = r"C:\Users\Computer\Desktop\NeurIPS\parquet_dataset"
os.makedirs(parquet_dir, exist_ok=True)

# Convert each CSV to Parquet
for filename in os.listdir(csv_dir):
    if filename.endswith(".csv"):
        csv_path = os.path.join(csv_dir, filename)
        parquet_path = os.path.join(parquet_dir, filename.replace(".csv", ".parquet"))
        
        # Read CSV and write as Parquet
        df = pd.read_csv(csv_path)
        df.to_parquet(parquet_path, index=False)
        print(f"Converted {filename} to {parquet_path}")
