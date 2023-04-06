import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

url = 'http://mfd.ru/currency/?currency=USD'
response = requests.get(url)
x = []
y = []
dates = []
rates = []

soup = BeautifulSoup(response.text, 'html.parser')
rows = soup.find_all(class_="mfd-table mfd-currency-table")

for row in rows:
    if row.find_all(class_="mfd-table mfd-currency-table") is not None:
        dates.append(row.text)

elem = []

for row in dates:
    elem = str(row).split()

len1 = len(elem)

for i in range(len1 - 1, 3, -4):
    x.append(str(elem[i - 2]))
    y.append(float(str(elem[i - 1])))

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set(title='Курс доллара', xlabel='Дата', ylabel='Курс')
ax.xaxis.set_major_locator(MaxNLocator(4))
plt.grid(True)
plt.show()