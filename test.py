from bs4 import BeautifulSoup as bs
import requests
from urllib import request

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


    myUrl = 'https://www.facebook.com/ProgresstechUA/'
    otvet = request.urlopen(myUrl)
    mytext1 = otvet.readlines()
    filetxt = open('textt.txt', 'wb')
    for line in mytext1:
        filetxt.write(line)
    filetxt.close()


    return subscribers

def inst():
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    # }
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
    print("try")
    r=requests.get("https://vk.com/progresstech_ukraine")
    soup = bs(r.text, "html.parser")

    myUrl = 'https://vk.com/progresstech_ukraine'
    otvet = request.urlopen(myUrl)
    mytext1 = otvet.readlines()
    filetxt = open('textt.txt', 'wb')
    for line in mytext1:
        filetxt.write(line)
    filetxt.close()


    #print (soup)

print(fcbook())