def giai_thua(n):

    if n < 0:
        raise ValueError("n phải là số nguyên dương")
    
    result = 1
    for i in range(1, n + 1):
         result *= i
    return result

n = int(input("Nhập số n:"))
giai_thua_n = giai_thua(n)
print(f"Giải thừa của {n} là: {giai_thua_n}")