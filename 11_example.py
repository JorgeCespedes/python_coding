
def sieveOfEratosthenes(n):
    '''Primes Numbers smaller than or equal to the Number'''
    primes = [True] * (n + 1)
    p = 2                   # because p is smallest prime
    while(p * p <= n):
        # if p is not maked as False, this it is a prime
        if (primes[p]) == True:
            # mark the all multiples of number as false
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    # printing all primes
    for i in range(2, n):
        if primes[i]:
            print(i)

if __name__ == '__main__':
    n = int(input('Enter a no to check all smaller prime number : '))
    sieveOfEratosthenes(n)



