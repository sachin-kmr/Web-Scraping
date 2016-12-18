import requests
from bs4 import BeautifulSoup as BS
import json

url = 'https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order'
data = requests.get(url)
soup = BS(data.text)

table = soup.find_all('table')
t = table[2]
tr = t.find_all('tr')

country = []

for ix in range(1, len(tr)):
    c_data = {}
    
    td = tr[ix].find_all('td')
    a = td[0].find_all('a')[0] #city names in 0
    
    c_data['city'] = a.text
    
    #print a['href'] #can't be accessed with . use []
    #country names in table[1]
    n = td[1].find_all('a')[0]
    
    c_data['country'] = n.text
    country.append(c_data)

print country[0:2]

data = {'data' : country}
#print data

y = json.dumps(data)

f = open('countries-and-capitals.json', 'w')
f.write(y)
f.close()

