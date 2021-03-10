
#Ben Lovelace
#DASE 4570
#Professor Michael
import time
vals_Items1 = [(24,12),(13,7),(23,11),(15,8),(16,9)]
vals_Items2 = [(825594,382745),(1677009,799601),(1676628,909247),(1523970,729069),(943972,467902),(97426,44328),(69666,34610),(1296457,698150),(1679693,823460),(1902996,903959),(1844992,853665),(1049289,551830),(1252836,610856),(1319836,670702),(953277,488960),(2067538,951111),(675367,323046),(853655,446298),(1826027,931161),(65731,31385),(901489,496951),(577243,264724),(466257,224916),(369261,169684)]

#function to create powerset
def powerset(inlist):
	result = [[]]
	for x in inlist:
		newsubsets = [subset + [x] for subset in result]
		result.extend(newsubsets)
	return result

#brute force funtion to find optimal solution
def bruteForce(inputList,maxCapacity):
	knapsack = []
	bestWeight = 0
	bestVal = 0
	for contentSelection in powerset(inputList):
		setVal = sum([e[0] for e in contentSelection])
		setWeight = sum([e[1] for e in contentSelection])
		if setVal > bestVal and setWeight<=maxCapacity:
			bestVal = setVal
			bestWeight = setWeight
			knapsack = contentSelection
	return knapsack

# function to format optimal solution into 1's and 0's 
def outputList(chosenKnapsack, itemsList):
	printedList = []
	for index1 in itemsList:	
		for index2 in chosenKnapsack:
			if index1 == index2:
				printedList.append(1)
				break
		if index1 != index2:
			printedList.append(0)

	return printedList

begin = time.perf_counter()
optimal1 = bruteForce(vals_Items1,26)
end = time.perf_counter()
time1 = end - begin
print(optimal1)
print("time to run knapsack 1", time1)
testList1 = outputList(optimal1, vals_Items1)
print("optimal solution knapsack 1", testList1)
with open('knapsack1_solution.txt', 'w') as filehandle:
   for listitem in testList1:
       filehandle.write('%i\n' % listitem)
start2 = time.perf_counter()
optimal2 = bruteForce(vals_Items2,6404180)
end2 = time.perf_counter()
time2 = end2 - start2
print(optimal2)
print("time to run knapsack 2", time2)
testList2 = outputList(optimal2, vals_Items2)
print("optimal solution knapsack 2", testList2)
with open('knapsack2_solution.txt', 'w') as filehandle:
   for listitem in testList2:
       filehandle.write('%i\n' % listitem)
