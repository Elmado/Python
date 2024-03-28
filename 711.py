#711 game, sum and mutliplicaiton must be equal to 711
# 7.11$ has these factors 79, 3**2, 2 ** 6 , 5 ** 6
#first i will create a function to generate all possible vectors of power for  given factor
#for example there 
FactorsArray = [79,3,2,5] #not used, this is just a reminder of the diveders of 7.11$

def PowerVector(TargetFactor):
	if TargetFactor == 79:
		TargetPower = 1
	elif TargetFactor == 3:
		TargetPower = 2
	elif TargetFactor == 2:
		TargetPower = 6
	elif TargetFactor == 5:
		TargetPower = 6
	#else:
	#	print('Wrong choice, you need to choose between 79, 3, 2 or 5')
	#	exit()
	#print ('TargetFactor is ', TargetFactor, 'TargetPower is', TargetPower)
	
	VectorList = []
	#print (VectorList)
	for a1 in range(TargetPower+1):
		a2max = TargetPower - a1
		#print (a1)
		for a2 in range(a2max+1):
			a3max = TargetPower - a1 - a2
			#print(a1,a2)
			for a3 in range(a3max+1):
				a4 = TargetPower- a1- a2 - a3
				NewVector = [a1,a2,a3,a4]
				#print (NewVector)
				VectorList.append([a1,a2,a3,a4])
				#print (VectorList)
	return (VectorList)

import numpy as np

#now this functions tranforms the array of powers, to an array of Base**Powers,
#eg. for array of powers [1,1,0,0]of the factor 3  this will return  an array[3,3,1,1]
def PoweredArray (array, factor):
		Resultarray = []
		for i in (array):
			Resultarray.append (factor ** i)
		return (Resultarray)

#print (PoweredArray([2,0,0,0],3)) #should return [9,1,1,1]

#now we will compile all the factor arrays to make one matrix of all factors
#once the matrix is creates, the functions finds out each itemprice
#and calculates the total bill (sum of all prices) and the mulitplicaiton of all prices

def PowerMatrix(array3,array2,array5):
	matrix = np.array([[79,1,1,1],PoweredArray(array3,3),PoweredArray(array2,2),PoweredArray(array5,5)])
	#Remember that 79 has only one power, so the only array for 79 is [79,1,1,1]
	prices = [1,1,1,1]
	TotalBill = 0
	MultiBill = 1
	for array in matrix:
		for i in range(4):
			prices[i] = prices[i] * array[i]
	#now that we have the prices, we can normalize them to $ and sum and multiply the bill
	for i in range(4): 
		prices[i] = prices[i]/100
		TotalBill = TotalBill + (prices[i])
		MultiBill = MultiBill * (prices[i])

	#print(matrix,'prices of the 4 items are',prices)
	#print ('total bill is', TotalBill)
	#print ('multiplication of the 4 items is', MultiBill)
	return ([prices,TotalBill])


#PowerMatrix ([0,1,1,0],[2,0,2,2],[0,2,2,2])

VectorThree = PowerVector(3)
VectorTwo = PowerVector(2)
VectorFive = PowerVector(5)

#now we will get the code to try all the possible combinations of arrays
attempt = 0
results = []
for vectors3 in VectorThree:
	for vectors2 in VectorTwo:
		for vectors5 in VectorFive:
			attempt = attempt +1 
			#print (attempt, vectors3,vectors2,vectors5)
			MatrixToCheck = PowerMatrix(vectors3,vectors2,vectors5)
			TotalToCheck = MatrixToCheck[1]
			#print ('checking', MatrixToCheck)

			if TotalToCheck == 7.11 :
				print ('found it. here are the prices',MatrixToCheck)
				results.append(MatrixToCheck)
print ('here are all the results', results)
				#continuing = input('type 0 to exit, 1 to continue')
				#try:
				# continuing == 1
				#except:
				#	print ('bye') 

#print (PowerVector (TargetFactor))

#for Factors in [3,2,5]:
#	print (Factors)
