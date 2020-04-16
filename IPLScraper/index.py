import requests
from bs4 import BeautifulSoup
from csv import writer

page = requests.get("https://www.iplt20.com/stats/2019")

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all('table', class_='standings-table')

tds = []
for row in table:
    for r in row.find_all('tr'):
        position = list((r.find_all('td')))
        Row = []
        for row in position:
            Row.append(row.get_text().strip())

        tds.append(Row)


with open("ipl19.csv", "w") as csvFile:
    csv = writer(csvFile)
    csv.writerow(["position", "team", "Pid", "Won", "Lost",
                  "Tied", "N/R", "Net RR", "For", "Against", "Pts", "Form"])

    for row in tds:

        csv.writerow(row)
