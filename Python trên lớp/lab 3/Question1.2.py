def sum(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    print(tong)
n = int(input("nhập số i : "))
sum(n)