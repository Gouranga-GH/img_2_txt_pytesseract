# Import necessary libraries
# 'cv2' is the OpenCV library for reading and processing images
# 'pytesseract' is the Python wrapper for the Tesseract OCR engine, used to extract text from images
import cv2
import pytesseract

# Import the custom 'preprocess_image' function from the app's utils module
# This function is responsible for preprocessing the image before OCR (e.g., converting to grayscale, applying thresholding)
from app.utils.image_preprocess import preprocess_image

# Function to process the image for OCR
def process_image_for_ocr(image_path):
    # Read the image from the file path
    # 'cv2.imread' loads the image from the specified path into memory as a multi-dimensional array
    image = cv2.imread(image_path)

    # Preprocess the image (grayscale, thresholding, etc.)
    # The 'preprocess_image' function prepares the image for better OCR results by performing operations like grayscale conversion and thresholding
    processed_image = preprocess_image(image)

    # Apply pytesseract to extract text from the processed image
    # 'pytesseract.image_to_string' performs Optical Character Recognition (OCR) on the image and returns the detected text as a string
    text = pytesseract.image_to_string(processed_image)

    # Return the extracted text
    return text
