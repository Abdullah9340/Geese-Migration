import requests
from bs4 import BeautifulSoup
from houses import House
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://listings.och.uwaterloo.ca/Listings/Search/Results"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

def get_OCH_uwaterlooOCH_listings():
    houses = []
    for row in soup.find_all('tr'):
        print(row.find('a',href=True).get('href'))