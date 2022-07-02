import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
r = requests.get(START_URL)
# time.sleep(10)

def scrape():
    headers = ['star', 'distance', 'mass', 'radius']
    planet_data = []
    soup = BeautifulSoup(r.text, 'html.parser')
    table_tag = soup.find('table', attrs = { 'class': 'wikitable sortable' })

    # Web scraping headers rather than writing them out, would still need to remove excess headers
    # headers = []
    # for header_tag in table_tag.find_all('th'):
    #     headers.append(header_tag.text)
    # headers = [header.strip() for header in headers]

    for tr_tag in table_tag.find_all('tr'):
        td_tags = tr_tag.find_all('td')
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            for i in range(0, len(td_tags)):
                if index == i:
                    # if index == headers.index('Star') or index == headers.index('Distance (ly)') or index == headers.index('Mass(MJ)') or index == headers.index('Radius(RJ)'):
                    if index == 0 or index == 5 or index == 8 or index == 9:
                        temp_list.append(td_tag.text)
        planet_data.append(temp_list)
    planet_data.pop(0)

    with open('data.csv', 'w',encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()