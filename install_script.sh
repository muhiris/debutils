#!/bin/bash

# Set the GitHub repository URL
github_repo="https://raw.githubusercontent.com/muhiris/debutils/main"

# Download the Python script
curl -fsSL "$github_repo/init.py" -o init.py

# Run the Python script
python3 init.py

# Optionally, you can remove the downloaded script
# rm init.py
