from datetime import datetime
import requests
from bs4 import BeautifulSoup


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def get_price_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
#     soup = BeautifulSoup(page)

    try:
        input_tag = soup.find(attrs={"name": "lastPrice"})
        output = input_tag['value']
        print (output)
    except:
        return "None, None, None"

if __name__ == '__main__':
    url = "https://www.theglobeandmail.com/investing/markets/funds/TDB886.CF/" 
    get_price_info(url)


            # message = price_str

    # with open(datetime.now().strftime("%d-%m-%Y"),"w") as file:
    #     file.write("test automation " + price_str)
