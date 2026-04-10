import requests
import re
import os
import threading

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "scan_survival_urls.txt")

if os.path.isfile(filename):
    pass
else:
    with open(filename,"w",encoding='utf-8') as f:
        pass

path = os.path.dirname(os.path.abspath(__file__)) + "\\scan_survival_urls.txt"
scan_lock = threading.Lock()
urled = set()

def scan_survival():
    #print(path)
    try:
        with open(path,"r",encoding='utf-8') as f:
            urls = f.read().splitlines()
            for url in urls:
                if not url.strip():
                    continue
                url = f"https://{url}"
                if url in urled:
                    continue
                urled.add(url)
                try:
                    response = requests.get(url, headers=headers, timeout=2.5)
                    response.encoding = "utf-8"
                    title = re.findall("<title>(.*?)</title>", response.text)[0]
                    with scan_lock:
                        if response.status_code == 200:
                            print(f"[\033[32m*\033[0m] \033[34m{url}\033[0m ——> 响应码: \033[32m{response.status_code}\033[0m ——> 长度: \033[32m{len(response.text)}\033[0m ——> 标题: \033[35m{title}\033[0m")
                        else:
                            print(f"[\033[31m*\033[0m] \033[34m{url}\033[0m ——> 响应码: \033[31m{response.status_code}\033[0m ——> 长度: \033[31m{len(response.text)}\033[0m ——> 标题: \033[35m{title}\033[0m")
                except:
                    with scan_lock:
                        print(f"[\033[31m*\033[0m] \033[34m{url}\033[0m ——> \033[31m该站点已死亡\033[0m")
    except:
        print("\033[31m路径打开失败！请检查项目文件是否完整！若无法确定请重新下载项目！\033[0m")
        os._exit(1)

def get_survival():
    print('\033[36m——————————————————————————————开始检测——————————————————————————————\033[0m')
    for th in range(30):
        t = threading.Thread(target=scan_survival, args=()).start()
