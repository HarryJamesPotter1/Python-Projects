import requests
from bs4 import BeautifulSoup

SIGNS = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagitarius','Capricorn','Aquarius','Pisces']
URL = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={0}"

print("The Horscopes are: ")
print(", ".join(SIGNS))

sign = " "

while sign not in SIGNS:
    sign = input("Please Enter your Horscope: ").strip()

index = SIGNS.index(sign) + 1
url = URL.format(str(index))
response = requests.get(url)
html = response.content
#print(html)
soup = BeautifulSoup(html, "html.parser")
#print(soup)
paragraph = soup.find("p")
print(paragraph.text)