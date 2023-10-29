import multiprocessing  
import os
import requests
from bs4 import BeautifulSoup 

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Referer": "https://www.bing.com/",
}

def download(src:str)->None:
    response=requests.get(src)
    numbers = format(range(0,1000)).zfill(4)
    if not os.path.exists(f"dataset"):
        os.mkdir(f"dataset")
    with open(os.path.join("dataset",f"{numbers}.jpg","wb")) as f:
        f.write(response.content)

def create_list(urls:list)->list:
    list=[]
    src_list=[]
    for item in urls:
        response=requests.get(item,headers=HEADERS)
        soup=BeautifulSoup(response.text,'lxml')
        img=soup.findAll('img')
        list+=img
    print(list)
    for content in list:
        src=content.get('src')
        src_list+=src
    return src_list


if __name__=="__main__":
    num=input("Input numbers of url: ")
    for item in range(int(num)):
        urls=[]
        url=input("Input url: ")
        urls.append(url)
    list=create_list(urls)
    with multiprocessing.Pool(processes=4) as p:
        p.map(download,list)
