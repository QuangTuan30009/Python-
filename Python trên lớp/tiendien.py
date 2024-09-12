def ao(n):
    if n <= 3 :
        print("Số tiền phải trả là : ", n * 120000 )
    elif 4 <= n <= 6 :
        print("Số tiền bạn phải trả là : ", 3 * 120000 + (n - 3) * 90000 )
    elif 7 <= n <= 10:
        print("Số tiền bạn phải trả là : ", 3 * 120000 + 3 * 90000 +(n - 6) * 85000)
    else :
        print("Số tiền phải trà là : ", 3 * 120000 + 3 * 90000 + 4 * 85000 + (n - 10) * 70000 )

n = int(input("Nhập số áo bạn mua : "))
ao(n)


