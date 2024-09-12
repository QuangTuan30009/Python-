import math
a = float(input("Moi nhap so a : "))
if a == 0:
    a = float(input(" a phai khac 0, moi nhap lại : "))
b = float(input("nhap so b : "));
if b == 0:
    b = float(input(" b phao khac 0, moi nhap lai so b: "))
c = float(input("moi nhap so c: "))
denta = b ** 2 - 4 * a * c
if denta < 0 :
    print("phuong trinh vo nghiem !")
if denta == 0 :
    print("phương trinh co nghiem kep x1 = x2 = ", -(b / 2 * a))
if denta > 0 :
    print("phương trinh co 2 nghiem phan biet :")
    print("x1 =", (-(b) + math.sqrt(denta)) / (2 * a))
    print("x2 =", (-(b) - math.sqrt(denta)) /(2 * a))

