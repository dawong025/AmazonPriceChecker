from bs4 import BeautifulSoup
import requests
import lxml


url = "https://www.amazon.com/Nintendo-Advance-Wars-Reboot-Camp/dp/B097BS4B1R/ref=asc_df_B097BS4B1R/?tag=hyprod-20&linkCode=df0&hvadid=658908762893&hvpos=&hvnetw=g&hvrand=13351719217756823192&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1014221&hvtargid=pla-1346911253480&psc=1&mcid=28ac1f99de763a6d9d54a1b73647f9ce"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers=header)


soup = BeautifulSoup(response.content, "lxml")

# print(soup.prettify())

# Current Price
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

# Full Price
if soup.find(class_="a-price a-text-price") is not None:
    full_price = soup.find(class_="a-price a-text-price").get_text()
    full_price_wo_currency = full_price.split("$")[1]
    f_price_as_float = float(full_price_wo_currency)
    print(f_price_as_float)

print("Current Price: " + price_as_float)



