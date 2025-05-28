import math
a=int(input("nhap so a: "))
b=int(input("nhap so a: "))
c=int(input("nhap so a: "))
if(a==0):
    print("phuong trinh vo nghiem")
    if(b==0):
        print("phuong trinh vo nghiem")
    else:
        print("phuong trinh co 1 nghiem kep: "+ str(-b/c))

d=b**2-4*a*c

if(d>0):
    x1=float((-b+math.sqrt(d))/(2*a))
    x2=float((-b-math.sqrt(d))/(2*a))
    print("pt có 2 nghiem phan biet:")
    print("x1= "+ str(x1))
    print("x2= "+ str(x2))
elif(d<0):
        print("pt vô nghiệm")   
else:
    print("pt có 1 nghiệm kép"+str(-b/2*a))