import requests
import time
from lxml import etree

   # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362
def get_html(url):
	headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
	response = requests.get(url,headers=headers)
	if response.status_code == 200:
		# print('------开始爬取网页信息------')
		response.encoding = 'utf-8'
		return response.text
	else:
		return

def get_info(html):
	html = etree.HTML(html)
	ls = html.xpath('//tr[@class="item"]')
	# print('------开始解析网页-------')
	for i in ls:
		print('gogogo')
		name = i.xpath('./td[2]/div[1]/a/text()')[0].replace('\n','').replace(' ','')
		info = i.xpath('./td[2]/p[1]/text()')[0]
		score = i.xpath('./td[2]/div[2]/span[2]/text()')[0]
		nums = i.xpath('./td[2]/div[2]/span[3]/text()')[0].replace('\n','').replace(' ','')
		data = {'书名：':name,
		        '出版信息：':info,
		        '豆瓣评分：':score,
		        '评价人数：':nums}
		print(data)


def main():
	urls = ['https://book.douban.com/top250?start={}'.format(str(i))for i in range(0,250,25)]
	for url in urls:
		html = get_html(url)
		get_info(html)
		time.sleep(1)

if __name__ == '__main__':
	main()