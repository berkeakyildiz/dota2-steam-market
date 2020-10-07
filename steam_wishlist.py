import json
import urllib.request
from time import sleep

baseUrl = "http://steamcommunity.com/market/priceoverview/?appid=570&currency=17&market_hash_name="
# baseUrl = "http://api.steamapis.com/market/item/570/"
# api = "?api_key="

f = open("wishlist_items.txt", "r+", encoding='unicode_escape')
total = 0
w = open("wishlist_prices.txt", "r+")
steam_apis_api_key = "kD6b30v2QSyq3moqPWk7IGgk4NY"
steam_web_api_key = "2BCA06981311CE96B9B9A4DFE502D342"
count = 0

for line in f:
    # if count == 10:
    #     sleep(30)
    count = count + 1
    print(line)
    item = line.replace("\'", "%27")
    item = item.replace(" ", "%20")
    url = baseUrl + item
    url = url.strip()
    # url = url + api + steam_apis_api_key
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    lowest_price = data["lowest_price"]
    print(lowest_price)
    line = line.replace("\n", "")
    w.writelines(line + " = " + lowest_price + "\n")
    lowest_price = lowest_price.replace(".", "")
    lowest_price = lowest_price.replace(",", ".")
    lowest_price = lowest_price.split()[0]
    price = float(lowest_price)
    total += price
    sleep(6)
    # print(total)
w.writelines("\n\n\nTotal Price: " + total.__str__() + "  TL \n")

