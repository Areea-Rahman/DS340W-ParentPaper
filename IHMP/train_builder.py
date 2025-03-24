import os
import numpy as np
import pandas as pd

# Define paths
data_path = "C:/Users/nitiy/MEME/mortality/train"  # Change to your actual train data directory
label_file = "C:/Users/nitiy/MEME/mortality/train/listfile.csv"  # Path to the label file with the correct labels

# Load labels
df_labels = pd.read_csv(label_file)
df_labels.columns = ["stay", "y_true"]  # Ensure column names are correct

def load_data(file_name):
    file_path = os.path.join(data_path, file_name)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df.values.flatten()  # Flatten if needed
    return None

# Process all files
X, y = [], []
for _, row in df_labels.iterrows():
    data = load_data(row["stay"])
    if data is not None:
        X.append(data)
        y.append(row["y_true"])

# Convert to NumPy arrays
X = np.array(X, dtype=object)  # Use dtype=object if sequences have different lengths
y = np.array(y)

# Save as .npy files
np.save(os.path.join(data_path, "X_train.npy"), X)
np.save(os.path.join(data_path, "y_train.npy"), y)

print("Data processing complete. NumPy files saved.")
