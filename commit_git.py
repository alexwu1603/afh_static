import os
import subprocess
import time

# Get the current working directory (the directory where the script is located)
repo_path = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the repository path
os.chdir(repo_path)

# Function to commit changes
def commit_changes():
    try:
        # Add all changes to the staging area
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit the changes with a commit message
        subprocess.run(['git', 'commit', '-m', 'add new website na'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)

        print('Changes committed successfully.')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')

# Main loop to commit changes every 30 minutes
while True:
    commit_changes()
    # Wait for 30 minutes (1800 seconds)
    time.sleep(1800)
