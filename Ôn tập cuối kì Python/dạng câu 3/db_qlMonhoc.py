import sqlite3

conn = sqlite3.connect("db_qlmonhoc.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS monhoc(
#     mamon TEXT PRIMARY KEY,
#     tenmon TEXT NOT NULL)""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS diem(
#     masv TEXT,
#     hoten TEXT,
#     mamon TEXT,
#     diem FLOAT,
#     PRIMARY KEY (masv, mamon),
#     FOREIGN KEY (mamon) REFERENCES monhoc(mamon))""")

# Dữ liệu mẫu
mh = [('mh1', 'Toán cao cấp'), ('mh2', 'Xác suất thống kê'), ('mh3', 'Kỹ thuật lập trình')]
diem = [
    ('sv1', 'Nguyễn Văn A', 'mh1', 8.5),
    ('sv2', 'Trần Thị B', 'mh2', 9.0),
    ('sv3', 'Lê Văn C', 'mh1', 7.0),
    ('sv4', 'Phạm Thị D', 'mh3', 8.7),
    ('sv5', 'Ngô Văn E', 'mh1', 9.3)
]
cursor.executemany('INSERT INTO monhoc VALUES (?, ?)', mh)
cursor.executemany('INSERT INTO diem VALUES (?, ?, ?, ?)', diem)

# Câu 1
print("Câu 1: Sinh viên học 'Toán cao cấp'")
cursor.execute('''
SELECT d.masv, d.hoten, d.diem, m.tenmon
FROM diem d
JOIN monhoc m ON d.mamon = m.mamon
WHERE m.tenmon = "Toán cao cấp"
''')
rows = cursor.fetchall()
print(f"| {'MaSV':<8} | {'HoTen':<20} | {'Diem':<5} | {'MonHoc':<20} |")
print(f"| {'-'*8}-|-{'-'*20}-|-{'-'*5}-|-{'-'*20} |")
for masv, hoten, diem, tenmon in rows:
    print(f"| {masv:<8} | {hoten:<20} | {diem:<5} | {tenmon:<20} |")

# Câu 2
print("\nCâu 2: Sinh viên có điểm >= 8, giảm dần")
cursor.execute('''
SELECT d.masv, d.hoten, d.diem, m.tenmon
FROM diem d
JOIN monhoc m ON d.mamon = m.mamon
WHERE d.diem >= 8
ORDER BY d.diem DESC
''')
rows = cursor.fetchall()
print(f"| {'MaSV':<8} | {'HoTen':<20} | {'Diem':<5} | {'MonHoc':<20} |")
print(f"| {'-'*8}-|-{'-'*20}-|-{'-'*5}-|-{'-'*20} |")
for masv, hoten, diem, tenmon in rows:
    print(f"| {masv:<8} | {hoten:<20} | {diem:<5} | {tenmon:<20} |")

conn.commit()
conn.close()
