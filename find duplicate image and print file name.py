import os
import hashlib
from PIL import Image

def file_hash(filepath):
    """Calculate the MD5 hash of the image file."""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def find_duplicates(folder_path):
    """Find duplicate images in the given folder."""
    duplicates = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):  # Checking only JPG files
            file_path = os.path.join(folder_path, filename)
            filehash = file_hash(file_path)
            if filehash in duplicates:
                duplicates[filehash].append(filename)
            else:
                duplicates[filehash] = [filename]
    return duplicates

def print_duplicates(duplicates):
    """Print the names of duplicate images."""
    for key, filenames in duplicates.items():
        if len(filenames) > 1:
            print(f'Duplicate images: {filenames}')

folder_path = 'path_to_your_folder'  # Replace with your folder path
duplicates = find_duplicates(folder_path)
print_duplicates(duplicates)
