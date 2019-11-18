# <tr class="alt">
#	<td>16</td>
# 	<td><div align="left">北京理工大学</div></td>
# 	<td>北京</td>
# 	<td>54.0</td>
# 					<td class="hidden-xs need-hidden indicator5">79.7</td>
# 					<td class="hidden-xs need-hidden indicator6" style="display: none;">97.90%</td>
# 					<td class="hidden-xs need-hidden indicator7" style="display: none;">43022</td>
# 					<td class="hidden-xs need-hidden indicator8" style="display: none;">16605</td>
# 					<td class="hidden-xs need-hidden indicator9" style="display: none;">1.042</td>
# 					<td class="hidden-xs need-hidden indicator10" style="display: none;">378</td>
# 					<td class="hidden-xs need-hidden indicator11" style="display: none;">13</td>
# 					<td class="hidden-xs need-hidden indicator12" style="display: none;">872622</td>
# 					<td class="hidden-xs need-hidden indicator13" style="display: none;">253765</td>
# 					<td class="hidden-xs need-hidden indicator14" style="display: none;">3.06%</td>
#</tr>
import requests
from lxml import etree
import time

def get_html(url):
	headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) Apple\
	WebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
	response = requests.get(url,headers=headers)
	if response.status_code == 200:
		response.encoding = 'utf-8'
		return response.text
	else :
		return

def get_info(html):
	html = etree.HTML(html)
	ls = html.xpath("//tr[@class='alt']")
	for info in ls:
		rank = info.xpath('./td[1]/text()')[0]
		name = info.xpath('./td[2]/div/text()')[0]
		province = info.xpath('./td[3]/text()')[0]
		score = info.xpath('./td[4]/text()')[0]
		data = {'中国院校排名:':rank,
		        '校名:':name,
		        '所在省份：':province,
		        '评分：':score}
		print(data)

def main():
	url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
	html = get_html(url)
	get_info(html)
	time.sleep(1)

if __name__ == '__main__':
	main()