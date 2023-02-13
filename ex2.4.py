import sys
import timeit
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def Qsort(array):
    
    if len(array) <=1:
        return array
    
    midpoint = len(array) // 2
    pivot = array[midpoint]
    lower = []
    middle = []
    upper = []
    for i in array:
        if(i < pivot):
            lower.append(i)
        elif( i > pivot):
            upper.append(i)
        else:
            middle.append(i)
    result = Qsort(lower) + middle + Qsort(upper)
    return result
    
	
def main():
    with open("ex2.json", "r") as numFile:
        content = json.load(numFile)
    
    range_x = []
    range_y = []
    for i in content:
        range_x.append(len(i))
        range_y.append(timeit.timeit(lambda: Qsort(i), number=1))
    
    plt.plot(range_x, range_y)
    plt.title("Timing results of the improved ex2.json file")
    plt.xlabel("Input size")
    plt.ylabel("Time Taken (seconds)")
    plt.show()
  

if __name__ == '__main__':
    main()