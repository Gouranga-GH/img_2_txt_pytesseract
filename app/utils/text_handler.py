# Import necessary libraries
# 'os' is used to handle file and directory operations such as path creation and file writing
import os

# Function to save extracted text to a file
# 'text' is the extracted text content
# 'filename' is the name of the file where the text will be saved
# 'folder_path' is the directory where the file will be saved (default is 'data')
def save_text_to_file(text, filename, folder_path='data'):
    # Create the full file path
    # 'os.path.join' safely combines the folder path and filename into a complete file path
    file_path = os.path.join(folder_path, filename)

    # Open the file in write mode ('w') and save the text
    # 'with open()' ensures that the file is properly closed after writing, even if an error occurs
    with open(file_path, 'w') as f:
        # Write the extracted text into the file
        f.write(text)
