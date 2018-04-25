from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list3']

# spider 1

def get_links_from(channel,pages,who_sells=0):
    # http://bj.58.com/diannao/0/pn3/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        item_link = link.get('href').split('?')[0]
        url_list.insert_one({'url':item_link})
        print(item_link)

get_links_from('http://bj.58.com/tongxunyw/',2)


