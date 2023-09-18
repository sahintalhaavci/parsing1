import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='itemList')
    news = catalog.find_all('div', class_='itemContainer itemContainerLast')
    for new in news:
        try:
            title = new.find('a', class_='itemImage').get('title')
        except:
            title = "Название не указано"


        data = {
            'title': title
        }
        write_csv(data)
        

def write_csv(data: dict) -> None:
    with open('cars.csv', 'a') as csv_file:
        fieldnames = ['title']
        writer = csv.DictWriter(csv_file, delimiter='/', fieldnames=fieldnames)
        writer.writerow(data)


def main():
    url = 'https://vesti.kg/'
    html = get_html(url)
    data = get_data(html)

main()