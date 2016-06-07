##############################################
#   File:       ProjectEulerB.py
#   Desc:       Solution to Problems 11 to 20
#   Created by: Sujan Subendran
##############################################

# find highly divisible triangular numbe
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

# find first 10 digits of sum for one hundred 50 digit numbers
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

# Longest Collatz sequence under 1 million
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
