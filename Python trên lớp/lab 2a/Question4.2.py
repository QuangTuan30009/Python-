a = 0
for i in (4, 6, 8, 24, 12, 2):
    if i > a:
        a = i
    else:
        break
    if a >= 24:
        print(a)