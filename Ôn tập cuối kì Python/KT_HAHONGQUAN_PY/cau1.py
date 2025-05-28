
def kt(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return n

# def ktdsshh(ds):
#     dsshh = []
#     for i in ds:
#         if kt(i):
#             dsshh.append(i)
#     return dsshh
    
ds_shh = input("Nhap vao 1 mang cac so nguyen cach nhau bằng dau (,) : ")

danh_sach = ds_shh.split(',')

dsht = []

for i in danh_sach:
    kt(int(i))
    dsht.append(i)


for i in dsht:
    print("so hh la: "+ str(i))


# T_T
