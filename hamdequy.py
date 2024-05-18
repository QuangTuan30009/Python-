from math import *

def S(n):

    if n == 0:

        return 1

    else:

        return n * S(n - 1)

if __name__ == "__main__":

    n = int(input("Nhập n:"))

    print(S(n))
def nhap_n_phan_tu():
    global n
    try:
        n = int(input("Nhập n phần tử:"))
    except:
        print("Vui longf nhập số\n")
def hoan_doi_phan_tu(a, n):
    if len(a) == n:
        print(a)
    else:
        for i in range(1, n + 1):
            if i not in a :
                a.append(i)
                hoan_doi_phan_tu(a, n)