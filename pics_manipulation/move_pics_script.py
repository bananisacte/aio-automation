import os
import shutil

# Define the source and destination directories
source_dir = 'C:\\Users\\kunyz\\Desktop\\AiO\\תמונות מוצרים\\30-07-2024\\Mor_Levi_Pics&URL_FINAL_MANUAL_URL\\07-30 133006\\Pic1'
destination_dir = 'C:\\Users\\kunyz\\Desktop\\AiO\\תמונות מוצרים\\30-07-2024\\amd_mobos'

# Ensure the destination directory exists
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# List of image IDs to be copied
image_ids = [
    '95A52003', '95A52006', '95A52007', '95B55017', '95A62015', '95B55010', '95A62001',
    '95B55023', '95X67010', '95B65066', '95X67030-2', '95X67150-1', '95TRX50', '95A62010',
    '95B55037', '95B65000-13', '95B65073', '95B65010', '95B65110', '95B65050', '95B65101',
    '95A52005', '95B55022', '95B65000', '95B65020', '95X67012', '95B65062'
]

# Get a list of all files in the source directory
all_files = os.listdir(source_dir)

# Loop through the list of image IDs
for image_id in image_ids:
    # Loop through all files to find matches
    for file_name in all_files:
        if image_id in file_name:
            source_file = os.path.join(source_dir, file_name)
            destination_file = os.path.join(destination_dir, file_name)

            # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f'Copied: {source_file} to {destination_file}')

print('File copying completed.')
