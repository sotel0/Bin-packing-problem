import math

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    
#maybe not need counter
def find_solution(sizes):
	mergeSort(sizes)
	measurements = traverse(sizes)
	#print (measurements)
	#print(sizes)
	cutoff = len(sizes)
	##print(cutoff)

	cutoff = (int)(math.sqrt(cutoff))
	#find the average length of xTotal and yTotal and use it here instead of measurements[0]
	avgXandY = (measurements[0]+measurements[1])/2
	##print (avgXandY)

	avgSize = (avgXandY)/len(sizes)
	#print("avgSize: ")
	#print(avgSize)

	avgCol = avgSize*cutoff

	#printing the set farthest y value
	#print (avgCol)
	#print(len(sizes))
	t_y = 0
	t_x = 0
	#counter = 0
	outerIndexX = 0
	biggest = 0
	res = []
	sizes.reverse()
	for i in range(0,len(sizes)):
		
		if (sizes[i][0] > biggest):
			biggest = sizes[i][0]


		res.append((t_x, t_y))
		t_y += sizes[i][1]
		#counter = counter + 1

		if (t_y >= avgCol):
			counter = 0
			t_y = 0
			outerIndexX += biggest
			t_x = outerIndexX
			biggest = 0
	#printing the farthest x value
	#print (res[len(sizes)-1][0])
	return res
'''counter % cutoff == 0 or''' 

def traverse(blist):
	
	xTotal = 0
	yTotal = 0
	for i in range(0, len(blist)):
		xTotal += blist[i][0]
		yTotal += blist[i][1]

	res = [xTotal,yTotal]
	return res
