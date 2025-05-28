import sqlite3
import os 

def connect_db():
    return sqlite3.connect("shop.db")

# def create_db():
#     if not os.path.exists("shop.db"):
#         with connect_db() as conn:
#             print("Tao co so du lieu moi")
#             create_table()
#     else:
#         print("CSDL da ton tai, chi tao bang neu chu co")
#         create_table()

# def create_table():
#     with connect_db() as conn:
#         cursor = conn.cursor() 
#         cursor.execute(''' CREATE TABLE IF NOT EXISTS product(id TEXT PRIMARY KEY , 
#                            name TEXT NOT NULL, price FLOAT NOT NULL)''')
#         conn.commit()   


def themsp(id, name,price):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product (id, name, price) VALUES (?,?,?) ", (id, name, price,))
        conn.commit()
        print("Da them sp!")

# def htptheogia():
#     with connect_db() as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM product WHERE price > 50000 ")
#         dsp = cursor.fetchall()
#         if dsp:
#             print("ds phong co gia tu 5000 -> 10000 la: ")
#             for i in dsp:
#                 print("id:"+str(i[0])+", ten sp:"+str(i[1])+", gia:"+str(i[2]))
#         else:
#             print("k co phong nao")


def htsp():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product WHERE price > 50000 ")
        p =  cursor.fetchall()
        col_width = [5, 30, 20]
        
        print("Danh sach phong: ")
        print("{:5} {:<10} {:<20}".format("id    ", "name     ", "price    "))
        print("-" * (sum(col_width) + len(col_width) * 1))
        if p:
            for i, row in enumerate(p):
                print("{:5} {:<10} {:<20}".format(*row))
                print("-" * (sum(col_width) + len(col_width) * 1))
        else:
            print("Khong co phong nao!")

# connect_db()
# create_table()


# themsp("sp1","dien thoai", 56000)
# themsp("sp2","may tinh", 40000)
# themsp("sp3","may anh", 100000)


htsp()


