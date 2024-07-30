import os

# Define the destination directory
destination_dir = 'C:\\Users\\kunyz\\Desktop\\AiO\\תמונות מוצרים\\30-07-2024\\amd_mobos'

# List of image IDs
image_ids = [
    '95A52003', '95A52006', '95A52007', '95B55017', '95A62015', '95B55010', '95A62001',
    '95B55023', '95X67010', '95B65066', '95X67030-2', '95X67150-1', '95TRX50', '95A62010',
    '95B55037', '95B65000-13', '95B65073', '95B65010', '95B65110', '95B65050', '95B65101',
    '95A52005', '95B55022', '95B65000', '95B65020', '95X67012', '95B65062'
]

# Initialize the list for the links
output_lines = []

# Loop through the list of image IDs
for image_id in image_ids:
    links = []
    # Loop through all files in the destination directory
    for file_name in os.listdir(destination_dir):
        if image_id in file_name:
            link = f'https://files.e-shop5.co.il/allinone/ProdPics/{file_name}'
            links.append(link)

    # Join all the links for the current image ID with ';' without spaces
    if links:
        links_string = ';'.join(links)
        output_lines.append(links_string)

# Save the output lines to a file
output_file = 'image_links.txt'
with open(output_file, 'w') as f:
    for line in output_lines:
        f.write(line + '\n')

print(f'Links saved to {output_file}')
