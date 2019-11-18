import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
	headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
	respones = requests.get(url,headers=headers)
	if respones.status_code == 200:
		return respones.text
	else:
		return

def get_infos(html):
	html = BeautifulSoup(html)
	rank = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
	##rankWrap > div.pc_temp_songlist > ul > li:nth-child(3) > a
	names = html.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
	times = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')

	for r,n,t in zip(rank,names,times):
		r = r.get_text().replace('\n','').replace('\t','').replace('\r','')
		n = n.get_text()
		t = t.get_text().replace('\n','').replace('\t','').replace('\r','')
		data = {'Rank':r,'Names':n,'Times':t}
		print(data)

def main():
	urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,24)]
	for url in urls:
		html = get_html(url)
		get_infos(html)
		time.sleep(1)

if __name__ == '__main__':
	main()

