from QLNS_HDT import QLNS
from QLCC import QLCC
qlns = QLNS('2024001','nguyen van a', 'main')
qlcc = QLCC(qlns.gen,qlns.hoten, qlns.dept)
def main_qlns():
    while True:
        print('Nhấn 1: Hiện thị csdl')
        print('Nhấn 2: Thêm csdl')
        print('Nhấn 3: Sửa csdl')
        print('Nhấn 4: Xóa csdl')
        print('Nhấn 5: Thoát')
        lc = int(input('Nhập lựa chọn :'))
        if lc == 1:
            qlns.hienthi()
        elif lc == 2:
            qlns.themcsdl()
            qlns.hienthi()
        elif lc == 3:
            qlns.suacsdl()
        elif lc ==4:
            qlns.delcsdl()
        elif lc == 5:
            confirm_exit = input("Bạn có muốn thoát ko Y/N?")
            if confirm_exit == 'y' or confirm_exit == 'Y':
                break
        else:
            print('Nhập nội dung theo yêu cầu')
def main_qlcc():
    qlcc.dongbocsdl(qlns.csdl)
    while True:
        print('Nhấn 1: Hiện thị csdlcc')
        print('Nhấn 2: Chấm công')
        print('Nhấn 3: Sửa chấm công')
        print('Nhấn 4: Thoát')
        lc = int(input('Nhập lựa chọn :'))
        if lc == 1:
            qlcc.show_update()
            # qlcc.hienthi_cc()
        elif lc == 2:
            qlcc.chamcong()
        elif lc == 3:
            pass
        elif lc == 4:
            confirm_exit = input("Bạn có muốn thoát ko Y/N?")
            if confirm_exit == 'y' or confirm_exit == 'Y':
                break
        else:
            print('Nhập nội dung theo yêu cầu')
if __name__ == '__main__':
    while True:
        print("Nhap 1: QLNS")
        print("Nhap 2: QLCC")
        print("Nhap 3: Exit")
        lc = input("Nhap lua chon")
        if lc == '1':
            main_qlns()
        if lc == '2':
            print('QLNS_CSDL: ', qlns.csdl)
            main_qlcc()
        if lc == '3':
            confirm_exit = input("Bạn có muốn thoát ko Y/N?")
            if confirm_exit == 'y' or confirm_exit == 'Y':
                break
        else:
            print("Nhap lua chon")