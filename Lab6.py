from bs4 import BeautifulSoup as bs
import requests as rq
from collections import Counter
from lxml import html
from string import punctuation
req = rq.get("https://news.obozrevatel.com/travel/location/top-10-izvestnyih-lokatsij-v-mire-kotoryie-turistyi-chasche-vsego-otmechayut-v-instagram-foto.htm")
sp = bs(req.text, 'html.parser')
lnks = [a['href'] for a in sp.find_all('a')]
text = (''.join(s.findAll(text=True))for s in sp.findAll('p'))
cntr = Counter(x.rstrip(punctuation).lower() for y in text for x in y.split())
#Слова
print('Подсчёт разных слов>>', cntr.most_common())
#Картинки
images = sp.find_all('img')
print ('Изображений>>', len(images))
#Ссылки
print('Ссылки>>')
for z in lnks:
    print(z)
    count = len(lnks)
print('Сcылок>>{}'.format(count))
