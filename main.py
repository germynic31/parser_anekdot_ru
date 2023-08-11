import requests
from bs4 import BeautifulSoup


def anekdot():
    url = 'https://www.anekdot.ru/last/anekdot/'
    r = requests.get(url=url)

    soup = BeautifulSoup(r.text, 'html.parser')

    anecdot = soup.find_all('div', class_="text")

    i = 0

    if i < len(anecdot):
        for article in anecdot:
            i += 1
            article_title = article.text.strip() + '\n\n'
            print(article_title)
            with open("anekdoti.txt", "a", encoding='utf-8') as file:
                file.write(article_title)


anekdot()
