import sys
import timeit
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
	if low < high:
		pi = func2(arr, low, high)
		func1(arr, low, pi-1)
		func1(arr, pi + 1, high)
		
def func2(array, start, end):
	p = array[start]
	low = start + 1
	high = end
	while True:
		while low <= high and array[high] >= p:
			high = high - 1
		while low <= high and array[low] <= p:
			low = low + 1
		if low <= high:
			array[low], array[high] = array[high], array[low]
		else:
			break
	array[start], array[high] = array[high], array[start]
	return high
	

# Exercise 2.2
def main():
    with open("ex2.json", "r") as numFile:
    #with open("ex2.5.json", "r") as numFile: # Comment out the above line and uncomment this line to view the graph for Exercise 2.5
        content = json.load(numFile)
    
    range_x = []
    range_y = []
    for i in content:
        range_x.append(len(i))
        range_y.append(timeit.timeit(lambda: func1(i, 0, (len(i)-1)), number=1))
    
    plt.plot(range_x, range_y)
    plt.title("Timing results of the ex2.json file")
    #plt.title("Timing results of the ex2.5.json file") # Comment out the above line and uncomment this line to view the graph for Exercise 2.5
    plt.xlabel("Input size")
    plt.ylabel("Time Taken (seconds)")
    plt.show()
  
  

if __name__ == '__main__':
    main()