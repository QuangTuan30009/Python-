def tong(n):
    sum = 0
    while (n > 0):
        sum = sum+ n % 10
        n = int(n / 10)
    return sum
 
n = int(input("Nhập số nguyên dương n = "))
print("Tổng các chữ số của", n , "là", tong(n))
