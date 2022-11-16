
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


random_chapter = random.randint(1,21)
if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)
webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'
print(webpage)
#counter = 0

#for i in range(1,22):
 #   webpage = 'https://ebible.org/asv/JHN' + str(counter)
  #  if i < 10:
   #     webpage = 'https://ebible.org/asv/JHN' + '0' + str(counter)
    #print(webpage)
    #counter += 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll('div', class_='main')

verse_list = []

for verse in page_verses:
    #print(verse)
    verse_list = verse.text.split(".")

myverse = 'Chapter' + random_chapter + 'Verse:' + random.choice(verse_list[:len(verse_list)-2])
print(myverse)