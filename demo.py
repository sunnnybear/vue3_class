#展示现在微博热搜前30条数据
import requests
from bs4 import BeautifulSoup
import time

url = 'https://s.weibo.com/top/summary?cate=realtimehot'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
lis = soup.select('div.data > table > tbody > tr')
for li in lis:
    title = li.select_one('td.td-02 > a').text
    hot = li.select_one('td.td-02 > span').text
    print(title, hot)
    time.sleep(1)



