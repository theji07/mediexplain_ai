from PIL import Image
import pytesseract
import platform

# ✅ Set Tesseract path for Windows (only needed on Windows)
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """Extracts raw text from the image using Tesseract OCR"""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_medicines(raw_text):
    """
    Extracts medicine names from OCR text using simple rule:
    Lines that start with 'Tab' or 'Cap' (e.g., 'Tab Atorvastatin 10mg')
    """
    lines = raw_text.split('\n')
    meds = []
    for line in lines:
        if line.lower().startswith(("tab", "cap")):
            parts = line.split()
            if len(parts) > 1:
                meds.append(parts[1])  # Get the medicine name
    return list(set(meds))  # Return unique medicines
