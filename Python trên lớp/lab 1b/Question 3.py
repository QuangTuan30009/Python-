import math 

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
x = float(input("Nhập số x: "))
s1 = (a * x * x) + (b * x) + c
print(s1)
denta = b * b - (4 * a * c)
if denta > 0:
    print("s2 = ", math.sqrt(denta))
else:
    print("s2 = 0")




a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

if a + b > c or a + c > b or b + c > a:
    p = (a + b + c) / 2
    S1 = math.sqrt(p * (p - a) * ( p - b) * (p - c))
    print(S1)
else :
    print(a, b, c, "a, b, c are not side of a triangle")
    
