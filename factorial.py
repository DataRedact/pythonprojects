# The factorial of the integer , written , is defined as:

# Calculate and print the factorial of a given integer.

# For example, if , we calculate  and get .

# Function Description

# Complete the extraLongFactorials function in the editor below. It should print the result and return.

# extraLongFactorials has the following parameter(s):

# n: an integer
# Note: Factorials of  can't be stored even in a  long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

# We recommend solving this challenge using BigIntegers.

def extraLongFactorials(n):
    allNums = []
    for i in range(n+1):
        allNums = [i, *allNums]
    factorial = []
    current = allNums[0]
    del allNums[0]
    for i in range(n):
        if i == len(allNums)-1:
            break
        temp= current*allNums[i]
        current = temp
    print(current)
