class Sach:
    def __init__(self):
        self.id=""
        self.tensach=""
        self.tacgia=""
        self.namph=""
    def nhapdl(self):
        self.id=input("Nhap id: ")
        self.tensach=input("Nhap ten sach: ")
        self.tacgia=input("Nhap tac gia: ")
        self.namph=input("Nhap nam pphat hanh: ")
    def ht(self):
        print(f"id: {self.id}")
        print(f"ten sach: {self.tensach}")
        print(f"tacgia: {self.tacgia}")
        print(f"nam phat hanh: {self.namph}")

class QLsach(Sach):
    def __init__(self):
        self.dssach=[]
    def themsach(self, sach):
        self.dssach.append(sach)
    def hienthi(self):
        print("danh sach sach da nhap: ")
        for i in self.dssach:
            i.ht()
            print("\n")
    def find(self, tentg):
        kqfind=[]
        for i in self.dssach:
            # if i.tacgia.lower() == tentg.lower(): hoặc
            if tentg.lower() in i.tacgia.lower():  # so sánh không phân biệt hoa thường
                kqfind.append(i)
        return kqfind

qls = QLsach()
#them sach
n=int(input("Nhap so luong sach: "))
for i in range(n):
    sach = Sach()
    print(f"Nhap info sach thu {i+1}: ")
    sach.nhapdl()
    qls.themsach(sach)
print("---------------------")
#hien thi ds sach
qls.hienthi()
#tim kem theo tac gia
print("---------------------")
name=input("Nhap ten tac gia can tim: ")
kq=qls.find(name)
if kq:
    for i in kq:
        i.ht() #chỗ này phải là ht() ở class cha
        print("-----------------")
else:
    print("khong tim thay")