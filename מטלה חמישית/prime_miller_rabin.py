"""
student: Asaf Fitusi
ID:318763430
Assignment no.5
program: prime_miller_rabin
"""
"""
This program generates prime numbers using the Miller-Rabin primality test. 
It creates random odd numbers of a specified length, verifies their primality, 
and ensures the generated numbers meet all requirements.
"""
import random

def modular_power(x, b, n):#This function computes x**b % n using iterated squaring
    lst = []
    try:
        while b > 0:#The loop converts the exponent b to its binary representation (LSB first).
            lst.append(b % 2)
            b //= 2
        result = 1
        for k in lst[::-1]:#This loop iterates over the binary representation of b (MSB first).
            result = (result**2) % n
            if k == 1:
                result = (result * x) % n
        return result
    except Exception as e:
        print(e)

def get_even_odd_parts(n):#This function calculates the even degree and the odd part.
    try:
        even_n = 0
        while n % 2 == 0:#Divides n by 2 until it becomes odd.
            n //= 2
            even_n += 1
        odd_n = n
        return even_n, odd_n
    except Exception as e:
        print(e)

def is_suspected_prime(n, t, s):#This function determines whether a number is prime using Miller-Rabin.
    a = random.randint(2, n - 2)
    d = modular_power(a, t, n)
    try:
        if d == 1 or d == n - 1:
            return True
        for i in range(s - 1):#Iterates through the range (0, s-2) for Miller-Rabin steps.
            d = (d**2) % n
            if d == n - 1:
                return True
        return False
    except Exception as e:
        print(e)

def is_probaly_prime(n):#This function performs a probabilistic primality test.
    try:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        (s, t) = get_even_odd_parts(n - 1)
        for i in range(10):#Increased the number of tests for larger numbers.
            if not is_suspected_prime(n, t, s):
                return False
        return True
    except Exception as e:
        print(e)

def make_random_odd_number(m):#This function generates a random odd number of length m.
    e_str = ''
    try:
        for i in range(m):#Generates the number according to the required conditions.
            if i == 0:
                first_digit = random.randint(1, 9)
                e_str += str(first_digit)
            elif i + 1 == m:
                last_digit = random.choice([1, 3, 5, 7, 9]) 
                e_str += str(last_digit)
            else:
                e_str += str(random.randint(0, 9))  
        int_e_str = int(e_str)
        return int_e_str
    except Exception as e:
        print(e)

def make_prime(m):#Generates a prime number of length m.
    try:
        x = make_random_odd_number(m)
        while not is_probaly_prime(x):#Ensures that the generated number is prime.
            x = make_random_odd_number(m)
        return x
    except Exception as e:
        print(e)

def main():#This is the main function of the program.
    try:
        print(make_prime())
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()