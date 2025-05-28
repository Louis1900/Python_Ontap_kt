#3.nhap day, tim so hh tu day do
daysaukhikt=[]
def kt(n):
    tong=0
    for i in range(1, n):
        if (n % i == 0):
            tong += i
    if (tong == n):
        return tong

n = input("Nhap day cach nhau bang dau phay: ")
a=n.split(',')
dayint = list(map(int,a))

for i in dayint:
    val = kt(i)
    if val != None:
        daysaukhikt.append(val)

print("day so hoan hao la:")
print(daysaukhikt)