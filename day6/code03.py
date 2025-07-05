# 上传文件
import requests

url = 'http://192.168.18.27/upload.php'
files = {
    # file从数据包中的name得知
    'file': open('1.png', 'rb'),
    'filename': '1.png'
}
r = requests.post(url=url, files=files)
print(r.text)
