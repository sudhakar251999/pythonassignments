'''#Conditinal statements
#sequential
print("hello world")
print("bangalore")
print("Ts")
#selection
#if
a=10
b=20
if a<b:
    print("a is less then b")

a=8
if a%2==0:
    print("a is even number")

a=9
b=5
if a>b:
    print("a is greater than b")

#if else

x=8
if x%2==0:
    print("x is even number")
else:
    print("x is odd number")

x=10
y=20
if x==y:
    print("x and b are equal")
else:
    print("x and y are not equal")

x=10
if x>0:
    print("x is positive number")
else:
    print("x is negative number")

i=20
if (i<15):
    print("i is smaller than 15")
else:
    print("i is greater than 15")


#if elif else

z=int(input("enter the number:"))
if z%2==0:
    print("z is divisble by 2")
elif z%3==0:
    print("z is divisble by 3")
else:
    print("z is neither divisble by 2 nor by 3")


b=30
if (b==10):
    print("b is 10")
elif (b==15):
    print("b is 15")
elif (b==20):
    print("b is 20")
else:
    print("b is not present")


number = int(input("enter the number:"))
if number > 0:
    print("Positive number")
elif number == 0:
    print('Zero')
else:
    print('Negative number')
print('This statement is always executed')

#nested if
number = 5
# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
        print('Number is 0')
    # inner else statement
    else:
        print('Number is positive')
# outer else statement
else:
    print('Number is negative')

age = 38
if (age >= 11):
  print ("You are eligible to see the Football match.")
  if (age <= 20 or age >= 60):
      print("Ticket price is $12")
  else:
      print("Ticket price is $20")
else:
    print ("You're not eligible to buy a ticket.")
#iterations
#for loops
days=['sun','mon','tues','wed','thur','fri','sat']
for days in days:
    print(days)

num=[1,2,3,4,5,6,8,]
for num in num:
    print(num)

for x in [10,20,30,40,50,60]:
    print(x)

#while loops

a=8
while a>0:
    print("a is:",a)
    a=a-2


# initialize the variable
i = 1
n = 5
# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1
#nested loop
x = [1, 2]
y = [4, 5]

for i in x:
    for j in y:
        print(i, j)

for i in range(2, 4):
     for j in range(1, 11):
        print(i, "*", j, "=", i * j)
print()

#break


for i in range(2, 4):
    for j in range(1, 11):
        if i == j:
            break
        print(i, "*", j, "=", i * j)
    print()

num = 0
for i in range(10):
    num += 1
    if num == 8:
        break
print("The num has value:", num)
print("Out of loop")

#continue


for var in "sudhakar":
    if var == "a":
        continue
    print(var,end=" ")

# loop from 1 to 10
for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")

#pass

n = 10
for i in range(n):
    pass
    print(i)'''

#range

for i in range(0,12,2):
    print(i)

a=8
for x in range(1,11,1):
    print(a,'*',x,'=',a*x)

c=7
count=0
for i in range(1,96):
    if i%c==0:
        count+=1
print(count)






