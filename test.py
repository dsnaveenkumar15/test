#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess, os

# Set the repository paths
repo1="N:\\Professional\\Office\\DevOps\\visa\\repo\\test-old\\test\\"
repo2="N:\\Professional\\Office\\DevOps\\visa\\repo\\test-new\\test\\"

# Move to repository 1 and fetch the latest changes
os.chdir(repo1)
subprocess.run(["git", "fetch"], shell = True)

# Move to repository 2 and fetch the latest changes
os.chdir(repo2)
subprocess.run(["git", "fetch"], shell = True)

# Compare the two repositories and get the list of changed files
changed_files = subprocess.run(["git", "diff", "--name-only", "repo1/master", "repo2/master"], capture_output=True)

# Split the list of changed files into a list
changed_files = changed_files.stdout.decode().strip().split("\n")

# Iterate through the list of changed files and get the number of lines changed
for file in changed_files:
    lines_changed = subprocess.run(["git", "diff", "--stat", "repo1/master", "repo2/master", file], capture_output=True)
    print(f"{file}: {lines_changed.stdout.decode().strip()}")
