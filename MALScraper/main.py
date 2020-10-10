import requests
from bs4 import BeautifulSoup

names = []


def scrap():
    for count in range(0, 151, 50):
        response = requests.get(
            f"https://myanimelist.net/topanime.php?limit={count}")
        if response.status_code == 200:
            print('Success! Trying to parse data..')
            list = parse(response)
        elif response.status_code == 404:
            print('Not Found.')
    print(list)


def parse(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr', class_='ranking-list')
    for row in rows:
        name = row.find_all('a')[1].get_text()
        name = name.split(':')[0]
        names.append(name)

    return names


scrap()
