# Python3 Program to find n'th fibonacci Number in
# with O(Log n) arithmetic operations
MAX = 10**7

# Create an array for memoization
f = [0] * MAX

# Returns n'th fibonacci number using table f[]
def fib(n) :
	# Base cases
	if (n == 0) :
		return 0
	if (n == 1 or n == 2) :
		f[n] = 1
		return (f[n])

	# If fib(n) is already computed
	if (f[n]) :
		return f[n]

	if( n & 1) :
		k = (n + 1) // 2
	else :
		k = n // 2

	# Applying above formula [Note value n&1 is 1
	# if n is odd, else 0.
	if((n & 1) ) :
		f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
	else :
		f[n] = (2*fib(k-1) + fib(k))*fib(k)

	return f[n]


# Driver code
n = 100
print(fib(n))


# This code is contributed by Nikita Tiwari.
