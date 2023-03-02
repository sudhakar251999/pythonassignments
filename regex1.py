#RegEx can be used to check if a string contains the specified search pattern.
#seaching function
'''Function Description
findall--Returns a list containing all matches
search-- Returns a Match object if there is a match anywhere in the string
split--  Returns a list where the string has been split at each match
sub	--   Replaces one or many matches with a string'''
import re
txt = "Thundersoft india pvt lmd hyderabad -500081"
x = re.search("500088", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


import re
txt = "Thundersoft india pvt lmd hyderabad -500081"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[A-Z]", txt)
print(x)
y= re.findall("[a-z]",txt)
print(y)

z= re.findall("\d",txt)
print(z)
#Search for a sequence that starts with "Th", followed by two (any) characters, and an "o":
a = re.findall("T...*", txt)
print(a)

b = re.findall("^Thundersoft", txt)
if b:
  print("Yes, the string starts with 'Thundersoft'")
else:
  print("the string No match")

#Search for a sequence that ends with "th", followed by two (any) characters, and an "ft"
c= re.findall("500081$", txt)
if c:
  print("Yes, the string ends with '500081'")
else:
  print("the string No match")
print(c)

#Search for a sequence that starts with "th", followed by 1 or more  (any) characters, and an "ft":

d= re.findall("Th..+ft", txt)
print("starts with",d)


#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

e= re.findall("Th...?t", txt)
print("sequence",e)
#Search for a sequence that starts with "in", followed excactly 2 (any) characters, and an "a":
f= re.findall("in.{2}a", txt)
print(f)

#Check if the string contains either "india" or "lmd":
txt = "Thundersoft india pvt lmd hyderabad -500081"
g = re.findall("india|lmd", txt)
print(g)
if g:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string starts with "Thu":

h = re.findall("\AThu", txt)

print(h)

if h:
  print("Yes, there is a match!")
else:
  print("No match")


#Check if the string contains any digits (numbers from 0-9):

k = re.findall("\d", txt)
print(k)
if k:
  print("Yes, there is at least one match!")
else:
  print("No match")


#Return a match at every white-space character:

l = re.findall("\s", txt)
print(l)
if l:
  print("Yes, there is at least one match!")
else:
  print("No match")


#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

m = re.findall("\w", txt)
print(m)
if m:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string ends with "india":
txt = "Thundersoft india pvt lmd hyderabad -500081"
n= re.findall("pvt\Z", txt)
print(n)
if n:
  print("Yes, there is a match!")
else:
  print("No match")


#Return a list containing every occurrence of "er":(findall)

txt = "Thundersoft india pvt lmd"
o= re.findall("er", txt)
print(o)
if o:
  print("Yes, there is a match!")
else:
  print("No match")
# counting the white-space
txt = "Thundersoft india pvt lmd"
p = re.search("\s", txt)
print("The first white-space character is located in position:", p.start())

#Split the string at every white-space character:

txt = "Thundersoft india pvt lmd"
q = re.split("\s", txt)
print(q)

#Split the string at the first white-space character:
txt = "Thundersoft india pvt lmd"
r= re.split("\s", txt, 2) #2 is count white space character
print(r)

#Replace all white-space characters with the digit "z or 9":

txt = "Thundersoft india pvt lmd"
s = re.sub("\s", "z", txt)
print(s)
