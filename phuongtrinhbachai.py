import math 
#nhập số a và b với điều kiện a, b khác 0
a = int(input("mời nhập số a:"))
while True :
    if a == 0: 
        a = int(input(" a phải khác 0 mời nhập lại số a: "))
    else :
        break 
b = int(input("mời nhập số b:")); 
while True :
    if b == 0:
        b = int(input(" b phải khác 0, mời nhập lại số b:"))
    else :
        break 
#nhập số c 
c = int(input("mời nhập số c:"))
#tính denta 
denta = b ** 2 - 4 * a * c
#so sánh denta với 0 
if denta < 0 :
    print("phương trình vô nghiệm")
if denta == 0 : 
    print("phương trình có nghiệm kép x1 = x2 = ", -(b / 2 * a))
if denta > 0 :
    print("phương trình có 2 nghiệm phân biệt :")
    print("x1 =", (-(b) + math.sqrt(denta)) / (2 * a))
    print("x2 =", (-(b) - math.sqrt(denta)) /(2 * a))

