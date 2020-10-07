import json
import urllib.request
from time import sleep

baseUrl = "http://steamcommunity.com/market/priceoverview/?appid="
secondUrl = "&currency=17&market_hash_name="
# baseUrl = "http://api.steamapis.com/market/item/570/"
# api = "?api_key="

f = open("selling_items.txt", "r+", encoding='unicode_escape')
total = 0
w = open("selling_prices.txt", "r+")
count = 0
appId = 570


for line in f:
    print(line)
    if line.__contains__("Dota 2 Trading Card"):
        appId = "753"
        item = "570-{0}".format(line)
        item = item.replace(" Dota 2 Trading Card", "")
    elif line.__contains__("The Steam Winter Sale - 2018 Profile Background"):
        appId = "753"
        item = "991980-{0}".format(line)
        item = item.replace(" The Steam Winter Sale - 2018 Profile Background", "")
    elif line.__contains__("Project CARS 2 Trading Card"):
        appId = "753"
        item = "378860-{0}".format(line)
        item = item.replace(" Project CARS 2 Trading Card", "")
    elif line.__contains__("Subnautica"):
        appId = "264710"
        item = line.replace(" Subnautica", "")
    elif line.__contains__("Dota 2"):
        item = line.replace(" Dota 2", "")
        appId = "570"
    item = item.replace("\'", "%27")
    item = item.replace(" ", "%20")
    url = baseUrl + appId
    url = url + secondUrl
    url = url + item
    url = url.strip()
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
w.writelines("\n\n\nTotal Price: " + total.__str__() + "  TL \n")

