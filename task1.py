from multiprocessing import Pool
import numpy as np

def sum_el(rows:int,columns:int,matrix:list)->int:
    matrix=np.array_split(matrix,rows)
    with Pool(processes=4) as p:
        result=p.map(sum,matrix)
    return sum(result)

if __name__=="__main__":
    rows=int(input("Input rows:"))
    columns=int(input("Input columns:"))
    array=[]
    for i in range(rows):
        row=[]
        for j in range(columns):
            el=int(input(f"Input value of cell ({i},{j}):"))
            row.append(el)
        array.append(row)
    print(sum_el(rows,columns,array))
   




    
