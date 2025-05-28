class Xe:
    def __init__(self):
        self.tenxe=""
        self.tocdo=0
    def hienthi(self):
        print("Tên xe:"+self.tenxe)
        print(f"Tốc độ {self.tocdo} km/h")
    def nhapdl(self):
        self.tenxe=input("Nhap ten xe: ")
        self.tocdo=float(input("Nhap toc do(km): "))

class Oto(Xe):
    def __init__(self):
        super().__init__()
        self.thnl=0    
    def nhapdl(self):
        super().nhapdl()
        self.thnl=int(input("Nhap muc tieu hao nl(L): "))
    def hienthi(self):
        super().hienthi()
        print("Mức tiêu hao nl: "+str(self.thnl)+" L/100km")
        print(f"Thời gian xe đi được 100km là: {self.time():.2f} gio")
    def time(self):
        t=100/self.tocdo
        return t

dsxe=[]
n=int(input("Nhap so luong xe: "))
for i in range(n):
    o = Oto()
    print(f"Nhap info xe thu {i+1}: ")
    o.nhapdl()
    dsxe.append(o)

print("----------------------")
print("\ndanh sach xe")
for i in dsxe:
    i.hienthi()
    #Tại sao chưa tạo đối tượng trong vòng for này mà i vẫn dùng được hàm hienthi() của class?
    #Vì i đã là một đối tượng trước đó rồi. Ta đã tạo các đối tượng Oto() trong vòng for trước đó và thêm chúng vào danh sách dsxe
    #Nên: dsxe đang chứa các đối tượng Oto. Biến i chính là mỗi đối tượng đó. Mà Oto có hàm hienthi(), nên bạn hoàn toàn có thể gọi i.hienthi().
    print("----------------------")




