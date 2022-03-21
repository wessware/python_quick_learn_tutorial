import requests
import sys
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

try:
    html: requests.get(URL).text
    doc = BeautifulSoup(html, 'html_parser')
    table = doc.find('table', class_='nfobox vevent')
    rows = table.find_all('tr')
    link = rows[11].find('a')['href']
    ver = rows[6].find('div').text.split()[0]
    url_i = rows[0].find('img')['src']
    image = requests.get(f'https:{url_i}').content

    with open('test.png', 'wb') as file:
        file.write(image)
    print(link, ver)
except requests.exceptions.ConnectionError:
    print('Error connecting and collecting soup.', file=sys.stderr)
