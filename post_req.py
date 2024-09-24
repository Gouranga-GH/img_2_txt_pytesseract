# Import the requests module
# 'requests' is a popular library in Python used to make HTTP requests to APIs or websites
import requests

# API URL
# This is the URL where the Flask API is running locally. It is set to handle image uploads for OCR processing.
url = 'http://127.0.0.1:5000/api/v1/ocr/upload'

# Image file path
# The path to the image file that will be uploaded to the API for OCR processing.
image_path = 'data/sample.png'

# Open the image file and send it to the API
# The image file is opened in binary mode ('rb') so it can be sent as an HTTP POST request.
with open(image_path, 'rb') as img:
    # The 'files' dictionary is created where 'file' is the key and the image file is the value.
    # This prepares the image file for uploading via the POST request.
    files = {'file': img}
    
    # Send a POST request to the specified URL with the image file attached.
    # The 'files' argument is used to send multipart/form-data, which is necessary for file uploads.
    response = requests.post(url, files=files)

# Print the response from the server
# 'response.json()' parses the JSON response returned by the API, which will likely contain the extracted text or an error message.
print(response.json())
