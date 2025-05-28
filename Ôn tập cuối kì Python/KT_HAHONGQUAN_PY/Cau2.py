import sqlite3

conn=sqlite3.connect("QLThuvien.db")
cursor=conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS Tacgia(
#                     Matacgia TEXT PRIMARY KEY,
#                     Tentacgia TEXT,
#                     Gioitinh TEXT)""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS Sach(
#                 Masach TEXT PRIMARY KEY,
#                 Tensach TEXT,
#                 Chungloai TEXT,
#                 Matacgia TEXT,
#                 Dongia FLOAT,
#                 Ngayxb TEXT,
#                 FOREIGN KEY (Matacgia) REFERENCES Tacgia (Matacgia)) """)


tg = [('tg1','Phạm Văn Ất','nam'),
           ('tg2','Hà Hồng Quân','nam'),
           ('tg3','Tố Hữu','nam'),
           ('tg4','Nguyễn thị hoa','nữ'),
           ('tg5','Hoàng minh thúy','nữ')]
cursor.executemany('INSERT INTO Tacgia VALUES (?,?,?)', tg)

s = [('s1','Đi Chơi','Tiểu thuyết','tg1',200,'20/12/2021'),
    ('s2','Thơ ngâm 1','Thơ','tg2',100,'10/09/2020'),
    ('s3','Thiểu thuyết ngắn','Tiểu thuyết','tg3',150,'13/02/2021'),
    ('s4','Trường đoạn','Thơ','tg4',90,'17/01/2019'),
    ('s5','Lên trời','Truyện','tg1',230,'26/08/2019')]
cursor.executemany('INSERT INTO Sach VALUES (?,?,?,?,?,?)', s)


query = '''
SELECT s.Masach AS "Ma sach",
        s.Tensach AS "Ten sach",
        s.Chungloai AS "Chung loai",
        s.Dongia AS "Don gia",
        s.Ngayxb AS "Ngay xb",
        tg.Tentacgia AS "Ten tac gia"
FROM Sach s 
LEFT JOIN Tacgia tg ON s.Matacgia = tg.Matacgia 
WHERE tg.Tentacgia = "Phạm Văn Ất" 
GROUP BY s.Masach, s.Tensach, s.Chungloai, s.Dongia, s.Ngayxb'''

cursor.execute(query)

rows = cursor.fetchall()

col1 = 15
col2 = 15
col3 = 15
col4 = 13
col5 = 13
col6 = 15

tieude = f"| {'Ma sach':<{col1}} | {'Ten sach':<{col2}} | {'Chung loai':<{col3}} | {'Don gia':<{col4}} | {'Ngay xuan ban':<{col5}} | {'Ten tac gia' :<{col6}} |"

dorong = f"| {'-' * col1}-|-{'-' * col2}-|-{'-' * col3}-|-{'-' * col4}-|-{'-' * col5} |-{'-' * col6} |"

print(tieude)
print(dorong)

for Masach, Tensach, Chungloai, Dongia, Ngayxb , tentg in rows:
    print(f"| {Masach:<{col1}} | {Tensach:<{col2}} | {Chungloai:<{col3}} | {Dongia:<{col4}} | {Ngayxb:<{col5}} | {tentg:<{col6}} |")

conn.close()