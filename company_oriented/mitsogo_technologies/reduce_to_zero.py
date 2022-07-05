def is_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    
    return True

def find_greatest_prime(n):
    prime = False
    for i in range(n//2, 2, -1):
        prime = is_prime(i)
        if prime is True:
            # print(i, n)
            return i
        

def reduce_to_zero(n):

    counter = 0
    while n >= 1:
        prime = is_prime(n)
        if n == 1:
            n -= 1
            return counter
        if n > 1 and prime:
            n -= 1
            counter += 1

        elif not prime:
            greatest_prime = find_greatest_prime(n)
            print(greatest_prime)
            n = n-greatest_prime
            counter += 1
    
    return counter


print(reduce_to_zero(10))


                