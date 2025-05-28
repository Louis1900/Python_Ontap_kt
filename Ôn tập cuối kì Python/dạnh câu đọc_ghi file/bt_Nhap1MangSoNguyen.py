import csv

def kt(n):
    tong = 0
    for i in range(1, n):
        if (n % i == 0):
            tong += i
    if (tong == n):
        return tong
        


def ghi(filename):
    dayso= []
    n = int(input("Nhap so luong: "))
    val = 0
    for i in range(1,n):
        val = kt(i)
        dayso.append(val)

    with open(filename, mode='w',newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([dayso])

def doc(filename):
    with open(filename, mode='r',newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

filename = "dayso.csv"
ghi(filename)
doc(filename)

