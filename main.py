import requests
from bs4 import BeautifulSoup as bs


def get_jokes():
    url = 'https://www.anekdot.ru/last/anekdot/'
    r = requests.get(url=url)

    soup = bs(r.text, 'html.parser')

    joke = soup.find_all('div', class_="text")

    i = 0

    if i < len(joke):
        for article in joke:
            i += 1
            article_title = article.text.strip() + '\n\n'
            with open("anekdoti.txt", "a", encoding='utf-8') as file:
                file.write(article_title)
        print('Все анекдоты в текстовом документе :)')


get_jokes()
