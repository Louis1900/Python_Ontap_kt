#nhap 2 so tim ucln va bcnn
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))

# Lưu lại giá trị gốc để tính BCNN sau này
x = a
y = b

# Tính UCLN bằng thuật toán Euclid (trừ dần)
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

# Tính BCNN từ UCLN
ucln = a #Sau vòng lặp while a != b, lúc này a và b đã bằng nhau, và đó chính là Ước chung lớn nhất (UCLN)
bcnn = (x * y) // ucln

print("UCLN là:", ucln)
print("BCNN là:", bcnn)
