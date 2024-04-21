# encoding:utf-8
import requests 
 
# 替换下面的【官网获取的AK】和【官网获取的SK】为你的实际API密钥和密钥
client_id = 'ySe9DRS6OSVgqLgGn1AJ9hIL'
client_secret = 'gZlG95dxMl6DoqA7RDhmywJp6a3JVBBi'
 
# 构建获取访问令牌的URL
token_url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
 
# 发送请求获取访问令牌
response = requests.get(token_url)
 
# 检查响应状态码
if response.status_code == 200:
    access_token = response.json()['access_token']
    print(f"Access Token: {access_token}")
else:
    print("Failed to obtain Access Token")