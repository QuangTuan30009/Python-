
def toan(n):
    while n <= 5:
        n = int(input("n phải lớn hơn 5, mời nhập lại: "))
    S1 = 0
    #tổng từ 1 đến n
    for i in range(1, n + 1):
        S1 += i
    print('Tổng từ 1 đến', n, "là:", S1)
    #giai thừa của n 
    S2 = 1
    for j in range ( 1, n + 1):
        S2 *= j
    print("Giai thừa của", n, "là: ", S2)
    # tính S3
    S3 = 0
    for k in range(1, n + 1):
        S3 += 1/k
    print("Tổng bằng: ", S3)
    #số nguyên tố 
    m = int(input("Nhập lại số n: "))
    #điều kiện của số nguyên tố 
    is_prime = True
    for i in range(2, m):
        if m % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(m, "là số nguyên tố")
    else:
        print(m, "không phải là số nguyên tố")
n = int(input('Nhập số n: '))
toan(n)
