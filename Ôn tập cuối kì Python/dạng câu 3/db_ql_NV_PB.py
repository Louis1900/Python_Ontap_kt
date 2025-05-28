#đề bài:
# Mục tiêu: GROUP BY, tính tổng, đếm
# +)CSDL:phongban(ma_pb, ten_pb)
#        nhanvien(ma_nv, ten_nv, luong, ma_pb)
# +)Yêu cầu:
#       Tính tổng lương theo từng phòng ban.
#       Đếm số lượng nhân viên mỗi phòng.
#       Tìm phòng có nhân viên lương cao nhất.

import sqlite3

conn = sqlite3.connect("db_phongban.db")
cursor = conn.cursor()


# cursor.execute("""CREATE TABLE IF NOT EXISTS phongban(
#                maphong TEXT PRIMARY KEY,
#                tenphong TEXT NOT NULL)""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS nhanvien(
#                 manv TEXT PRIMARY KEY,
#                 tennv TEXT NOT NULL,
#                 gt TEXT NOT NULL,
#                 maphong TEXT NOT NULL,
#                 luong FLOAT NOT NULL,
#                 FOREIGN KEY (maphong) REFERENCES phongban(maphong))""")


pb = [('kt', 'Kế toán'), 
      ('it', 'CNTT'), 
      ('ns', 'Nhân sự'), 
      ('bh', 'Bảo hiểm'), 
      ('kd', 'Kinh doanh')]
cursor.executemany("INSERT INTO phongban VALUES (?,?)", pb)
nv = [('nv1', 'Nguyễn Văn A', 'nam', 'kt', 9000000),
    ('nv2', 'Trần Thị B', 'nu', 'it', 10000000),
    ('nv3', 'Lê Văn C', 'nam', 'kt', 8500000),
    ('nv4', 'Phạm Thị D', 'nu', 'ns', 9500000),
    ('nv5', 'Ngô Thị E', 'nu', 'kt', 9200000)]
cursor.executemany("INSERT INTO nhanvien VALUES (?,?,?,?,?)", nv)


print("Cau 1:Nhân viên thuộc phòng 'Kế toán'")
query1 = '''SELECT nv.manv, nv.tennv, nv.gt, nv.luong, pb.tenphong 
FROM nhanvien nv 
LEFT JOIN phongban pb ON nv.maphong=pb.maphong 
WHERE tenphong="Kế toán"'''
cursor.execute(query1)
rows=cursor.fetchall()
print(f"| {'Ma nv':<10} | {'Ten nv':<15} | {'Gioi tinh':<10} | {'Luong':<10} | {'Ten phong':<15} |")
print(f"| {'-'*10}-|-{'-'*15}-|-{'-'*10}-|-{'-'*10}-|-{'-'*15} |")
for manv, tennv, gt, luong, tenphong in rows:
    print(f"| {manv:<10} | {tennv:<15} | {gt:<10} | {luong:<10} | {tenphong:<15} |")



print("\nCâu 2: Nữ, lương > 8 triệu, giảm dần")
query2='''SELECT nv.manv, nv.tennv, nv.gt, nv.luong, pb.tenphong 
FROM nhanvien nv 
JOIN phongban pb ON nv.maphong = pb.maphong 
WHERE nv.gt = "nu" AND nv.luong > 8000000 
ORDER BY nv.luong DESC'''
cursor.execute(query2)
rows = cursor.fetchall()
print(f"| {'MaNV':<8} | {'TenNV':<20} | {'GT':<6} | {'Luong':<10} | {'Phong':<12} |")
print(f"| {'-'*8}-|-{'-'*20}-|-{'-'*6}-|-{'-'*10}-|-{'-'*12} |")
for manv, tennv, gt, luong, tenphong in rows:
    print(f"| {manv:<8} | {tennv:<20} | {gt:<6} | {luong:<10,.0f} | {tenphong:<12} |")

conn.commit()
conn.close()