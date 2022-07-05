def nth_prime(n):

    # Sieve of Erathosthenes
    max_size = 1000005
    numbers = [True for i in range(max_size+1)]

    p = 2
    while (p * p <= max_size):

        if numbers[p] == True:
            for multiple in range(p*p, max_size+1, p):
                numbers[multiple] = False
        
        p += 1
    
    primes = []
    for i in range(2, max_size+1):
        if numbers[i]:
            primes.append(i)

    return primes[n-1]



print(nth_prime(16))
