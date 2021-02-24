import requests
from bs4 import BeautifulSoup
import re


URL = "https://www.johnlewis.com/sony-ht-st5000-wi-fi-bluetooth-nfc-sound-bar-with-wireless-subwoofer-high-resolution-audio-dolby-atmos-chromecast-multiroom/p3234220"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}

request = requests.get(URL)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

pattern = re.compile(r"(\d+,?\d+\.\d+)")
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(",", "")
price = float(without_commas)

print(price)
