import os
import shutil

# The path to your minions directory
minions_dir = '/Users/michaelgruen/Desktop/minions'

# Create directories for each agent
agent_dirs = ["memory", "executioner", "taskmaster"]
for dir_name in agent_dirs:
    os.makedirs(os.path.join(minions_dir, dir_name), exist_ok=True)

# Move corresponding files into their directories
file_to_dir_mapping = {
    "memory.py": "memory",
    "executioner.py": "executioner",
    "taskmaster.py": "taskmaster"
}

for file_name, dir_name in file_to_dir_mapping.items():
    src_path = os.path.join(minions_dir, file_name)
    dest_path = os.path.join(minions_dir, dir_name, file_name)
    shutil.move(src_path, dest_path)