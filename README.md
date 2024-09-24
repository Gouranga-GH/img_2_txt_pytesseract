# OCR Flask API

This project provides an OCR (Optical Character Recognition) API using Flask, OpenCV, and Tesseract. It allows users to upload images, and the API extracts and returns the text from the image using Tesseract OCR.

## Features
- Upload images in PNG, JPG, or JPEG formats.
- Extract text from images using Tesseract OCR.
- Save extracted text to a `.txt` file in the `data` folder.
- Return the extracted text via the API as a JSON response.

## Prerequisites
Before running the application, ensure the following software is installed:

1. **Python 3.x**
2. **Tesseract OCR** installed and configured on your system.

### Installing Tesseract
- **For Windows:**
  1. Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract/wiki/Downloads).
  2. Add the Tesseract installation path to the system's environment variables (usually `C:\Program Files\Tesseract-OCR\tesseract.exe`).

- **Verify Tesseract Installation:**
  Open a terminal or command prompt and run:
  ```bash
  tesseract --version
  ```

You should see the Tesseract version and some information about its setup.

## Installation
Clone the repository:
```bash
git clone <repository_url>
cd <repository_name>
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Set Tesseract Path: Ensure that the path to tesseract.exe is correctly set in `config.py`:
```python
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
```

Create the `data` folder: The API will store uploaded images and extracted text files in the data folder. Ensure that the folder exists:
```bash
mkdir data
```

## Running the Application
Start the Flask app:
```bash
python run.py
```

The app should now be running on `http://127.0.0.1:5000/`. You can check the terminal for confirmation.

## API Endpoints

### 1. Upload Image for OCR
**URL:** `/api/v1/ocr/upload`  
**Method:** `POST`  
**Request:** The API expects an image file to be uploaded with the key `file`.

#### Example Request using Postman:
- Set the method to `POST`.
- URL: `http://127.0.0.1:5000/api/v1/ocr/upload`.
- Under the `Body` tab, choose `form-data`.
- Key: `file`
- Value: [choose an image file to upload]
- Click `Send`.

#### Example Request using Python:
```python
import requests

url = 'http://127.0.0.1:5000/api/v1/ocr/upload'
image_path = 'data/sample.png'

with open(image_path, 'rb') as img:
    files = {'file': img}
    response = requests.post(url, files=files)

print(response.json())
```

#### Example Response:
```json
{
    "message": "File processed successfully",
    "text": "This is the extracted text from the image"
}
```

## Testing
- **Using Postman:** Follow the example provided in the API Endpoints section to test the image upload and OCR extraction.
- **Using Python:** The provided Python script in the example request section can be used to upload an image and get the OCR result.

## Dependencies
- Flask: `Flask==2.0.2`
- OpenCV: `opencv-python==4.5.5.64`
- Tesseract: `pytesseract==0.3.9`
- Pillow: `Pillow==9.1.0`
- Werkzeug: `Werkzeug==2.0.3`

## License
This project is licensed under the MIT License.
