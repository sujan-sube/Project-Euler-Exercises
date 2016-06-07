# sum of multiples of 3 and 5 that are below a number
def sumMultiples3and5(belowNum):
  sumMultiples = 0
  for i in range(belowNum):
    sumMultiples += i if (i % 3 == 0 or i % 5 == 0) else 0
  return sumMultiples

# print(sumMultiples3and5(1000))

# naive : calc sum of even fibonancci numbers
def evenFibonacciNums(maxValue):
  sumFib = 0
  i, j = 0, 1
  while(i < maxValue):
    term = i + j
    i, j = j, term
    sumFib += term if(term % 2 == 0) else 0
    # print(term)
  return sumFib

# print(evenFibonacciNums(4000000))

# naive: largest prime factor
def findLargePrimeFactor(num):
  largestPrime = 1
  for i in range(1, num + 1):
    if(num % i == 0):
      if(isPrime(i)):
        print(i)
        largestPrime = i
  return largestPrime

def isPrime(num):
  flag = True
  for i in range(2, int(num**0.5 + 1)):
    if(num % i == 0): 
      flag = False 
      break
  return flag

# print(findLargePrimeFactor(600851475143))

# better solution: largest prime factor
def findLargestPrimeFactor(num):
  while(num % 2 == 0):
    num /= 2
    fact = 2
  for i in range(3, 775147, 2):
    while(num % i == 0):
      num /= i
      fact = i
  if(num > 2):
    fact = num
  return fact

# print(findLargestPrimeFactor(600851475143))

# find largest palimdrome from product of two 3 digit numbers
def findLargestPalimdrome():
  palimdrome = []
  for i in range(999, 100, -1):
    for j in range(999, 100, -1):
      prod = i * j
      if(isPalimdrome(prod)):
        palimdrome.append(prod)
  return max(palimdrome)

def isPalimdrome(num):
  digits = str(num)
  reverse_digits = digits[::-1]
  if(digits == reverse_digits):
    return True
  else:
    return False

# print(findLargestPalimdrome())

# find smallest number divisible by 1 to 20
def findSmallestDivisible():
  for num in range(2520, 2432902008176640000, 2520):
    # print(num)
    for i in range(2, 20, 1):
      if(num % i != 0):
        isSmallest = False
        break
      else:
        isSmallest = True
    if(isSmallest):
      return num

# print(findSmallestDivisible())

# verification: find smallest number divisible by 1 to 20
def verifyFindSmallestDivisibleNum():
  num = 232792560
  for i in range(20, 1, -1):
    if(num % i != 0):
      print(str(i) + ' is not divisible')
    else:
      print(i)

# Sum square difference
def sumSquareDifference(num):
  sumSquare = 0
  squareSum = 0
  for i in range(1, num + 1, 1):
    sumSquare += i ** 2
    squareSum += i
  squareSum **= 2
  return (squareSum - sumSquare)

# print(sumSquareDifference(100))


# Find 10001st prime number
import sys
def findPrimeNumber(num):
  counter = 0
  for i in range(2, sys.maxsize):
    if isPrimeNum(i):
      counter += 1
    if counter == num:
      return i

def isPrimeNum(num):
  flag = True
  for i in range(2, int(num**0.5 + 1)):
    if(num % i == 0): 
      flag = False 
      break
  return flag

# print(findPrimeNumber(10001))

# Find Largest product in series
def findLargestAdjacentProduct(numArr, subset):
  numSets = len(numArr) - subset + 1
  productList = []
  for i in range(numSets):
    product = 1
    for j in numArr[i:i + subset]:
      product *= int(j)
    productList.append(product)
  return max(productList)

# numArr = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
# print(findLargestAdjacentProduct(numArr, 13))

def findSpecialPythagoreanTriplet():
  for b in range(0, 1001):
    for c in range(0, 1001):
      calc = (1000 - b - c)**2 + b**2 - c**2
      if calc == 0:
        a = 1000 - b - c
        if a**2 + b**2 == c**2 and c > b and b > a:
          return a * b * c

# print(findSpecialPythagoreanTriplet())

# Find sum of primes below a number
def findPrimeNumberSumBelowNum(num):
  sumTotal = 0
  for i in range(2, num):
    if isPrimeNum(i):
      sumTotal += i
  return sumTotal

def isPrimeNumber(num):
  flag = True
  for i in range(2, int(num**0.5 + 1)):
    if(num % i == 0): 
      flag = False 
      break
  return flag

# print(findPrimeNumberSumBelowNum(2000000))
