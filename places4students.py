import requests
from bs4 import BeautifulSoup
from houses import House
from requests_html import HTMLSession

url = "https://www.places4students.com/Places/PropertyListings?SchoolID=j9CaTYeszhs="
s = HTMLSession()
response = s.get(url)
response.html.render(wait=2, sleep=3)

soup = BeautifulSoup(response.html, 'html.parser')
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
