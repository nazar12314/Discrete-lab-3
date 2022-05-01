import random

def generate_primes(min, max):
    primes = []
    for i in range(min, max + 1):
        for j in range(1, int(i**0.5)+1):
            if i % j == 0 and j != 1 and j != i:
                break
        else:
            primes.append(i)
    return primes


def are_relative_primes(first, second):
    for number in range(2, min(first, second)):
        if first % number == 0 and second % number == 0:
            return False
    return True


def generate_public_and_private_keys():
    prime_numbers = generate_primes(100, 1000)
    p, q = random.choices(prime_numbers, k=2)
    maximum = (p - 1) * (q - 1)
    e = None
    d = None

    for num in range(5, maximum, 2):
        if are_relative_primes(num, maximum):
            e = num
            
            for num_2 in range(3, maximum, 2):
                if (num_2 * e) % maximum == 1:
                    d = num_2
                    return (p * q, e), (p * q, d)
                
    raise Exception("Key not generated!")
