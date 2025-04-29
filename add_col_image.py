import pandas as pd
import os

# Path to the CSV file
csv_path = os.path.join(os.getcwd(), "csv_dataset", "english_accounting.csv")
# output_path = os.path.join(os.getcwd(), "csv_dataset", "english_chemistry_with_images.csv")

try:
    # Read the CSV file
    df = pd.read_csv(csv_path, quotechar='"')
    
    # Add empty columns for images in the desired order
    new_df = pd.DataFrame()

    new_df['problem'] = df['problem']
    new_df['image_problem'] = ""  # Empty column for problem images
    new_df['answer'] = df['answer']
    new_df['image_answer'] = ""   # Empty column for answer images

    # new_df['problem'] = df['problem']
    # new_df['image_problem'] = df['image_problem']  # Empty column for problem images
    # new_df['image2_problem'] = ""
    # new_df['answer'] = df['answer']
    # new_df['image_answer'] = df['image_answer']   # Empty column for answer images
    # new_df['image2_answer'] = ""

    
    # Save to a new CSV file
    new_df.to_csv(csv_path, index=False, quoting=1)  # quoting=1 means QUOTE_ALL
    
    print(f"Modified CSV saved to: {csv_path}")
    print(f"New column structure: {new_df.columns.tolist()}")
    print(f"Total rows: {len(new_df)}")
    
except Exception as e:
    print(f"Error processing CSV file: {e}")