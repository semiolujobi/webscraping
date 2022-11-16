from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from twilio.rest import Client

import keys2

client = Client(keys2.accountSID, keys2.authToken)
myCellPhone =  "+12816100097"
twilionumber = "+14635837137"


url = 'https://crypto.com/price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url,headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
#title = soup.title
#print(title.text)
tablerows = soup.findAll("tr")
#print(tablerows[1].text)

for row in tablerows[1:6]:
    td = row.findAll("td")
    name = td[2].text
    price_list = td[3].text.split('$')
    price = price_list[1]
    percent_change = td[3].text[-6:]
    former_price = float(((float(price.replace(',','')))*(float(percent_change.replace('+','').replace('%',''))/100)) + (float(price.replace(',',''))))

    print(f"Currency Name: {name}")
    print(f"Price: {price}")
    print(f"Daily Percent Change: {percent_change}")
    print(f"Former Price: {former_price:.2f}")
    print()

for row in tablerows[1:2]:
    td = row.findAll("td")
    name = td[2].text
    price_list = td[3].text.split('$')
    price = int(price_list[1].replace(',','')[:3])
    if price < 400000:
        BTCtextmessage = 'BTC is below $40k'
        text1 = client.messages.create(to=myCellPhone, from_= twilionumber, body=BTCtextmessage)
        print(text1)

    if price < 3000:
        ETHtextmessage = 'ETH is below $3k'
        text2 = client.messages.create(to=myCellPhone, from_= twilionumber, body=ETHtextmessage)
        print(text2)

