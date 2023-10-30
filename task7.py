from multiprocessing import Pool
import random
import math

def estimate(points:int)->int:
    count_inside=0
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if (math.pow(x,2)+math.pow(y,2)<=1):
        count_inside+=1
    return count_inside

def multiprocessing(points:int)->int:
    with Pool(processes=4) as p:
        result=p.map(estimate,[(point) for point in range(points)[1:]])
    return sum(result)*4/points

if __name__=="__main__":
    points=int(input("Input number of points:"))
    print(multiprocessing(points))