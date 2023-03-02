# Program to check if a number is prime or not

num =int(input("enter the number"))
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 1:
            print(num, "is prime number")
    else:
        print(num, "is a not prime number")