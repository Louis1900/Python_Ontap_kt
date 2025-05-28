import sqlite3
import os

def connect_db():
    return sqlite3.connect("shopdb.db")

#sau khi chay file lần đầu tiên thì comment 2 cais hàm dưới đây lại
def create_db():
    if not os.path.exists("shopdb.db"):
        with connect_db() as conn:
            print("Tạo csdl mới")
            create_table()
    else:
        print("csdl đã tồn tại!, chỉ tạo bảng nếu chưa có")
        create_table()

def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS product(id TEXT PRIMARY KEY, 
                            name TEXT NOT NULL, price FLOAT NOT NULL)''')
        conn.commit()


#hàm thêm này sẽ không cần comment như 2 hàm trên
def themsp(id, name, price):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product (id, name, price) VALUES (?,?,?) ", (id, name, price,))#them 1 "dau phay vao cuoi"
        conn.commit()
        print("Da them san pham!")

def dssp():
    with connect_db() as conn:
        cursor = conn.cursor()
        #hien thi sp co gia tren 50000
        cursor.execute("SELECT * FROM product ")
        p=cursor.fetchall()
        col_width=[10, 20, 15]

        print("+)Danh sach san pham")
        print("{:10} {:20} {:15}".format("id","name","price"))
        print("-" * (sum(col_width) + len(col_width) * 1))

        if p:
            for i, row in enumerate(p):
                print("{:10} {:20} {:5}".format(*row))
                print("-" * (sum(col_width) + len(col_width) * 1))
        else:
            print("khong co phong nao!")

def htsp_nhohon50000():
    with connect_db() as conn:
        cursor = conn.cursor()
        #hien thi sp co gia tren 50000
        cursor.execute("SELECT * FROM product WHERE price<50000 ")
        p=cursor.fetchall()
        col_width=[10, 20, 15]

        print("\n+)Danh sach sp co gia < 50000")
        print("{:10} {:20} {:15}".format("id","name","price"))
        print("-" * (sum(col_width) + len(col_width) * 1))

        if p:
            for i, row in enumerate(p):
                print("{:10} {:20} {:5}".format(*row))
                print("-" * (sum(col_width) + len(col_width) * 1))
        else:
            print("khong co sp nao!")

# comment mấy dòng này lại
connect_db()
create_db()

themsp("01","dien thoai",50000)
themsp("02","pc",40000)
themsp("03","may tinh bang",70000)

dssp()

htsp_nhohon50000()