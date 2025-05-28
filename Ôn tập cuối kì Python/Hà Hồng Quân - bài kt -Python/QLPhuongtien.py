class Xe:
    def __init__(self):
        self.name=""
        self.speed=0.0
        
    def nhapinfo(self):
        self.name=input("Nhap ten xe: ")
        self.speed=float(input("Nhap toc do: "))

    def hienthi(self):
        print("ten xe: "+str(self.name)
              +"\ntoc do: "+str(self.speed)+" km/h")
        
class Oto(Xe):
    def __init__(self):
        super().__init__()
        self.fuel=0

    def nhapinfo(self):
        super().nhapinfo()
        self.fuel=int(input("Nhap muc tieu hao nhien lieu: "))

    def tinhthoigian(self):
        time = 100 / self.speed
        return time
    
    def hienthi(self):
        super().hienthi()
        print("muc tieu hao nl: "+str(self.fuel)+"L/100km")

dsxe = []
n=int(input("so luong xe: "))
for i in range(n):
    oto = Oto()
    oto.nhapinfo()
    dsxe.append(oto)
print("----------------------")
print("ds xe hien tai: ")
for i in dsxe:
    i.hienthi() #Tại sao chưa tạo đối tượng trong vòng for này mà i vẫn dùng được hàm hienthi() của class?
    #Vì i đã là một đối tượng trước đó rồi. Ta đã tạo các đối tượng Oto() trong vòng for trước đó và thêm chúng vào danh sách dsxe
    #Nên: dsxe đang chứa các đối tượng Oto. Biến i chính là mỗi đối tượng đó. Mà Oto có hàm hienthi(), nên bạn hoàn toàn có thể gọi i.hienthi().
    print("---------------------")

# print("thoi gian cac xe di duoc 100km:")
# for i in dsxe:
#     print("xe"+str(i)+str(i.tinhthoigian()))
        
print("thoi gian cac xe di duoc 100km:")
for i in dsxe:
    print(f"{i.name}: {i.tinhthoigian():.2f} gio") #Oto kế thừa từ Xe, mà trong lớp Xe có thuộc tính self.name, nên i.name là hoàn toàn hợp lệ.
