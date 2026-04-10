import requests
import re
import base64
import mmh3

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_finger():
    url = input("\033[36m请输入目标url\033[0m:")
    response = requests.get(url,headers=headers,timeout=3)
    icon = re.findall(r'href="(.*?\.ico)"', response.text)[0]
    if icon.startswith('/'):
        icon = icon[1:]
    host = re.findall('(https?://.*?/)', response.request.url)[0]
    icon_url = host + icon
    try:
        icon_response = requests.get(icon_url,headers=headers,timeout=3)
        print('\033[32mFOFA语法: icon_hash="' + str(mmh3.hash(base64.encodebytes(icon_response.content))) + '"\033[0m')
    except:
        print("\033[31m识别失败!\033[0m")