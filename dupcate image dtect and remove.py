import os
import hashlib
from PIL import Image

def file_hash(filepath):
    """Calculate the MD5 hash of the image file."""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def find_duplicates(folder_path):
    """Find and remove duplicate images in the given folder."""
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

def remove_duplicates(duplicates, folder_path):
    """Remove duplicate images, keeping one instance of each."""
    for key, filenames in duplicates.items():
        if len(filenames) > 1:
            # Keeping the first file and removing the rest
            for filename in filenames[1:]:
                os.remove(os.path.join(folder_path, filename))
                print(f'Removed: {filename}')

folder_path = 'E:/CAPSTONE ALL/1FIINNAL/140_Augment/app DATASET_140_photos_each_folder - Copy/19. SSD'  # Replace with your folder path
duplicates = find_duplicates(folder_path)
remove_duplicates(duplicates, folder_path)

