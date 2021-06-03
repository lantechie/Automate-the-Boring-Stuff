from datetime import datetime
import requests
from bs4 import BeautifulSoup


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def get_price_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features="lxml")

    try:
        # title = soup.find(id='productTitle').get_text().strip()
        # price_str = soup.find(id='priceblock_ourprice').get_text()
        price_str =soup.find("td", text="TD Comfort Balanced Portfolio").find_next_sibling("td").text
        print(price_str)
    except:
        return None, None, None

if __name__ == '__main__':
    url = "https://www.td.com/ca/en/asset-management/funds/solutions/portfolio-solutions/comfort-portfolios"
    get_price_info(url)


            # message = price_str

    # with open(datetime.now().strftime("%d-%m-%Y"),"w") as file:
    #     file.write("test automation " + price_str)
