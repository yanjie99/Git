import re
import requests
from fake_useragent import UserAgent


def get_html(url):
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return


def get_info(html):
    # <dd> <a style="" href="/book/390/293831.html">第两百四十八章 盐城</a></dd>
    pat = '<dd> <a style="" href="/book/390/\d+.html">(.*?)</a></dd>'
    data = re.findall(pat, html)
    # for i in range(len(data)):
    # 	print(data[i])
    # 迭代器
    c = (data[i] for i in range(len(data)))
    for i in c:
        print(i)


def main():
    url = 'https://www.qu.la/book/390/'
    html = get_html(url)
    if html == None:
        print('请求失败')
    else:
        get_info(html)


if __name__ == '__main__':
    main()
