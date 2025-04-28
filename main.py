##########################
# Save data to local
##########################

# from datasets import load_dataset, Dataset
# import os
# import pandas as pd

# # Create directory to save dataset
# output_dir = os.path.join(os.getcwd(), "local_dataset")
# csv_dir = os.path.join(os.getcwd(), "csv_dataset")
# os.makedirs(output_dir, exist_ok=True)
# os.makedirs(csv_dir, exist_ok=True)

# # Load from Hugging Face
# dataset = load_dataset("ReliableAI/Leaving_Cert_2024")

# # Save dataset to local directory in HF format
# dataset.save_to_disk(output_dir)

# # Export to CSV files (one per split)
# for split, data in dataset.items():
#     csv_path = os.path.join(csv_dir, f"{split}.csv")
#     df = data.to_pandas()
#     df.to_csv(csv_path, index=False)
#     print(f"CSV exported to: {csv_path}")

# # To verify it worked, print dataset info
# print(f"Dataset saved to: {output_dir}")
# print(dataset)

import pandas as pd
import os

# Path to the CSV file
csv_path = os.path.join(os.getcwd(), "csv_dataset", "irish_physics.csv")

# Read the CSV file
try:
    # Read with proper handling of quoted text containing commas
    df = pd.read_csv(csv_path, quotechar='"')
    
    # Print all problems and answers
    for index, row in df.iterrows():
        print(f"Problem {index+1}:")
        print("-" * 80)
        print(row['problem'])
        print("\nAnswer:")
        print("-" * 80)
        print(row['answer'])
        print("\n" + "=" * 100 + "\n")
        
    print(f"Total problems: {len(df)}")
    
except Exception as e:
    print(f"Error reading CSV file: {e}")