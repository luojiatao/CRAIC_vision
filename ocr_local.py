import paddlehub as hub
import cv2

img_path = r'C:\Users\luojiatao\Desktop\CRAIC\ocr.png'

ocr = hub.Module(name="ch_pp-ocrv3", enable_mkldnn=True)       # mkldnn加速仅在CPU下有效
result = ocr.recognize_text(images=[cv2.imread(img_path)])

print(result)
