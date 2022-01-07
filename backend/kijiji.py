import requests
from bs4 import BeautifulSoup
from houses import House

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://www.kijiji.ca/b-real-estate/kitchener-waterloo/student-housing/k0c34l1700212?rb=true&ll=43.464258%2C-80.520410&address=Waterloo%2C+ON&ad=offering&radius=50.0"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

def get_kijiji_listings():
    houses = []
    for link in soup.find_all('div', {'class': 'clearfix'}):
        if link.find('div', {'class': 'price'}):
            posting_name = str(
                link.find('a', {'class': 'title'}, href=True).get_text()).strip().replace("    ", "")
            posting_price = str(
                link.find('div', {'class': 'price'}).get_text()).strip()
            posting_link = f"https://www.kijiji.ca{link.find('a', href=True).get('href')}".strip(
            )
            posting_desc = str(
                link.find('div', {'class': 'description'}).get_text()).strip().replace("    ", "")

            if link.find('span', {'class': 'bedrooms'}):
                posting_beds = str(
                    link.find('span', {'class': 'bedrooms'}).get_text()).strip().replace("    ", "")
            else:
                posting_beds = ""
            if link.find('span', {'class': 'intersection'}):
                posting_location = str(
                    link.find('span', {'class': 'intersection'}).get_text()).strip().replace("    ", "")
            else:
                posting_location = ""
            houses.append(House(posting_name, posting_price,
                          posting_desc, posting_beds, posting_location, posting_link, ""))
    return houses

houses = get_kijiji_listings()
