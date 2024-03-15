class QLNS:

    def __init__(self, gen, hoten, dept):
        self.gen = gen
        self.hoten = hoten
        self.dept = dept
        self.csdl = {self.gen:{'magen': self.gen, 'hoten': self.hoten, 'bophan': self.dept}}

    def soluong(self):
        return self.csdl.__len__()
    
    def hienthi(self):
        if self.soluong() == 0:
            print(' Cơ sở dữ liệu trống ')
        else:
            print('Mã gen\t\tHọ tên\t\tBộ phận')
            for i in self.csdl:
                print(f'{self.csdl[i]["magen"]}\t\t{self.csdl[i]["hoten"]}\t\t{self.csdl[i]["bophan"]}')

    def themcsdl(self):
        sl_new = int(input('Nhập số lượng nhân viên mới cần thêm : '))
        for i in range(self.soluong() + 1, self.soluong() + sl_new + 1):
            gen = input(f'Nhập số GEN cần thêm thứ {i} ')
            while gen in self.csdl:
                print('Nhân viên đã tồn tại')
                gen = input(f'Nhập số GEN cần thêm thứ {i} ')
            self.csdl.setdefault(gen)
            self.csdl[gen] = {'magen': '', 'hoten': '', 'bophan': ''}
            self.csdl[gen]['magen'] = gen
            self.csdl[gen]['hoten'] = input('Nhập tên ')
            self.csdl[gen]['bophan'] = input('Nhập Dept : ')

    def suacsdl(self):
        manv = int(input('Nhập mã nhân viên cần sửa : '))
        while manv not in self.csdl:
            print('ma nv ko ton tai')
            manv = input("nhap ma gen nv: ")
        while True:
            print("Nhập 1: sửa tên")
            print("Nhập 2: sửa bộ phận")
            print("Nhập 3: Thoát")
            nh = input("Nhập lựa chọn của bạn")
            if nh == '1':
                self.csdl[manv]['hoten'] = input("Nhập họ tên mới")
            elif nh == '2':
                self.csdl[manv]['bophan'] = input("Nhập bộ phận mới")
            elif nh == '3':
                break
            else:
                print("Nhập theo đúng yêu cầu")
            print('Mã gen\t\tHọ tên\t\tBộ phận')
            print(f'{self.csdl[manv]["magen"]}\t\t{self.csdl[manv]["hoten"]}\t\t{self.csdl[manv]["bophan"]}')

    def delcsdl(self):
        gen = input('Nhập mã số nhân viên muốn xóa: ')
        while gen not in self.csdl:
            print("Không tìm thấy mã GEN")
            gen = input('Nhập mã số nhân viên muốn xóa: ')
        print("Thông tin nv bị xóa")
        print('Mã gen\t\tHọ tên\t\tBộ phận')
        print(f'{self.csdl[gen]["magen"]}\t\t{self.csdl[gen]["hoten"]}\t\t{self.csdl[gen]["bophan"]}')
        del self.csdl[gen]

    def main(self):
        while True:
            lc = self.title()
            if lc == 1:
                self.hienthi()
            elif lc == 2:
                self.themcsdl()
            elif lc == 3:
                self.suacsdl()
            elif lc == 4:
                self.delcsdl()
            elif lc == 5:
                break
            else:
                print('Nhập nội dung yêu cầu')

# sevt = QLNS('2024001','nguyen van a', 'main')
# sevt.hienthi()
# sevt.themcsdl()
# sevt.hienthi()
# sevt.suacsdl()
# sevt.delcsdl()
# sevt.hienthi()