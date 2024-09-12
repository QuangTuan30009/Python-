import math

def code(n):
  try:
    if isinstance(n, float):
      n = float(n)
    n = int(n)
  except ValueError:
    n = int(input("n phải là số nguyên, mời nhập lại: "))
  nhi_phan = bin(str(n))[2:]
  print(f"Số {n} ở dạng nhị phân là: {nhi_phan}")

n = input("Nhập n: ")
n = code(n)
code(n)
