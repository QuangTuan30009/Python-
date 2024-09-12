def print_N(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Finish!')
n = int(input("Nhậpn : "))
print_N(n)




while True:
    line = input("nhap chuoi: ")
    if line == "#":
        continue
    if line == "done":
        break
    print(line)
print("done")