'''

'''

import requests
from bs4 import BeautifulSoup

def input_interface():
    url = "https://read.wqyunpan.com/qrcode/79712?fileId=391069"
    return url

def qyunpan_crawler():
    url = input_interface()
    response = requests.get(url)
    left_keyword = bytes("<head><",encoding='utf-8')
    right_keyword = bytes(">",encoding='utf-8')
    left = response.content.find(left_keyword) + len(left_keyword);print("left =",left);print('len(left_keyword) =',len(left_keyword))
    right = response.content.find(right_keyword,left);print('right =',right)# 右关键字的首项索引不被切片，切片左闭右开正好合适
    if left != -1 and right != -1:
        target = response.content[left:right]
        print(target)

qyunpan_crawler()