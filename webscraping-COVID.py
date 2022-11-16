# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url,headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
table_rows = soup.findAll("tr")

state_worst_death = ''
state_best_death = ''
high_death_ratio = 0.0
low_death_ratio  = 100.0

state_best_test = ''
state_worst_test = ''
high_test_ratio = 0.0
low_test_ratio = 100.0

for row in table_rows[2:51]:
    td = row.findAll("td")
    number = td[0].text
    state_name = td[1].text
    total_cases = int(td[2].text.replace(",",""))
    total_deaths = int(td[4].text.replace(",",""))
    total_tests = int(td[10].text.replace(",",""))
    population = int(td[12].text.replace(",",""))
    
    death_rate = round((total_deaths/total_cases)*100,2)
    test_rate = round((total_tests/population)*100,2)
    if death_rate > high_death_ratio:
        state_worst_death = state_name
        high_death_ratio = death_rate
    
    if death_rate < low_death_ratio:
        state_worst_death = state_name
        low_death_ratio = death_rate
    
    if test_rate > high_test_ratio:
        state_worst_death = state_name
        high_test_ratio = test_rate

    if test_rate < low_test_ratio:
        state_worst_death = state_name
        low_test_ratio = test_rate

    print(f"State: {state_name}")
    print(f"Death rate: {death_rate}%")
    print()
    print()
    print()
    #input()

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")
