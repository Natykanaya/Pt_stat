from bs4 import BeautifulSoup as bs
import requests
from urllib import request
#urllib.request
import urllib.request

def fcbook():
    r = requests.get("https://www.facebook.com/ProgresstechUA/")
    soup = bs(r.text, "html.parser")
    podsp = soup.find_all('div', class_="_4bl9")
    num_list = []

    podsp_p=podsp[2]
    subs=podsp_p.get_text()
    for word in subs:
        if word.isnumeric():
            num_list.append(word)
    #убираем скобки списка и выводим цифру
    subscribers=''.join(num_list)

    return subscribers

def inst():

    session = requests.Session()
    r = session.get("https://www.instagram.com/progresstech.ua/?hl=ru")#, headers=headers)
    soup = bs(r.text, "html.parser")
    #print(soup)
    podpis = soup.find('meta',property="og:description")
    podp=podpis["content"]
    podpp=podp.split()
    ret = podpp[0]
    return ret

def vk():
    r=requests.get("https://vk.com/progresstech_ukraine")
    soup = bs(r.text, "html.parser")
    # f = open('vk.html', 'wb')
    # f.write(soup.encode('utf-8'))
    # print("writing")
    # return f
    #print(soup)


    tag=soup.find_all('span',_class='header_label fl_l')
    for i in tag:
        print(i)

    # Скачиваешь сначала страницу
    #url = 'https://vk.com/progresstech_ukraine'

    #html = urllib.urlopen(url).read()
    # Теперь записываешь файл
    # f = open('vk.html', 'w')
    #
    # f.write(html)
    # print("writing")

vk()