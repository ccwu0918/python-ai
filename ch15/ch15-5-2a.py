import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("images/traditional2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img, lang="chi_tra_vert")
print(text.strip())

