#đề bài:
# +)CSDL:lop(ma_lop, ten_lop)
#        sinhvien(ma_sv, ten_sv, gioitinh, ma_lop, diem_tb)
# +)Yêu cầu:
#   Hiển thị danh sách sinh viên thuộc lớp "CNTT1", kèm tên lớp.
#   Liệt kê sinh viên có điểm TB > 7.0 và là nữ, sắp xếp theo điểm giảm dần.

import sqlite3

conn = sqlite3.connect("db_qlsinhvien.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS lop(
#                malop TEXT PRIMARY KEY,
#                tenlop TEXT)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS sinhvien(
#                masv TEXT PRIMARY KEY,
#                tensv TEXT,
#                gt TEXT,
#                malop TEXT,
#                dtb FLOAT)""")

lop = [('cntt','CNTT1'),
       ('dulich','Dulich1'),
       ('y','YDuoc'),
       ('Luat','Luat1'),
       ('YDK','YDaKhoa')]
cursor.executemany('INSERT INTO lop VALUES (?,?)',lop)

sv = [('sv1', 'ha thi quan', 'nu', 'cntt', 9),
      ('sv2', 'ha van quan', 'nam', 'cntt', 8),
      ('sv3', 'ha minh quan', 'nam', 'y', 7.5),
      ('sv4', 'ha huyen quan', 'nu', 'Luat', 9.5),
      ('sv5', 'ha hong quan', 'nam', 'dulich', 9.2)]
cursor.executemany('INSERT INTO sinhvien VALUES (?,?,?,?,?)',sv)


print("cau 1: Hiển thị danh sách sinh viên thuộc lớp CNTT1, kèm tên lớp.")
query1 = '''SELECT 
    s.masv AS "Masv", 
    s.tensv AS "Tensv", 
    s.gt AS "Gioitinh",
    s.malop AS "Malop",
    s.dtb AS "DTB",
    l.tenlop AS "Tenlop" 
FROM sinhvien s 
LEFT JOIN lop l ON s.malop=l.malop 
WHERE l.tenlop="CNTT1" '''
cursor.execute(query1)
rows=cursor.fetchall()
col11=10
col12=13
col13=10
col14=10
col15=10
col16=10
tieude1=f"| {'Masv':<{col11}} | {'Tensv':<{col12}} | {'Gioitinh':<{col13}} | {'Malop':<{col14}} | {'DTB':<{col15}} | {'Tenlop':<{col16}} |"
dorong1=f"| {'-' * col11}-|-{'-' * col12}-|-{'-' * col13}-|-{'-' * col14}-|-{'-' * col15}-|-{'-' * col16} |"
print(tieude1)
print(dorong1)
for masv, tensv, gt, malop, dtb, tenlop in rows:
    print(f"| {masv:<{col11}} | {tensv:<{col12}} | {gt:<{col13}} | {malop:<{col14}} | {dtb:<{col15}} | {tenlop:<{col16}} |")



print("\ncau 2:Liệt kê sinh viên có điểm TB > 7.0 và là nữ, sắp xếp theo điểm giảm dần.")
query2 = '''SELECT 
    s.masv AS "Masv", 
    s.tensv AS "Tensv", 
    s.gt AS "Gioitinh",
    s.malop AS "Malop",
    s.dtb AS "DTB",
    l.tenlop AS "Tenlop" 
FROM sinhvien s 
LEFT JOIN lop l ON s.malop=l.malop 
WHERE (s.dtb > 7) AND (s.gt = "nu" ) 
ORDER BY s.dtb DESC '''
cursor.execute(query2)
rows=cursor.fetchall()
col21=10
col22=13
col23=10
col24=10
col25=10
col26=10
tieude2=f"| {'Masv':<{col21}} | {'Tensv':<{col22}} | {'Gioitinh':<{col23}} | {'Malop':<{col24}} | {'DTB':<{col25}} | {'Tenlop':<{col26}} |"
dorong2=f"| {'-' * col21}-|-{'-' * col22}-|-{'-' * col23}-|-{'-' * col24}-|-{'-' * col25}-|-{'-' * col26} |"
print(tieude2)
print(dorong2)
for masv, tensv, gt, malop, dtb, tenlop in rows:
    print(f"| {masv:<{col21}} | {tensv:<{col22}} | {gt:<{col23}} | {malop:<{col24}} | {dtb:<{col25}} | {tenlop:<{col26}} |")

conn.commit()
conn.close()
