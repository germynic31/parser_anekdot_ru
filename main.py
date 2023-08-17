import requests
from bs4 import BeautifulSoup as bs


def get_jokes():
    url = 'https://www.anekdot.ru/last/anekdot/'
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        return print(f'Ошибка при запросе страницы: {e}')

    soup = bs(r.text, 'html.parser')

    jokes = soup.find_all('div', class_="text")

    with open("anekdoti.txt", "w", encoding='utf-8') as file:
        for joke in jokes:
            article_title = joke.text.strip() + '\n\n'
            file.write(article_title)
    print('Все анекдоты в текстовом документе :)')


get_jokes()
