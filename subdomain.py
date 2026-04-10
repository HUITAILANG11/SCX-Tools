import requests
import re
import os
import threading

current_dir = os.getcwd()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
subdomain_set = set()
scan_lock = threading.Lock()
have_url = set()

def get_maindomain():
    main_domain = input("\033[36m请输入需要搜查的主域名\033[0m(例:\033[33mbaidu.com\033[0m):\n")
    return main_domain

def get_quantity():
    while True:
        print("\033[36m请选择探测量级\033[0m(\033[33m量级越大，可探测的子域名越多，速度越慢\033[0m)\033[32m:\033[0m")
        print("[1]\033[32m500\033[0m    [2]\033[32m5000\033[0m    [3]\033[33m20000\033[0m    [4]\033[33m50000\033[0m    [5]\033[31m100000\033[0m")
        arr = [1,2,3,4,5]
        quantity = int(input())
        if quantity not in arr:
            print("选择无效！请重新选择！")
            continue
        break
    return quantity

def scan_subdomain(main_domain, quantity):
    if quantity == 1:
        path = current_dir + "\\subdomains\\deepmagic.com-prefixes-top500.txt"
    elif quantity == 2:
        path = current_dir + "\\subdomains\\subdomains-top1million-5000.txt"
    elif quantity == 3:
        path = current_dir + "\\subdomains\\subdomains-top1million-20000.txt"
    elif quantity == 4:
        path = current_dir + "\\subdomains\\deepmagic.com-prefixes-top50000.txt"
    elif quantity == 5:
        path = current_dir + "\\subdomains\\bitquark-subdomains-top100000.txt"
    path = path.replace("\\\\", "\\").replace("\\", "\\\\")
    try:
        with open(path, "r", encoding = "utf-8") as f:
            submin_list = f.read().splitlines()
            for submin in submin_list:
                with scan_lock:
                    if submin in subdomain_set:
                        continue
                    subdomain_set.add(submin)
                try:
                    url = f"https://{submin}.{main_domain}"
                    response = requests.get(url, headers=headers, timeout=2.5)
                    response.encoding = "utf-8"
                    title = re.findall("<title>(.*?)</title>", response.text)[0]
                    if response.status_code == 200:
                        with scan_lock:
                            print(f"[\033[32m*\033[0m] \033[34m{response.url}\033[0m ——> 标题: \033[35m{title}\033[0m")
                except:
                    pass
    except:
        print("\033[31m运行出现错误！请确保项目文件完整！若无法确定请重新下载完整项目\033[0m！")

def get_submin():
    maindomain = get_maindomain()
    quantity = get_quantity()
    print("\033[31m注意\033[0m:\033[33m线程越多，速度越快，触发网站WAF防御机制的风险越大，准确率相对更低一些，不建议线程数过高，一般10-50即可\033[0m")
    while True:
        num = int(input("\033[36m请选择线程数\033[0m(\033[33m1\033[0m~\033[33m300\033[0m):"))
        if num < 1:
            print("\033[33m线程数过低\033[0m")
            continue
        elif num > 300:
            print("\033[33m线程数过高\033[0m")
            continue
        break
    print("\033[33m探测量级越大，速度越慢，请耐心等待...\033[0m(\033[31m如果长时间没有任何结果输出，请检查域名是否输入正确并重新启动程序\033[0m)")
    print('\033[36m——————————————————————————————开始检测——————————————————————————————\033[0m')
    for th in range(num):
        t = threading.Thread(target=scan_subdomain, args=(maindomain,quantity,)).start()