"""
Accept a positive integer n, with n > 1n>1, as input from the user and print all the prime factors of n in ascending order.
"""

def isPrime(num):  # sourcery skip: invert-any-all, use-any
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True 

n = int(input())

if n > 1:
    for i in range(2, n+1):
        if n % i == 0 and isPrime(i):
            print(i)
            
# Public Test cases passed: 2/2
# Private Test cases passed: 5/5