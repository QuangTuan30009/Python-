def palindrome(num):
    num_str = str(num)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            return False
    return True


m = int(input("Nhập số nguyên thứ nhất : "))
n = int(input("Nhập số nguyên thứ hai : "))

if m >= n:
    print("Lỗi: m phải nhỏ hơn n")
else:
    # Hiển thị tất cả các số palindrome trong khoảng [m, n]
    for i in range(m, n + 1):
        if palindrome(i):
            print(i)
