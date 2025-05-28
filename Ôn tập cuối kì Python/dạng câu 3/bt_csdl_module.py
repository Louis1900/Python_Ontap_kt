#bài này làm dạng mudule hóa, chia hàm để tái sử dụng
import sqlite3
import os #xu li den he dieu hanh, duong dan den cac thu muc(path)
def connect_db():
    return sqlite3.connect("qlsv.db")
# def create_db():
#     if not os.path.exists("qlsv.db"):
#         with connect_db() as conn:
#             print("Tao co so du lieu moi")
#             create_table()
#     else:
#         print("CSDL da ton tai, chi tao bang neu chu co")
#         create_table()
# def create_table():
#     with connect_db() as conn:
#         cursor = conn.cursor() #mo CSDL
#         cursor.execute(''' CREATE TABLE IF NOT EXISTS Lop(id INTEGER PRIMARY KEY AUTOINCREMENT, tenlop TEXT NOT NULL)''')
#         cursor.execute(''' CREATE TABLE IF NOT EXISTS Sinhvien(id INTEGER PRIMARY KEY AUTOINCREMENT, hoten TEXT not null, 
#                        masv TEXT UNIQUE NOT NULL, lop_id INTEGER, FOREIGN KEY(lop_id) REFERENCES Lop(id))''')
#         conn.commit()   #cho luu cac thay doi trong conn
def themlop(tenlop):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Lop (tenlop) VALUES (?) ", (tenlop,))#dau phay "," co nghia la con co them 1 truong nua
        conn.commit()
        print("Da them lop!")
def themsv(hoten, masv,lop_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Sinhvien (hoten, masv, lop_id) VALUES (?,?,?) ", (hoten, masv, lop_id,))
        conn.commit()
        print("Da them sinh vien!")
def hienthisv(tenlop):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Sinhvien.hoten, Sinhvien.masv, Sinhvien.lop_id FROM Sinhvien JOIN Lop ON Sinhvien.lop_id = Lop.id WHERE Lop.tenlop = ? ", (tenlop,))
        sv = cursor.fetchall()#doc ban gi
        if sv:
            print("Ds sv lop "+str(tenlop)+":")
            for i in sv:
                print("Ho ten: "+str(i[0])+", msv: "+str(i[1])+", Lopid: "+str(i[2]) )
        else:
            print("Khong co sv nao trong lop nay!")
        print("---------------------------------")
def hienthilop():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Lop ")
        sv =  cursor.fetchall()
        if sv:
            print("Danh sach cac lop: ")
            for i in sv:
                print(str(i[0])+", Lop: "+str(i[1]))
        else:
            print("Khong co sinh vien nao trong lop nay!")
        print("---------------------------------")
def suasv(hotenmoi, masv):
    with connect_db() as conn:
        cursor = conn.cursor() 
        cursor.execute("UPDATE Sinhvien SET hoten = ? WHERE masv = ? ", (hotenmoi, masv))
        conn.commit()
def xoasv(masv):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Sinhvien WHERE masv = ? ", (masv,))
        conn.commit()
# themlop("cntt")
# themlop("cntt2")
# themsv("ha van quan", "sv001", 1)
# themsv("ha minh quan", "sv002", 1)
# themsv("ha hong quan", "sv003", 2)
# themsv("ha hong quan", "sv004", 2)
hienthilop()
hienthisv("cntt")
hienthisv("cntt2")
# suasv("ha thi quan","sv001")
# xoasv("sv004")