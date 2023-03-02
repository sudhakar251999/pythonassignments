n= int(input("enter a number:"))
reverse = 0
while n != 0:
    rem = n % 10
    reverse = reverse * 10 + rem
    n = n // 10
print("{} is reverse of {}".format(reverse,n))





