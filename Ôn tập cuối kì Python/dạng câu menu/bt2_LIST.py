def mh_menu():
    print("\n MENU: ")
    print("\n 1.Them so vao ds.")
    print("\n 2.Sua so trong ds ")
    print("\n 3.Xoa so khoi ds ")
    print("\n 4.Tim kiem so trong ds ")
    print("\n 5.Hien thi ds ")
    print("\n 0.Thoat chuong trinh ")

# ham them
def Add_num(number):
    val = int(input("Nhap so can them: "))
    index = input("Nhap vi tri(Enter de them so vao cuoi)")

    if index.strip() == "":
        number.append(val)
        print("da them "+str(val)+" vao cuoi ds")
    else:
        index = int(index)
        if 0<=index<=len(number):
            number.insert(index,val)
            print("Da them "+str(val)+" vao vi tri" +str(index))
        else:
            print("Vi tri k hop le!")


# ham sua
def Update(number):
    index = int(input("nhap vt can sua: "))
    if 0 <= index < len(number):
        gtmoi = int(input("Nhap gt moi: "))
        gtcu = number[index]
        number[index] = gtmoi
        print("da cap nhat gt!")
    else:
        print("vi tri sua k hop le!")


#ham xoa
def Xoa(number):
    print("1.xoa theo gt")
    print("2.xoa theo vi tri")
    choice = input("chon cach xoa: ")
    if choice == "1":
        val = int(input("Nhap gt can xoa: "))
        if val in number:
            number.remove(val)
            print("da xoa gt")
        else:
            print("gt k ton tai")
    elif choice == "2":
        index = int(input("nhap vt van xoa:"))
        if 0 <= index < len(number):
            xoa_gt = number.pop(index)
            print("da xoa gt "+str(xoa_gt)+" tai vi tri "+str(index))
        else:
            print("vi tri k hop le!")
    else:
        print("lua chon k hop le!")


# ham tim kiem
def Timkiem(number):
    val = int(input("Nhap so can tim: "))
    for num in number:
        if num == val:
            print("trong list co gt nay!")
        else:
            print("k tim thay gt can tim!")



def Hienthi(num):
    for index, value in enumerate(num):
        print("danh sach la: " + str(index)+": "+str(value))

# ham main
def main():
    num=[12,34,56,67,78]
    while True:
        mh_menu()
        choice=input(" Nhap lc: ")

        if choice == "1":
            Add_num(num)
        elif choice == "2":
            Update(num)
        elif choice == "3":
            Xoa(num)
        elif choice == "4":
            Timkiem(num)
        elif choice == "5":
            Hienthi(num)
        elif choice == "0":
            print("bye bye")
            break
        else:
            print("lua chon khong hop le, vui long nhap lai!")


if __name__ == "__main__":
    main()
