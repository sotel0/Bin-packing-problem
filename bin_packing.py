# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Danny Kumpf and Isaac Sotelo
# Last Modified: February 17, 2016
# ----------------------------------------------

"""
BIN_PACKING_SOLUTION:
    We sorted the list of rectangles from smallest to largest. Then they were placed into columns until they reached a cuttoff limit and then a new column is started at the top. It is continued until the list is empty. Our cuttoff limit value is based on finding the average rectangle size using the total x and total y values. A traversing method was used to find these values. Which is then multiplied by the average number of rectangles per column. 
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement


"""

import math #used for the square root function

def mergeSort(alist): #sorts the list of tuples to be ordered from lowest to highest (x and y)
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
    
def findCutoff(sizes):

	measurements = traverse(sizes)					#Go through the list and return the total x and y values							

	avgCol = (int)(math.sqrt(len(sizes)))			#gets the average number of rectangles per column
	
	total = measurements[0]+measurements[1]
	avgXandY = (total)/2							#average value of the total x's and y's

	avgSize = (avgXandY)/len(sizes)					#average size of each rectangle

	cutoff = avgSize*avgCol							#the cutoff length of the column

	return cutoff

def find_solution(sizes): 

	table = {}										#keep track of the id of the rectangles and index it was originally at
	t_y = 0											#top left y coordinate
	t_x = 0											#top left x coordinate
	outerIndexX = 0									#keeps track of where the new column should start
	biggestX = 0									#temporary variable to find outerIndexX should be
	res = [0]*len(sizes)							#resulting list to return

	for i in range(0,len(sizes)):					#putting the id and Idex in a dictionary directly
		table[id(sizes[i])] = i

	mergeSort(sizes)								#ordering the list of rectangles

	cutoff = findCutoff(sizes)

	sizes.reverse()									#reverse the list so that the larger rectangles will be placed first

	for i in range(0,len(sizes)):				#find the coordinates for each rectangle
		
		if (sizes[i][0] > biggestX):			#find the biggest x value
			biggestX = sizes[i][0]

		coordinate = (t_x, t_y)

		realIndex = table[id(sizes[i])]			#get the index of the current rectangle by looking it up in the dictionary using the id
		
		res[realIndex] = coordinate  			#add the rectangle coordinates to the resulting list 

		t_y -= (sizes[i][1])					#update the y value to the y value of the current rectangle

		if (t_y <= (cutoff*(-1))):				#checks whether a new column needs to be started
			t_y = 0								#sets the y value back to zero
			outerIndexX += (biggestX)			#sets the start of the new column
			t_x = outerIndexX					
			biggestX = 0

	return res

def traverse(blist):  #returns each x and y value of the given list
	
	xTotal = 0
	yTotal = 0

	for i in range(0, len(blist)):	#go through the whole list
		xTotal += blist[i][0]		#add up all the x values
		yTotal += blist[i][1]		#add up all the y values

	res = [xTotal,yTotal]
	
	return res
