import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("http://www.rajinikanthjokes.com/")


soup = BeautifulSoup(response.text, "html.parser")

para = soup.find_all('p')

with open("jokes.csv", "w") as csvFile:
  csv = writer(csvFile)
  for p in para:
    csv.writerow([p.get_text().encode('utf-8')])
