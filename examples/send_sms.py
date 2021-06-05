import json
import sys
import requests
from bs4 import BeautifulSoup
sys.path.append('../lib')
import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
  url = 'http://코로나19경남.kr/main/main.do'

  response = requests.get(url)

  if response.status_code != 200:
    print(response.status_code)
    exit()
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  table = soup.select_one('.city_board .table')
  tds = table.select('table tbody tr+tr td')
  for td in tds:
    print(td.get_text())
  data = {
    'messages': [
      {
        'to': '01024657784',
        'from': '01024657784',
        'text': '경상남도 확진자 수는 ' + tds[1].get_text() + '명입니다.'
      },
    ]
  }
  res = message.sendMany(data)
  print(json.dumps(res.json(), indent=2, ensure_ascii=False))
