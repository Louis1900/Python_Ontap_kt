import sqlite3

conn = sqlite3.connect("db_qlthuvien.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS tacgia(
#                matg TEXT PRIMARY KEY,
#                tentg TEXT NOT NULL,
#                gioitinh TEXT NOT NULL)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS sach(
#                masach TEXT PRIMARY KEY,
#                tensach TEXT NOT NULL,
#                chungloai TEXT NOT NULL,
#                matg TEXT NOT NULL,
#                dongia FLOAT NOT NULL,
#                ngayxuatban TEXT NOT NULL, 
#                FOREIGN KEY (matg) REFERENCES tacgia(matg)) """)

tg = [('tg1', 'Pham van at', 'nam'),
      ('tg2', 'Ngyen thi linh', 'nam'),
      ('tg3', 'Ha thi quan', 'nu'),
      ('tg4', 'Hoang van son', 'nam'),
      ('tg5', 'Nguyen thi ha', 'nu')]
cursor.executemany('INSERT INTO tacgia VALUES (?,?,?)', tg)

tg = [('s1', 'Kinh thánh', 'Văn học', 'tg1', 200000, '13/12/2009'),
      ('s2', 'Thơ hàn', 'Thơ', 'tg2', 150000, '23/01/2007'),
      ('s3', 'Truyện cười', 'Truyện', 'tg4', 50000, '15/07/2006'),
      ('s4', 'Tuyen tap tho ca', 'Thơ', 'tg5', 70000, '11/04/2007'),
      ('s5', 'De men plk', 'Văn học', 'tg1', 250000, '24/11/2005')]
cursor.executemany('INSERT INTO sach VALUES (?,?,?,?,?,?)', tg)

query = '''SELECT s.masach AS "Ma sach", 
    s.tensach AS "Ten sach", 
    s.chungloai AS "Chung loai", 
    s.dongia AS "Don gia", 
    s.ngayxuatban AS "Ngay xb", 
    tg.tentg AS "Ten tg" 
FROM sach s 
LEFT JOIN tacgia tg On s.matg=tg.matg 
WHERE tg.tentg = "Pham van at" 
GROUP BY s.masach, s.tensach, s.chungloai, s.dongia, s.ngayxuatban, tg.tentg'''
cursor.execute(query)

rows=cursor.fetchall()
col1=10
col2=20
col3=15
col4=15
col5=15
col6=20

tieude=f"| {'Ma sach':<{col1}} | {'Ten sach':<{col2}} | {'Chung loai':<{col3}} | {'Don gia':<{col4}} | {'Ngay xb':<{col5}} | {'Ten tg':<{col6}} |"
dorong=f"| {'-' * col1}-|-{'-' * col2}-|-{'-' * col3}-|-{'-' * col4}-|-{'-' * col5}-|-{'-' * col6} |"
print(tieude)
print(dorong)

for masach, tensach, chungloai, dongia, ngayxb, tentg in rows:
    print(f"| {masach:<{col1}} | {tensach:<{col2}} | {chungloai:<{col3}} | {dongia:<{col4}} | {ngayxb:<{col5}} | {tentg:<{col6}} |")
conn.close()