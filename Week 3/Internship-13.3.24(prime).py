def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def prime_or_factorial():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print("It is a prime number.")
        print("Sum of digits:",sum_of_digits(num))
    else:
        print("It is not a prime number.")
        print("Factorial:",factorial(num))
prime_or_factorial()
