import easyocr
import cv2

def extract_text_from_image(image):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])  # You can specify additional languages if needed


    # Extract text from the image
    result = reader.readtext(image)

    # Process the result
    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + " "  # Append the text to the result

    return extracted_text.strip()  # Remove leading/trailing whitespaces

# Example usage:
# image_path = 'img.png'
# extracted_text = extract_text_from_image(image_path)
# print()
# print("Extracted Text:", extracted_text)