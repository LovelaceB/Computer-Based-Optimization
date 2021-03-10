#Ben Lovelace
#DASE 4570 
#Project 2

import math
import numpy
import time

#trig function given to us to find the mins and maxs
def trigFuntion(x):
	y = math.sin(5*x)/x
	return y

#function to calculate slope 
def slope(x1,y1,x2,y2):
	z = (y2-y1)/(x2-x1)
	return z

# gradient descent function that iterates through input interval in .001 steps and 
# calculates slope at each iteration
def gradientDescent(leftInterval, rightInterval):
	previousSlope = 0
	maxList = []
	minList = []
	globalMax = 0
	globalMin = 0
	for x in numpy.arange(leftInterval, rightInterval,.001):
		x2 = x + .001
		y1 = trigFuntion(x)
		y2 = trigFuntion(x2)
		if y2 > globalMax:
			globalMax = y2
		if y2 < globalMin:
			globalMin = y2
		currentSlope = slope(x,y1,x2,y2)
		if currentSlope <= 1e-1 and currentSlope >= -1e-1:
			currentSlope = 0
		if currentSlope == 0 and previousSlope>0:
			maxList.append([x,y1])
		if currentSlope == 0 and previousSlope<0:
			minList.append([x,y1])
		previousSlope = currentSlope
	return maxList, minList, globalMax, globalMin

# calling all of the functions 
begin = time.perf_counter()
sho = gradientDescent(-10,10)
print("Max List: ", sho[0])
print("Min List: ", sho[1])
print("Global max: ", sho[2])
print("Global min: ", sho[3])
end = time.perf_counter()
time1 = end - begin
print("time to run gradient descent", time1)

