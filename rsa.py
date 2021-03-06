import random
import string


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
    prime_numbers = generate_primes(50, 500)
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


def convert_string_to_number(strng):
    characters = string.printable
    items = {characters[num]: str(num) if num >= 10 else "0" + str(num) for num in range(len(characters))}
    result = ""
    for char in strng:
        char_number = items[char]
        result += char_number
    return result

def convert_number_to_string(converted_message):
    characters = string.printable
    result = ""
    items = {str(num) if num >= 10 else "0" + str(num): characters[num] for num in range(len(characters))}
    for num in [converted_message[i:i+2] for i in range(0, len(converted_message), 2)]:
        char = items[num]
        result += char
    return result


def encode(public_keys, message:str):
    converted_message = convert_string_to_number(message)
    e, n = public_keys
    encoded = ""
    for i in range(len(converted_message)//2):
        block = converted_message[i*2:(i + 1)*2]
        encoded = encoded + str(int(block) ** e % n) + ","
    return encoded[:-1]


def decode(private_keys, encoded_message):
    d, n = private_keys
    blocks = [int(x) for x in encoded_message.split(",")]
    decoded = ""
    for block in blocks:
        calculated = str(block ** d % n)
        decoded = decoded + "0"*(2-len(calculated)) + calculated
    return convert_number_to_string(decoded)


if __name__ == "__main__":
    public, private = generate_public_and_private_keys()
    message = input("Message: ")
    encoded = encode(public, message)
    decoded = decode(private, encoded)
    print(decoded)
