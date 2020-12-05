import math

a = int(input())
b = int(input())
c = int(input())

#step1
print("find if the value a is - or +")

#step2
x = ((-b) / (2*a))

#step3
y = float(((a)*(x**2))+((b)*(x))+(c))

#step4
vertex = f"{x ,y}"

#step5
axis_of_symmetry = x

#step6
def yintcept():
    x = 0
    yintercept = float(((a) * (x ** 2)) + ((b) * (x)) + (c))
    print(f'y intercept value is = {yintercept}')

#step7
def xintercept():
    x1intercept = (-b + math.sqrt(b ** 2 - (4) * (a) * (c))) / (2 * a)
    print(f'x1 intercept value is {x1intercept}')
    x2intercept = (-b - math.sqrt(b ** 2 - (4) * (a) * (c))) / (2 * a)
    print(f'x2 intercept value is {x2intercept}')

print(f'axis_of_symmetry = {axis_of_symmetry}')
print(f'vertex point is = {vertex}')
xintercept()
yintcept()