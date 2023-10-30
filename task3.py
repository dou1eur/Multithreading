from multiprocessing import Pool

def search(keyword:str,filename:list)->None:
    with open(f"{filename}.txt",'r',encoding='utf-8') as f:
        strs=f.readlines()
        count_keyword=0
        for line in strs:
            if keyword in line:
                count_keyword+=1
        if count_keyword>0:
            print(f"{keyword} founded in {filename}")

def multiprocessing(keyword:str,filenames:list)->list:
    with Pool(processes=4) as p:
        result=p.starmap(search,[(keyword,filename) for filename in filenames])
        return result

if __name__=="__main__":
    keyword=input("Input keyword:")
    num=int(input("Input number of files:"))
    files=[]
    for item in range(num):
        file=input("Input file: ")
        files.append(file)
    print(files)
    multiprocessing(keyword,files)
    