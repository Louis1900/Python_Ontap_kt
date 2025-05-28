#1.kiểm tra 1 số có phải số chính phương không
#sử dụng một vòng lặp để kiểm tra từ 0 đến n để xem có một số nào đó mà bình phương bằng n không. 
def kt(n):
    for i in range(0, n):
        if i * i == n:
            return True
    return False
num = int(input("Nhap so can kt: "))
if kt(num):
    print(f"{num} là số chính phương.")
else:
    print(f"{num} không phải là số chính phương.")

#---------------------------------------------------------------------------------------------

#2.nhap so n, tim so chinh phuong trong khoang tu 1->n
#for kt từng số từ 1 đến n-1. Nếu bình phương của số đó vẫn nhỏ hơn n, chúng ta thêm bình phương của nó vào danh sách perfect_squares.
#Nếu bình phương của số vượt quá n, chúng ta dừng vòng lặp bằng break. Kết quả cuối cùng là danh sách các số chính phương nhỏ hơn n.
def list_perfect_squares(n):
    perfect_squares = []
    for i in range(1, n):
        if i * i < n:
            perfect_squares.append(i * i)
        else:
            break
    return perfect_squares
n = int(input("Nhap so can kt: "))
result = list_perfect_squares(n)
print(f"Các số chính phương nhỏ hơn {n} là: {result}")

#---------------------------------------------------------------------------------------------

#3.nhap day, tim so chinh phuong tu day do
daysaukhikt=[]
def kt(n):
    for i in range(0, n):
        if i * i == n:
            return n
    return False

n = input("Nhap day cach nhau bang dau phay: ")
a=n.split(',')
dayint = list(map(int,a))

for i in dayint:
    val = kt(i)
    if val != False:
        daysaukhikt.append(val)

print("day so chinh phuong la:")
print(daysaukhikt)