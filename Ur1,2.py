import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'http://mfd.ru/currency/?currency=USD'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

dates = []
rates = []

table = soup.find('table',{'class':'mfd-table mfd-currency-table'})
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    if len(cols) > 0:
        date = cols[0].text.strip()
        rate = cols[1].text.strip()
        dates.append(date)
        rates.append(float(rate.replace(',', '.')))

plt.plot(dates, rates)
plt.xlabel('Date')
plt.ylabel('USD/RUB')
plt.title('USD/RUB Exchange Rate')
plt.show()