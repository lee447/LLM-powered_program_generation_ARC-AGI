import os
import random
import shutil

# Paths (change to create another evaluation set)
source_folder = "ARC2_Data/evaluation"
target_folder = "Evaluation_set_ARC2" 

os.makedirs(target_folder, exist_ok=True)

# List all JSON files
json_files = [f for f in os.listdir(source_folder) if f.endswith(".json")]

# Select 100 random files
random_files = random.sample(json_files, 100)


for filename in random_files:
    src_path = os.path.join(source_folder, filename)
    dst_path = os.path.join(target_folder, filename)
    shutil.copyfile(src_path, dst_path)

print(f"Copied {len(random_files)} tasks to '{target_folder}'.")
