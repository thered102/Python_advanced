import math
class GiaiPhuongTrinhBac2:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def giai(self):
        if self.a == 0:
            print("vui long nhap he so a khac 0")
        else:
            delta = self.b*self.b - 4*self.a*self.c
            if delta < 0:
                print("Phuong trinh vo nghiem")
            elif delta == 0:
                print("phuong trinh co nghiem kep =", -self.b/self.a*2)
            else:
                print("Phuong trinh co 2 nghiem:")
                print("x=", (-self.b + math.sqrt(delta))/self.a*2)
                print("y=", (-self.b - math.sqrt(delta))/self.a*2)
a = int(input("nhap he so a: "))
if str(a).isdigit():
    print("nhap sai")

b = int(input("nhap he so b: "))
c = int(input("nhap he so c: "))
gpt = GiaiPhuongTrinhBac2(a,b,c)
gpt.giai()