import paddlehub as hub
import cv2

img_path = r'C:\Users\luojiatao\Desktop\CRAIC\ocr.bmp'

ocr = hub.Module(name="ch_pp-ocrv3", enable_mkldnn=True)       # mkldnn加速仅在CPU下有效
result = ocr.recognize_text(images=[cv2.imread(img_path)])

# or 传递文件地址调用
# result = ocr.recognize_text(paths=[img_path])
