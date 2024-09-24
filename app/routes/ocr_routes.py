# Import required modules
# 'os' is used to handle file system paths and directory operations
import os
# 'Blueprint', 'request', and 'jsonify' are Flask utilities for handling routes, requests, and JSON responses
from flask import Blueprint, request, jsonify

# 'secure_filename' ensures that the uploaded file's name is sanitized
from werkzeug.utils import secure_filename

# Import helper functions from app.utils for processing OCR and saving text to a file
from app.utils.ocr_helper import process_image_for_ocr
from app.utils.text_handler import save_text_to_file

# Create a new Blueprint named 'ocr' for handling OCR-related routes
# This allows the separation of routes into modular sections for better organization
ocr_blueprint = Blueprint('ocr', __name__)

# Define a set of allowed file extensions for image uploads (only .png, .jpg, and .jpeg are accepted)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check if the uploaded file has a valid extension
# Splits the filename at the last dot, checks the extension, and verifies if it's in the allowed list
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define a route for handling image uploads using the POST method
# '/upload' is the API endpoint for this route, which will process image files
@ocr_blueprint.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is part of the request; if not, return an error in JSON format with status code 400 (Bad Request)
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    # Extract the file from the request
    file = request.files['file']

    # Check if the file exists and if it has a valid extension using 'allowed_file'
    if file and allowed_file(file.filename):
        # Sanitize the filename to avoid potential security issues
        filename = secure_filename(file.filename)
        
        # Ensure the 'data' directory exists; if it doesn't, create it
        if not os.path.exists("data"):
            os.makedirs("data")
        
        # Construct the path where the uploaded file will be saved (in the 'data' directory)
        image_path = os.path.join("data", filename)
        
        # Save the uploaded file to the specified path
        file.save(image_path)

        # Process the saved image using OCR to extract text from the image
        text = process_image_for_ocr(image_path)
        
        # Save the extracted text to a .txt file in the 'data' directory, named after the original image
        save_text_to_file(text, f"{filename}.txt")

        # Return a success message along with the extracted text in JSON format with status code 200 (OK)
        return jsonify({"message": "File processed successfully", "text": text}), 200
    else:
        # If the file extension is not valid, return an error message in JSON format with status code 400 (Bad Request)
        return jsonify({"error": "Invalid file format"}), 400
