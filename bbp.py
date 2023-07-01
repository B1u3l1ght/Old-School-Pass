# Python3 program for the above approach

# Function to print the values stored
# in vector arr
def printVector(arr):
	if len(arr) != 0:
		arr = arr[::-1]
		for i in range(len(arr)):
			print(arr[i], end=" ")
		print()
# Recursive function to print different
# ways in which N can be written as
# a sum of at 2 or more positive integers
def findWays(arr, i, n):

	# If n is zero then print this
	# ways of breaking numbers
	if (n == 0):
		printVector(arr)

	# Start from previous element
	# in the representation till n
	for j in range(i, n + 1):

		# Include current element
		# from representation
		arr.append(j)

		# Call function again
		# with reduced sum
		findWays(arr, j, n - j)

		# Backtrack to remove current
		# element from representation
		del arr[-1]
		
# Driver Code
if __name__ == '__main__':

	# Given sum N
	n = 9

	# To store the representation
	# of breaking N
	arr = []

	# Function Call
	findWays(arr, 1, n)

# This code is contributed by mohit kumar 29
