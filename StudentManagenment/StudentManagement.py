

class Student:
    def __init__(self):
        self.code = None
        self.name = None
        self.score = None

    # Nhập thông tin sinh viên
    def input_info(self):
        self.code = input("Nhập mã sinh viên: ")
        self.name = input("Nhập tên sinh viên: ")
        self.score = float(input("Nhập điểm sinh viên: "))

    # Hiển thị thông tin sinh viên
    def display_info(self):
        print(f"Code: {self.code}, Name: {self.name}, Score: {self.score}")
class StudentManagement():
    def __init__ (self, code, name, score):
        self.code = code
        self.name = name
        self.score = score
        
        
    # tạo methods cho student
    def input(self):
        self.code = input("Student name: ")
        self.name = input("Student code: ")
        self.score = float(input("Student score: "))
    #hiển thị 
    def dis_play(self):
        self.student = []
    # tạo mảng dynamic student_array
class Student_array():
    def _make_array(self, c):

 
    #quản lý 
    def __init__(self) -> None:
        self.search_student = []
    #1 add student 
    def add(self):
        self.student=[]
        self.score=[]
        self.code=[]
    #2 delete 
    def delete(self):
    #3 update 
    def update (self):
        for student in self.students:
            if student.name == name:
                student.input_student()
                return True
        return False
    def update_student(self,score):
        for student in self.students:
            if student.score == score:
                student.input_student()
                return True
        return False
    #4 search 
    def search_student(self, name):
        current = self.name
        while current != None:
            if current.data == name:
                return True
            current = current.next
        return False 
    def display(self):

    #5 search
    def search_student(self, name):
        current = self.name
        while current != None:
            if current.data == name:
                return True
            current = current.next
        return False   
 
    def update(self, new_name, new_socre, code ):
        for student in self.student:
            if self.code == code:
                student.inpu_student()



def main():
    choice = 0

    while choice != 6:
        Menu.print()
        choice = Input.input_user_choice()

        if choice == 1:
            StudentManagement.add_new_student()
        elif choice == 2:
            StudentManagement.update_student()
        elif choice == 3:
            StudentManagement.delete_student()
        elif choice == 4:
            StudentManagement.update_student()
        elif choice == 5:
            StudentManagement.search_student()
        
class menu():
    def print_menu(self):
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Display Student")
        print("6. Exit")

class main():
    def main(self):
        choice = 0
    
        while choice != 6:
            Menu.print()
            choice = Input.input_user_choice()
    
            if choice == 1:
                StudentManagement.add_new_student()
            elif choice == 2:
                StudentManagement.update_student()
            elif choice == 3:
                StudentManagement.delete_student()
            elif choice == 4:
                StudentManagement.update_student()
            elif choice == 5:
                StudentManagement.search_student()
    
    
    if __name__ == "__main__":
        main()






