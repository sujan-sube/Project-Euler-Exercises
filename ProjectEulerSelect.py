from ProjectEulerA import *
from ProjectEulerB import *
import timeit 

# Dataset for Problem ID 8
DATASET_8 = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

solutionSet = {
    "1": [sumMultiples3and5, 1000],                     # sum of all multples of 3 or 5 below 1000
    "2": [evenFibonacciNums, 4000000],                  # sum of even fibonacci up to 4 million
    "3": [findLargestPrimeFactor, 600851475143],        # find largest prime factor
    "4": [findLargestPalimdrome],                       # product of two 3 digit numbers
    "5": [findSmallestDivisible],                       # find smallest number divisible by 1 to 20
    "6": [sumSquareDifference, 100],                    # sum square difference of first 100 natural numbers
    "7": [findPrimeNumber, 10001],                      # find 10001st prime number
    "8": [findLargestAdjacentProduct, DATASET_8, 13],   # find largest consecutive product in series
    "9": [findSpecialPythagoreanTriplet],               # find unique Pythagroean triplet
    "10": [findPrimeNumberSumBelowNum, 2000000],        # find sum of primes below 2 million
    "12": [findHighlyDivisibleTriangleNum, 500],        # find first triangular number with 500+ factors
    "13": [findSumOfNumberList, 10],                    # find first 10 digits of sum for one hundred 50 digit numbers
    "14": [findLongestCollatzSequence, 1000000],        # Longest Collatz sequence under 1 million
    "16": [sumOfDigits, 2**1000],                       # Sum of digits in 2^1000
    "18": [findMaxPathSum],                             # maximum path sum (using dynamic programming)
    "549": [calcS, 10**8]                               # Naive Divisibility of factorials (brute-force: would take years)
  }

def wrapper(func, args):
    start = timeit.default_timer()
    result = func(*args)
    print("Run Time: " + "{:9.5f}".format(timeit.default_timer() - start) + "s")
    return result

def selectSoln(solnId):
    funcAndArgs = solutionSet.get(str(solnId), 0)
    if funcAndArgs == 0:
        return "ID not found!"
    else:
        return wrapper(funcAndArgs[0], funcAndArgs[1:])

if __name__ == "__main__":
    print("Enter 0 to exit")
    while(True):
        selection = input("\nSelect Problem ID: ")
        if selection == "0": 
            break
        print("Answer: " + str(selectSoln(selection)))
