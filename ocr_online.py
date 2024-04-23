# encoding:utf-8
import requests
import base64

def ocr_image(image_path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
    # 使用原始字符串来避免转义字符问题
    with open(image_path, 'rb') as f:
        img = base64.b64encode(f.read())
    params = {"image": img}
    access_token = '24.b6eac3dd0b53ac5c9f689872e670f5a5.2592000.1715309532.282335-60663499'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()

if __name__ == "__main__":
    image_path = r'C:\Users\luojiatao\Desktop\CRAIC_vision\ocr.png'
    result = ocr_image(image_path)
    print(result)
