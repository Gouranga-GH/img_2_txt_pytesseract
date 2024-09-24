# Import necessary libraries
# 'cv2' is the OpenCV library used for image processing operations
import cv2

# Function to convert image to grayscale and apply thresholding
def preprocess_image(image):
    # Convert the image to grayscale
    # 'cv2.cvtColor' converts the image from its original color space (BGR in OpenCV) to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    # 'cv2.threshold' converts the grayscale image into a binary image (black and white)
    # Pixels with values greater than or equal to 128 are set to 255 (white), others are set to 0 (black)
    # The first return value '_' is ignored as it's the threshold value used internally
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Return the thresholded binary image
    return thresh
