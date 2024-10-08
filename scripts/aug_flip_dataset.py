import os
import shutil

import cv2
from tqdm import tqdm


def flip_images(source_dir, destination_dir):
    for root, dirs, files in tqdm(os.walk(source_dir), desc='flip augmentation'):
        for file in files:
            # Get the path of the current file
            source_path = os.path.join(root, file)

            # Create the corresponding destination directory structure
            relative_path = os.path.relpath(source_path, source_dir)
            destination_dir_path = os.path.dirname(relative_path)
            destination_dir_name = os.path.basename(destination_dir_path) + "_flipped"
            destination_dir_path = os.path.join(destination_dir, destination_dir_name)
            os.makedirs(destination_dir_path, exist_ok=True)

            # Read the image and flip it
            image = cv2.imread(source_path)
            flipped_image = cv2.flip(image, 1)  # 1 for horizontal flip

            # Save the flipped image to the destination folder
            destination_file_path = os.path.join(destination_dir_path, file)
            cv2.imwrite(destination_file_path, flipped_image)

# Example usage
source_directory = "bb-dataset-cropped-upper/images_new"
destination_directory = "bb-dataset-cropped-upper/images_flipped"

flip_images(source_directory, destination_directory)

for file in os.listdir(source_directory):
    shutil.move(os.path.join(source_directory, file), destination_directory)
os.rmdir(source_directory)
print("Done flip")
