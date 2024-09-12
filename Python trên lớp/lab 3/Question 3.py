def ds():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    # Khởi tạo biến i để duyệt từ cuối danh sách
    i = len(numbers) - 1
    while i >= 0:
        print(numbers[i])
        i -= 1
ds()