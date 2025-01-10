"""Main module for automatic daily commits."""

import json
import os
from commit import auto_commit

# Update the CONFIG_PATH to dynamically locate the `config.json` file in the same directory as this script
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

# Load Configuration
with open(CONFIG_PATH, 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

repo_path = config['repo_path']
readme_path = os.path.join(repo_path, config['readme_path'])
commit_prefix = config['commit_prefix']

# Call the auto_commit function
auto_commit(repo_path, readme_path, commit_prefix)
