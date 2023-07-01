# Python program for the above approach

# Function to find the total number of
# ways to represent N as the sum of
# integers over the range [1, K]
def NumberOfways(N, K):

	# Initialize a list
	dp = [0] * (N + 1)
	
	# Update dp[0] to 1
	dp[0] = 1
	
	# Iterate over the range [1, K + 1]
	for row in range(1, K + 1):
	
		# Iterate over the range [1, N + 1]
		for col in range(1, N + 1):
		
			# If col is greater
			# than or equal to row
			if (col >= row):
			
				# Update current
				# dp[col] state
				dp[col] = dp[col] + dp[col - row]
				
				
	# Return the total number of ways
	return(dp[N])

# Driver Code

N = 40     ## S string length (when T≥S  both parmeters N an K should be the string length, when T<S, N=S and K=T) 
K = 2      ## T total elements (default, script shows ways to sum to 40 from when T=2)

print(NumberOfways(N, K))
