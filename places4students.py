import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from main import House
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://www.places4students.com/Places/PropertyListings?SchoolID=j9CaTYeszhs="
session = HTMLSession()
resp = session.get(url)
resp.html.render()
html = resp.html.html

soup = BeautifulSoup(html, 'html.parser')
print(soup)


def get_p4s_listings():
    houses = []
    for link in soup.find_all('tr', {'class': 'featured'}):
        print("test")
        posting_name = str(
            link.find('div', {'class': 'listing-title'}).get_text()).strip().replace("  ", "")
        posting_price = str(
            link.find('td', {'class': 'listing-rate'}).get_text()).strip()
        posting_desc = str(
            link.find('div', {'class': 'listing-description'}).get_text()).strip().replace("  ", "")
        posting_beds = "Not Available"
        posting_location = ""
        posting_link = f"https://www.places4students.com/Places/{ link.find('div',{'class':'title'}).find('a',href=True).get('href').strip()}"
        posting_img = f"https://www.places4students.com{link.find('div',{'class':'occupancydate-thumbnail'}).find('img').get('src')}"
        houses.append(House(posting_name, posting_price,
                            posting_desc, posting_beds, posting_location, posting_link, posting_img))

    for link in soup.find_all('tr', {'class': 'AltRow'}):
        posting_name = str(
            link.find('div', {'class': 'listing-title'}).get_text()).strip().replace("  ", "")
        posting_price = str(
            link.find('td', {'class': 'listing-rate'}).get_text()).strip().replace("  ", "")
        posting_desc = str(
            link.find('div', {'class': 'listing-description'}).get_text()).strip().replace("  ", "")
        posting_beds = "Not Available"
        posting_location = ""
        posting_link = f"https://www.places4students.com/Places/{link.find('div',{'class':'title'}).find('a',href=True).get('href').strip()}"
        posting_img = f"https://www.places4students.com{link.find('div',{'class':'occupancydate-thumbnail'}).find('img').get('src')}"
        houses.append(House(posting_name, posting_price,
                            posting_desc, posting_beds, posting_location, posting_link, posting_img))
    return houses


houses = get_p4s_listings()
print(houses)
for a in houses:
    print("--------------------------------------------")
    print(a)
    print("--------------------------------------------")
