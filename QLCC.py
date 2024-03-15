from QLNS_HDT import QLNS

class QLCC(QLNS):
    def __init__(self, gen, hoten, bophan, T1=0, T2=0, T3=0):
        super().__init__(gen, hoten, bophan)
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.csdlcc = {}
        # self.csdlcc = {self.gen:{'magen': self.gen, 'hoten': self.hoten, 'T1': self.T1, 'T2': self.T2, 'T3': self.T3}}

    def hienthi_cc(self):
        if self.csdl.__len__() == 0:
        # if self.csdlcc.__len__() == 0:
            print(' Cơ sở dữ liệu trống ')
        else:
            print('Mã gen\t\tHọ tên\t\tT1\t\tT2\t\tT3')
            for i in self.csdl:
                self.csdlcc.setdefault(i)
                self.csdlcc[i] = {'magen': self.gen, 'hoten': self.hoten, 'T1': self.T1, 'T2': self.T2, 'T3': self.T3}
                print(f'{self.csdlcc[i]["magen"]}\t\t{self.csdlcc[i]["hoten"]}\t\t{self.csdlcc[i]["T1"]}\t\t{self.csdlcc[i]["T2"]}\t\t{self.csdlcc[i]["T3"]}')
            # for i in self.csdlcc:
            #     print(f'{self.csdlcc[i]["magen"]}\t\t{self.csdlcc[i]["hoten"]}\t\t{self.csdlcc[i]["T1"]}\t\t{self.csdlcc[i]["T2"]}\t\t{self.csdlcc[i]["T3"]}')

    def hienthi_cc2(self, get_csdl):
        if get_csdl.__len__() == 0:
        # if self.csdlcc.__len__() == 0:
            print(' Cơ sở dữ liệu trống ')
        else:
            print('Mã gen\t\tHọ tên\t\tT1\t\tT2\t\tT3')
            for i in self.csdl:
                self.csdlcc.setdefault(i)
                self.csdlcc[i] = {'magen': self.gen, 'hoten': self.hoten, 'T1': self.T1, 'T2': self.T2, 'T3': self.T3}
                print(f'{self.csdlcc[i]["magen"]}\t\t{self.csdlcc[i]["hoten"]}\t\t{self.csdlcc[i]["T1"]}\t\t{self.csdlcc[i]["T2"]}\t\t{self.csdlcc[i]["T3"]}')

    def show_update(self):
        print('Mã gen\t\tHọ tên\t\tT1\t\tT2\t\tT3')
        # print(f'{self.csdlcc[manv]["magen"]}\t\t{self.csdlcc[manv]["hoten"]}\t\t{self.csdlcc[manv]["T1"]}\t\t{self.csdlcc[manv]["T2"]}\t\t{self.csdlcc[manv]["T3"]}')
        for i in self.csdlcc:
            print(f'{self.csdlcc[i]["magen"]}\t\t{self.csdlcc[i]["hoten"]}\t\t{self.csdlcc[i]["T1"]}\t\t{self.csdlcc[i]["T2"]}\t\t{self.csdlcc[i]["T3"]}')

    def dongbocsdl(self, csdl):
        for i in csdl:
            if i not in self.csdlcc:
                self.csdlcc.setdefault(i)
                self.csdlcc[i] = {'magen': csdl[i]['magen'], 'hoten': csdl[i]['hoten'], 'T1': 0, 'T2': 0, 'T3': 0}

    def chamcong(self):
        manv = input("Nhập mã nhân viên chấm công: " )
        while manv not in self.csdlcc:
            print("Nhân viên chưa có trong csdl")
            manv = input("Nhập mã nhân viên chấm công: ")
        while True:
            print("Chấm công tháng 1: nhấn 1")
            print("Chấm công tháng 2: nhấn 2")
            print("Chấm công tháng 3: nhấn 3")
            print("Thoat: nhấn 4")
            lc = input("Chọn tháng chấm công")
            if lc == '1':
                t1 = int(input("Nhập công tháng 1"))
                self.csdlcc[manv]['T1'] = t1
            elif lc == '2':
                t2 = int(input("Nhập công tháng 2"))
                self.csdlcc[manv]['T2'] = t2
            elif lc == '3':
                t3 = int(input("Nhập công tháng 3"))
                self.csdlcc[manv]['T3'] = t3
            elif lc == '4':
                break
            else:
                print("Lua chon theo yeu cau plz")
        # self.show_update(manv)
if __name__ == '__main__':
    qlns = QLNS('2023001', 'nguyen van a', 'main')
    # qlns.themcsdl()
    qlcc = QLCC(qlns.gen, qlns.hoten, qlns.dept)
    qlcc.hienthi_cc()
    qlcc.chamcong()