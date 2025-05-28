from datetime import datetime
import csv

class Student:
    def __init__(self, ma, hoten, ngaysinh, gpa):
        self.ma = ma
        self.hoten = hoten
        self.ngaysinh = self.KT_Date(ngaysinh)
        self.gpa = self.KT_GPA(gpa)

    def __str__(self):
      return f"Mã SV: {self.ma}, Họ Tên: {self.hoten}, Ngày Sinh: {self.ngaysinh}, GPA: {self.gpa}"
    @staticmethod
    def KT_Date(date):
        try:
            datetime.strptime(date, "%d/%m/%Y")
            return date
        except ValueError:
            raise ValueError("Ngày sinh không hợp lệ, phải có định dạng dd/mm/yyyy")

    @staticmethod
    def KT_GPA(gpa):
        try:
            gpa = float(gpa)
            if 0 <= gpa <= 10:
                return gpa
            else:
                raise ValueError("GPA phải trong khoảng từ 0 đến 10")
        except ValueError:
            raise ValueError("GPA phải là số hợp lệ")

    @staticmethod
    def Ghi_file(filename):
        students = []
        try:
            n = int(input("Nhập số lượng sinh viên: "))
            for _ in range(n):
                ma = input("Nhập mã SV: ")
                hoten = input("Nhập họ tên: ")
                ngaysinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
                while True:
                    try:
                        ngaysinh = Student.KT_Date(ngaysinh)
                        break
                    except ValueError as e:
                        print(e)
                        ngaysinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
                
                gpa = input("Nhập GPA: ")
                while True:
                    try:
                        gpa = Student.KT_GPA(gpa)
                        break
                    except ValueError as e:
                        print(e)
                        gpa = input("Nhập GPA: ")
                
                students.append(Student(ma, hoten, ngaysinh, gpa))
        except ValueError:
            print("Số lượng sinh viên phải là số nguyên hợp lệ.")
            return

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Mã SV", "Họ Tên", "Ngày Sinh", "GPA"])
            for student in students:
                if student.gpa > 7.0:
                    writer.writerow([student.ma, student.hoten, student.ngaysinh, student.gpa])
        print("Dữ liệu đã được ghi vào tệp thành công.")

    @staticmethod
    def Docfile(filename):
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Bỏ qua tiêu đề
                print("\nDanh sách sinh viên có GPA > 7.0:")
                for row in reader:
                    student = Student(row[0], row[1], row[2], float(row[3]))
            print(student)
        except FileNotFoundError:
            print("Tệp không tồn tại. Hãy nhập dữ liệu trước.")
        except Exception as e:
            print("Lỗi khi đọc tệp:", e)

# Chạy chương trình
filename = "students.csv"
Student.Ghi_file(filename)
Student.Docfile(filename)