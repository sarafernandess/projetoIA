import pytesseract
import cv2

# ler a imagem

imagem = cv2.imread("img_4.jpg")

caminho = r"C:\Program Files\Tesseract-OCR"

pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'

# extrair texto
texto = pytesseract.image_to_string(imagem, lang="por")
print(texto)
