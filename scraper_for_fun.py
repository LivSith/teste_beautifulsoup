import requests
from bs4 import BeautifulSoup


website_url = 'http://scraping.pro/web-scraper-test-drive/'
catch_data = requests.get(website_url)

soup = BeautifulSoup(catch_data.text, 'lxml')

table_test = soup.find_all('table', class_='wp-table-reloaded')

# print(catch_data.text)
reference_url = 'http://scraping.pro/web-scraper-test-drive'
for table in table_test:
    list = (table.find_all('td'))
    for datas in list:
        if datas.next_element.name == 'a':
            clean_url = '{0}{1}'.format(reference_url, datas.next_element.get('href'))
            print(clean_url)
        else:
            print (datas.next_element)