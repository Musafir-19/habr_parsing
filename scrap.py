import json
import requests
from bs4 import BeautifulSoup as BS


url = 'https://habr.com/ru/top/daily/'

res = requests.get(url)

habr = []

if res.status_code == 200:
    soup = BS(res.content, 'html.parser')
    div = soup.find('div', class_='tm-articles-list')
    articles = div.find_all('article', class_='tm-articles-list__item')
    for item in articles:
        url = 'https://habr.com' + item.h2.a['href']
        title = item.h2.text
        author = item.find(
            'span', class_='tm-user-info tm-article-snippet__author').text.strip()
        time = item.find(
            'span', class_='tm-article-snippet__datetime-published').text
        comments = item.find(
            'span', class_='tm-article-comments-counter-link__value').text.strip()
        habr.append({'url': url, 'title': title, 'author': author,
                    'time': time, 'comments': comments})

with open('habrScrap.json', 'w', encoding='utf-8') as f:
    json.dump(habr, f, indent=4, ensure_ascii=False)