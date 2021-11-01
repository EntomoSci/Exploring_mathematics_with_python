def is_prime(num):
    '''This function checks if a number is a prime number or not and returns a boolean value'''
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def get_prime_numbers(list_amount=10):
    '''This function returns by default a list of the first 10 prime numbers'''
    
    prime_list = []
    num = 1
    while len(prime_list) < list_amount:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list