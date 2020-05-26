#encoding:utf-8
def sum_prime_dp (n):
    #This implements the concept of dinamic programming
    #Strategy: First mark the primes, then sum it up
    #Prime numbers are divisible only by 1 and by itself
    
    #din is the actual resultant array
    #ranged from 0 to limit of the array plus 1
    #filled with 0s from start
    din = [0 for i in range(n + 1)]
    
    #arr will be used as a marker for primes
    arr = [0 for i in range(n + 1)]

    #Avoiding costs on importing math (questionable)
    sqrt_n = int(n ** (0.5))

    #We will be using 0 as a marker for "prime"
    #and 1 as a marker for "non-prime"
    
    #Trivially
    arr[0], arr[1] = 1, 1

    #Loop from 0 to sqrt(n) + 1, we intend to check for
    #all prime numbers simmilarly than what is done using
    #the "Sieve of Eratosthenes"
    #More info.:https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    for i in range(sqrt_n + 1):
        #If we find a value that doesnt have been marked as prime
        #after analysing what came before him, then it is by
        #itself a prime.
        if(arr[i] == 0):
            #Therefore, all multiples of such number cannot be primes
            for j in range(2*i, n + 1, i):
                arr[j] = 1

    #Accumulator for sum
    sum_of_primes = 0
    
    #For every prime marked, we sum its index
    #The values in the final array represent the sum "up to that point"
    #for each acessed index
    for i in range(n + 1):
        if(arr[i] == 0):
            sum_of_primes += i
        din[i] = sum_of_primes
    
    return din

def sum_prime_range(begin, end):
    sum_array = sum_prime_dp(end)
    #Calculates the sum based on a specific interval
    #Notice that it can be achieved by simply subtracting
    #the sum of all primes from the beginning from 
    #the sum of all primes till the end of the interval
    return(sum_array[end] - sum_array[begin - 1])

def main_wrapper():
    #Simple wrapper, for managing input
    value1, value2 = 0, 0

    while(value1 == 0 or value2 == 0):
        #Not necessary to do it for intervals with 0
        value1 = int(raw_input())
        value2 = int(raw_input())
    #Ensures begin and end
    print(sum_prime_range(min(value1, value2), max(value1, value2)))

main_wrapper()
