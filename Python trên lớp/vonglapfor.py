def sln():
    so_lon_nhat = -1
    for i in [3, 41, 21, 9, 74, 15]:
        if i >= so_lon_nhat:
            so_lon_nhat = i
    print("Số lớn nhất là:", so_lon_nhat)

sln()
print("done")
