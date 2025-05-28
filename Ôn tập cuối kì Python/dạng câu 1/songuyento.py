#1.kt 1 so nguyen to
# n = int(input("Nhập vào một số tự nhiên: "))
# for i in range(2, n):
#     if n % i == 0:
#         print(f"Số {n} không phải số nguyên tố")
#         break
# else:
#     print(f"Số {n} là số nguyên tố")

#---------------------------------------------------------------------------------------------

#2.so nguyen to tu 1->n
# def kt(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# def liet_ke_nt(n):
#     dayso=[]
#     for i in range(2, n): 
#         if kt(i):
#             dayso.append(i)
#     return dayso

# n = int(input("Nhập vào một số tự nhiên: "))
# kq = liet_ke_nt(n)
# print(f"Các số nguyên tố nhỏ hơn {n} là: {kq}")


#---------------------------------------------------------------------------------------------


#3.nhap 1 day, tim so nguyen to trong day do
daysaukhikt=[]
def kt(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return n

n = input("Nhap day cach nhau bang dau phay: ")
a=n.split(',')
dayint = list(map(int,a))

for i in dayint:
    val = kt(i)
    if val != False:
        daysaukhikt.append(val)

print("day so nguyen to la:")
print(daysaukhikt)