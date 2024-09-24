import os

# Define the folder structure
folders = [
    'app',
    'app/utils',
    'app/routes',
    'data',
    'tests'
]

# Define the files to be created with optional content
files = {
    'app/utils/ocr_helper.py': '# OCR helper functions',
    'app/utils/image_preprocess.py': '# Image preprocessing functions',
    'app/utils/text_handler.py': '# Text handling functions',
    'app/routes/ocr_routes.py': '# API routes for OCR',
    'app/__init__.py': '# Initialize data module',
    'app/config.py': '# Configuration settings',
    'tests/test_ocr_api.py': '# Unit tests for OCR API',
    'requirements.txt': '# Add required packages here\nflask\npytesseract\nopencv-python',
    'README.md': '# Project README\nThis is an OCR project using Flask and Tesseract.',
    '.gitignore': '# Python\n__pycache__/\n*.pyc\nvenv/\n.env',
    'run.py': '# Application entry point\nfrom app import app\n\nif __name__ == "__main__":\n    app.run(debug=True)'
}

# Create the folder structure
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create the files with the specified content
for filepath, content in files.items():
    with open(filepath, 'w') as file:
        file.write(content)

print("Folder structure and files have been created successfully.")
