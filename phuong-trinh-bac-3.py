#thư viện cmarth để sài đc số phức 
import cmath 
#cách tính phương trình bậc 3
#nhập hệ số a, b, c với điều kiện hệ số a khác 0 
a = int(input("Nhập hệ số a:"))
while True :
    if a == 0:
        a = int(input(" a phải khác 0, mời nhập lại a:"))
    else :
        break 
b = int(input("mời nhập số b:"))
c = int(input("mời nhập số c:"))
#Tính denta  đặc biệt và điều kiện denta lớn hơn 0 
denta = (b ** 2) - (3 * a * c)
if denta < 0 :
    print("phương trình có 3 nghiệm phức đối")
    print("x1 =", (-b + cmath.sqrt(-(denta))) / (3 * a))
    print("x2 =", (-b - cmath.sqrt(-(denta))) / (3 * a))
    print("x3 =", (-c) / a)
if denta == 0 :
    print("phuong trình 1 nghiệm thực bội và 2 nghiệm ảo thức đối")
    print("x1 = x2 =", (-b) / (3 * a))
    print("x3 =", (-b + cmath.sqrt(-(denta))) / ( 3 * a ))
    print("x4 =", (-b - cmath.sqrt(-(denta))) / ( 3 * a))
if denta > 0 :
    print("phương trình có 3 nghiệm thực")
    x1 =(-b + cmath.sqrt(denta)) / ( 3 * a)
    x2 =(-b - cmath.sqrt(denta)) / ( 3 * a)
    x3 =(-c) / (a * x1 * x2)
    print("x1 =", x1)
    print('x2 =', x2)
    print("x3 =", x3)

