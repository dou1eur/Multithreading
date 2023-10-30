from multiprocessing.pool import ThreadPool
import os
import requests
from bs4 import BeautifulSoup 

#the code doesn't work
#will it work someday...
"""
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Referer": "https://www.bing.com/",
}

def create_list(urls:list)->list:
    list_src=[]
    for url in urls:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "lxml")
        images = soup.find_all("img")
    for item in images:
        src=item["src"]
        list_src.append(src)
    print(list_src)
    return list_src


def download(url:str)->None:
    if not os.path.exists("dataset"):
        os.mkdir("dataset")
    response=requests.get(url)
    filename=url.split('/')[-1]
    with open(os.path.join(filename,"wb")) as f:
        f.write(response.content)
    

def multiprocessing(urls:list)->list:
    with ThreadPool(processes=4) as p:
        result=p.map(download,[(url) for url in urls])
    p.close()
    p.join()
    return result

if __name__=="__main__":
    num=input("Input numbers of url: ")
    for item in range(int(num)):
        urls=[]
        url=input("Input url: ")
        urls.append(url)
    multiprocessing(create_list(urls))
"""
