##############################################
#   File:       ProjectEulerB.py
#   Desc:       Solution to Problems 11 to 20
#   Created by: Sujan Subendran
##############################################

# 12: find highly divisible triangular numbe
def findHighlyDivisibleTriangleNum(divisors):
    count = 0
    triangleNum = 0
    i = 1
    while count <= divisors:
        triangleNum += i
        i += 1
        count = countFactors(triangleNum)
    return triangleNum

def countFactors(num):
    factorList = []
    for i in range(1, int(num**0.5) + 1): 
        if num % i == 0:
            factorList.append(i)
            factorList.append(num // i)
    return len(factorList)

# print(findHighlyDivisibleTriangleNum(500))

# 13: find first 10 digits of sum for one hundred 50 digit numbers
def findSumOfNumberList(digits):
    numArr = []
    total = 0
    with open('dataset/problem13.txt') as f:
        for line in f:
            numArr.append(int(line))
    for num in numArr:
        total += num
    total //= 10 ** (len(str(total)) - digits)
    return total

# print(findSumOfNumberList(10))

# 14: Longest Collatz sequence under 1 million
def findLongestCollatzSequence(maxValue):
    collatz = [0, 0]
    for i in range(maxValue - 1, 499999, -1):
        num = i
        chain_length = 1
        while(num != 1):
            if num % 2 == 0:  # even
                num //= 2
            else:             # odd
                num = num * 3 + 1
                chain_length += 1
    if chain_length > collatz[1]:
        collatz[0] = i
        collatz[1] = chain_length
        print(collatz)
    return collatz[0]

# print(findLongestCollatzSequence(1000000))

# 16: Sum of digits of 2^1000
def sumOfDigits(num):
    digits = str(num)
    sumDigits = 0
    for i in digits:
        sumDigits += int(i)
    return sumDigits

# print(sumOfDigits(2**1000))

# 18: maximum path sum (using dynamic programming)
def findMaxPathSum():
    arr = []
    with open("dataset/problem18.txt") as f:
        for line in f:
            numbers = list(map(int, line.split()))
            arr.append(numbers)
    
    for i in range(len(arr) - 2, -1, -1):
        for j in range(0, len(arr[i]), 1):
            arr[i][j] += max(arr[i + 1][j], arr[i + 1][j + 1])
            # print("{0},{1}: ".format(i, j) + str(arr[i][j]))

    return arr[0][0]

# print(findMaxPathSum())

# 549: Naive Divisibility of factorials
cache = {}
def calcS(n):
    sumS = 0
    for i in range(2, n + 1, 1):
        sumS += calcSmallestNumFactorial(i)
        # print(i)
    return sumS

def calcSmallestNumFactorial(i):
    fact, m = 1, 1
    while(fact % i != 0):
        m += 1
        if m in cache:
            fact = cache[m]
        else:
            fact *= m
            cache.update({m: fact})
    return m
