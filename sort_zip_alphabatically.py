import pandas as pd
import zipfile
import os

zip_file_path = 'blocklist.zip'
text_file_name = 'randomized.txt'
sorted_file_name = 'sorted_blocklist.txt'

# Read the text file from the ZIP archive
df = pd.read_csv(zip_file_path, compression='zip', header=None, sep=',', quotechar='"')

# Sort the DataFrame alphabetically
df_sorted = df.sort_values(by=0)

# Save the sorted data to a new text file
sorted_file_path = sorted_file_name
df_sorted.to_csv(sorted_file_path, header=False, index=False)

# Create a temporary ZIP file and add the sorted text file to it
temp_zip_file_path = 'temp.zip'
with zipfile.ZipFile(temp_zip_file_path, 'w') as temp_zip:
    temp_zip.write(sorted_file_path, arcname=text_file_name)

# Replace the original ZIP file with the updated one
os.replace(temp_zip_file_path, zip_file_path)

print(df.describe())
