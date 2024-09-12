class Student:
    def __init__(self, code=None, name=None, score=None):
        self.code = code
        self.name = name
        self.score = score

    # Nhập thông tin sinh viên
    def input_info(self):
        self.code = input("Nhập mã sinh viên: ")
        self.name = input("Nhập tên sinh viên: ")
        self.score = float(input("Nhập điểm sinh viên: "))
    def _make_array(self, c):
        return( c * ctypes.py_object)()

    # Hiển thị thông tin sinh viên
    def display_info(self):
        print(f"Code: {self.code}, Name: {self.name}, Score: {self.score}")

#Student 
class Student_array:
    def __init__(self):
        self.students = []

    # Thêm sinh viên vào mảng
    def add_student(self, student):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  
        self.students[self.n] = student
        self.n += 1

    # Hàm thay đổi kích thước mảng
    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)  #
        for i in range(self.n):
            new_array[i] = self.students[i]  # Sao chép dữ liệu cũ sang mảng mới
        self.students = new_array
        self.capacity = new_capacity

    # Kiểm tra sinh viên có tồn tại
    def student_exists(self, code):
        return any(student.code == code for student in self.students)

    # Xóa sinh viên
    def delete_student(self, code):
        for i in range(self.n):
            if self.students[i].code == code:
                for j in range(i, self.n - 1):
                    self.students[j] = self.students[j + 1]  # Dịch chuyển các phần tử
                self.students[self.n - 1] = None  # Loại bỏ phần tử cuối cùng
                self.n -= 1
                print("Xóa sinh viên thành công!")
                return
        print("Sinh viên không tồn tại.")

    # Cập nhật thông tin sinh viên
    def update_student(self, code):
        for i in range(self.n):
            if self.students[i].code == code:
                print("Nhập thông tin mới cho sinh viên:")
                new_name = input("Nhập tên sinh viên mới: ")
                new_score = float(input("Nhập điểm sinh viên mới: "))
                self.students[i].name = new_name
                self.students[i].score = new_score
                print("Cập nhật sinh viên thành công!")
                return
        print("Sinh viên không tồn tại.")

    # Tìm kiếm sinh viên theo tên 
    def search_student(self):
        search_name = input("Nhập tên hoặc chuỗi cần tìm: ")
        results = [student for student in self.students if search_name.lower() in student.name.lower()]
        if results:
            print("Kết quả tìm kiếm:")
            for student in results:
                student.display_info()
        else:
            print("Không tìm thấy sinh viên nào.")

    # Hiển thị danh sách sinh viên
    def display_students(self):
        if not self.students:
            print("Danh sách sinh viên trống.")
        else:
            print("Danh sách sinh viên:")
            for student in self.students:
                student.display_info()

   

def menu():
    print("\n===== Quản Lý Sinh Viên =====")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Hiển thị danh sách sinh viên")
    print("6. Dừng chương trình")


def main():
    manager = Student_array()
    manager.initialize_students()  # Khởi tạo danh sách sinh viên mẫu

    while True:
        menu()
        choice = input("Chọn chức năng: ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.delete_student()
        elif choice == '3':
            manager.update_student()
     

