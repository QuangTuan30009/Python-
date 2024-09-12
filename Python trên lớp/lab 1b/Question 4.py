a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

current_max = a
current_min = a

for number in [b, c]:
  if number > current_max:
    current_max = number
  if number < current_min:
    current_min = number

print(f"Max: {current_max:.2f}, Min: {current_min:.2f}")
