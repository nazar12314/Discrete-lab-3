import random
import math

def generate_primes(min, max):
    primes = []
    for i in range(min, max + 1):
        for j in range(1, int(i ** 0.5) + 1):
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

    for num in range(3, maximum, 2):
        if are_relative_primes(num, maximum):
            e = num

        for num_2 in range(3, maximum, 2):
            if num_2 * e % maximum == 1:
                d = num_2
                return (e, p * q), (d, p * q)


def encode(public_keys, message:str):
    e, n = public_keys
    N = 25
    while True:
        if N*100+25<n:
            N = N*100+25
        else: break
    encoded = ""
    split = len(str(N))
    for i in range(math.ceil(len(message)/split)):
        #block = f"{message[i * split:(i + 1) * split]}{'0'*(split-len(message[i * split:(i + 1) * split]))}"
        block = message[i * split:(i + 1) * split]
        encoded = encoded + str(int(block) ** e % n) + ","
    return encoded+str(split)


def decode(private_keys, encoded_message):
    d, n = private_keys
    blocks = [int(x) for x in encoded_message.split(",")]
    split = blocks[-1]
    decoded = ""
    for block in blocks[:-1]:
        print(block)
        calculated = str(block ** d % n)
        decoded = decoded + "0"*(split-len(calculated)) + calculated
    return decoded


if __name__ == "__main__":
    public, private = generate_public_and_private_keys()
    message = input("Message: ")
    encoded = encode(public, message)
    decoded = decode(private, encoded)
    print(f"Message: {message}, encoded: {encoded}, decoded: {decoded}")
