import requests
from bs4 import BeautifulSoup


URL = "https://www.johnlewis.com/ruark-mrx-bluetooth-wi-fi-connected-wireless-speaker/soft-grey/p3645548"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}

request = requests.get(URL)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

print(string_price)
