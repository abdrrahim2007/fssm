
"""
i = int(input("enter a number : "))
max = i
while i!=0:
    i = int(input("enter another number : "))

    if i<max or i ==0:
        max=max
    elif i>=max:
        max=i
    else:
        print("something went wrong")


print("the max is : ",max)
"""

"""
i = int(input("enter a number : "))
pos = 1
max = i
while i!=0:
    i = int(input("enter another number : "))
    pos +=1

    if i<max or i ==0:
        max=max
    elif i>=max:
        max_pos = pos
        max=i
    else:
        print("something went wrong")


print(f"the max is {max} and it's position is {max_pos}")

"""

"""
from random import randrange
randn = randrange(1,20)
choice = input('guess a number between 1 and 20 (or type give up) : ')
attempts = 1
while choice != 'give up':
    if int(choice) == randn and attempts==1:
        print("you guess it at 1st attempt")
    elif int(choice) == randn:
        print(f"you guess it after {attempts}")
    else:
        if int(choice) >randn:
            print("too high")
        else:
            print("too low")
    choice = input('guess again : ')
    attempts +=1
if int(choice) =="give up":
    print(f"real number was {randn} you tried {attempts} attempts but didn't guess it")

"""
"""
i = int(input('enter a number : '))
n=i
res = i
while i!=1:
    res *=(i-1)
    i-=1

print(f" the factorial of {n} is {res}")
"""
"""
b = int(input("enter a positif number : "))
h=b
res_h=''
res_b =''
while b!=0:

    res_b +=str(b%2)
    b//=2
while h!=0:

    if h%16 ==15:
        res_h +="F"
    elif h%16 ==14:
        res_h +="E"
    elif h%16 ==13:
        res_h +="D"
    elif h%16 ==12:
        res_h +="C"
    elif h%16 ==11:
        res_h +="B"
    elif h%16 ==10:
        res_h +="A"
    else:
        res_h +=str(h%16)
    h//=16

print(f"the number in hexadicimal is {res_h[::-1]}")

print(f"the number in binary is {res_b[::-1]}")

"""

#S1
"""
n = int(input("enter a number  : "))
i = 0
s=0
p=1
while p<=n:
    s += i+1
    i+=1
    p+=1
print(f"la somme est {s}")"""
#2

"""
n = int(input("enter a number  : "))
i = 0
s=0
p=1
while p<=n:
    s += 2*(i+1)
    i+=1
    p+=1
print(f"la somme est {s}")
"""
"""

n = int(input("enter a number  : "))
i = 0
s=0
p=1
while p<=n:
    s += 2*(i+1)-1
    i+=1
    p+=1
print(f"la somme est {s}")
"""

"""
n = int(input("enter a number  : "))
i = 0
s=0
p=1
while p<=n:
    s += (i+1)**2
    i+=1
    p+=1
print(f"la somme est {s}")
"""

"""
n = int(input("enter a number  : "))
i = 0
s=0
p=1
while p<=n:
    s += (i+1)**3
    i+=1
    p+=1
print(f"la somme est {s}")
"""