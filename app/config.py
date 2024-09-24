# Path to Tesseract executable on Windows (this will vary based on installation)
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ensure Tesseract can be accessed by pytesseract
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
