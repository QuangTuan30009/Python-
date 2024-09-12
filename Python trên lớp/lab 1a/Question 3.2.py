a = 0
b = 10 
while a < b :
    trc = a - 1 if a > 0 else 0 
    print("Current Number", a , "Pervious Number", trc, "Sum: ", a + trc)
    a += 1