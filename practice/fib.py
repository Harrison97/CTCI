import doctest

# A Naive recursive solution
# for Rod cutting problem
import sys

# A utility function to get the
# maximum of two integers
def max(a, b):
    return a if (a > b) else b

# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces
def cutRod(price, n):
    """
    >>> cutRod([1, 5, 8, 9, 10, 17, 17, 20], 8)
    22
    """
    if(n <= 0):
        return 0
    max_val = -sys.maxsize-1

    # Recursively cut the rod in different pieces
    # and compare different configurations
    for i in range(0, n):
        max_val = max(max_val, price[i] +
                      cutRod(price, n - i - 1))
    return max_val

# Driver code
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", cutRod(arr, size))

# This code is contributed by 'Smitha Dinesh Semwal'

# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod_DP(price, n):
    """
    >>> cutRod_DP([1, 5, 8, 9, 10, 17, 17, 20], 8)
    22
    """
    val = [0 for x in range(n+1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val

    return val[n]

# Driver program to test above functions
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))

# This code is contributed by Bhavya Jain

doctest.testmod()
