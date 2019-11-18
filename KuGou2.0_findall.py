import requests
from bs4 import BeautifulSoup
import time
import lxml

def get_html(url):
	headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
	respones = requests.get(url,headers=headers)
	if respones.status_code == 200:
		return respones.text
	else :
		return 

def get_info(html):
	html = BeautifulSoup(html,'lxml')
	ranks = html.find_all('span',class_='pc_temp_num')
	names = html.find_all('a',class_='pc_temp_songname')
	times = html.find_all('span',class_='pc_temp_time')
	for r,n,t in zip(ranks,names,times):
		r = r.get_text().replace('\n','').replace('\t','').replace('\r','')
		n = n.get_text()
		t = t.get_text().replace('\n','').replace('\t','').replace('\r','')
		data = {'排名':r,'歌曲时长':t,'歌名&歌手':n}
		print(data)

def main():
	urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,24)]
	for url in urls:
		html = get_html(url)
		get_info(html)
		time.sleep(1)

if __name__ == '__main__':
	main()
