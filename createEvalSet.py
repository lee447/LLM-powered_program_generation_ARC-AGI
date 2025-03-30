import os
import random
import shutil

# Paths
source_folder = "ARC_Data/evaluation"
target_folder = "Evaluation_set"  # Now at the same level as ARC_Data

# Ensure target folder exists
os.makedirs(target_folder, exist_ok=True)

# List all JSON files
json_files = [f for f in os.listdir(source_folder) if f.endswith(".json")]

# Select 100 random files
random_files = random.sample(json_files, 100)

# Copy them to the target folder
for filename in random_files:
    src_path = os.path.join(source_folder, filename)
    dst_path = os.path.join(target_folder, filename)
    shutil.copyfile(src_path, dst_path)

print(f"Copied {len(random_files)} tasks to '{target_folder}'.")
