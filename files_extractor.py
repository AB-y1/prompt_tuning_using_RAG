import os
import shutil


source_dir = "data/patterns/"
target_dir = "target"
def attach_folder_names(source_dir, target_dir):
    """
    Iterates through a folder, attaches the folder name to the files inside it, and copies the files to a target directory.

    Args:
        source_dir (str): The path to the source directory.
        target_dir (str): The path to the target directory.

    Returns:
        None
    """
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate through the source directory
    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)

        # Check if the item is a directory
        if os.path.isdir(folder_path):
            # Iterate through the files in the folder
            for filename in os.listdir(folder_path):
                # Construct the full file path
                file_path = os.path.join(folder_path, filename)

                # Construct the new file name with the folder name
                new_filename = f"{folder_name}_{filename}"
                new_file_path = os.path.join(target_dir, new_filename)

                # Copy the file to the target directory
                shutil.copy2(file_path, new_file_path)
                print(f"Copied {file_path} to {new_file_path}")

extractor = attach_folder_names(source_dir, target_dir)