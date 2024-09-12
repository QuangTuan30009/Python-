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

    # Hiển thị thông tin sinh viên
    def display_info(self):
        print(f"Code: {self.code}, Name: {self.name}, Score: {self.score}")


class StudentArray:
    def __init__(self):
        self.students = []  
        self.size = 0  

    # Thêm sinh viên
    def add_student(self):
        student = Student()
        student.input_info()
        if any(s.code == student.code for s in self.students):
            print(f"Sinh viên với mã {student.code} đã tồn tại.")
        else:
            self.students.append(student)
            self.size += 1
            print("Thêm sinh viên thành công!")

    # Xóa sinh viên
    def delete_student(self):
        code = input("Nhập mã sinh viên cần xóa: ")
        original_size = self.size
        self.students = [student for student in self.students if student.code != code]
        self.size = len(self.students)  
        if self.size < original_size:
            print("Xóa sinh viên thành công!")
        else:
            print("Sinh viên không tồn tại.")

    # Cập nhật thông tin sinh viên
    def update_student(self):
        code = input("Nhập mã sinh viên cần cập nhật: ")
        for student in self.students:
            if student.code == code:
                print("Nhập thông tin mới cho sinh viên:")
                student.name = input("Nhập tên sinh viên mới: ")
                student.score = float(input("Nhập điểm sinh viên mới: "))
                print("Cập nhật sinh viên thành công!")
                return
        print("Sinh viên không tồn tại.")

    # Tìm kiếm sinh viên theo tên (có chứa chuỗi con)
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
    print("Quản Lý Sinh Viên")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Hiển thị danh sách sinh viên")
    print("6. Dừng chương trình")


def main():
    manager = StudentArray()

    while True:
        menu()
        choice = input("Chọn chức năng: ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.delete_student()
        elif choice == '3':
            manager.update_student()
        elif choice == '4':
            manager.search_student()
        elif choice == '5':
            manager.display_students()
        elif choice == '6':
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
