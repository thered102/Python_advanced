csdl = {2023001: {'Gen': 2023001, 'Họ tên': 'Van A', 'Dept': 'Main'},
            2023002: {'Gen': 2023002, 'Họ tên': 'Thi B', 'Dept': 'Glass'}}
def title():
    print('-------------------------')
    print('Nhấn 1: Hiện thị CSDL')
    print('Nhấn 2: Thêm CSDL')
    print('Nhấn 3: Sửa CSDL')
    print('Nhấn 4: Xóa CSDL')
    print('Nhấn 5: Thoát')
    global sl,lc
    sl = len(csdl)
    lc = int(input('Nhập lựa chọn :'))
    return lc
def hienthi() :
    if sl == 0:
        print(' Cơ sở dữ liệu trống ')
    else:
        listgen = list(csdl.keys())
        print('Mã gen\t\tHọ tên\t\tBộ phận')
        for i in range(0, sl):
            gen = listgen[i]
            print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')
def themcsdl():
    sl_new = int(input('Nhập số lượng nhân viên mới cần thêm : '))
    for i in range(sl + 1, sl + sl_new + 1):
        gen = int(input(f'Nhập số GEN cần thêm thứ {i} '))

        while gen in csdl:
            print('Nhân viên đã tồn tại')
            gen = int(input(f'Nhập số GEN cần thêm thứ {i} '))
        csdl.setdefault(gen)
        name = input('Nhập tên: ')
        bophan = input('Nhập Dept : ')
        csdl[gen] = {'Gen': gen, 'Họ tên': name, 'Dept': bophan}
def suacsdl():
    gen = int(input('Nhập mã nhân viên cần sửa : '))
    if csdl.get(gen) != None:
        print('Mã gen\t\tHọ tên\t\tBộ phận')
        print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')

        field = int(input('Nhập trường cần thay đổi [1] Họ tên, [2] Bộ phận:'))

        noidung = input('Nhập nội dung thay đổi : ')
        if field == 1:
            field2 = 'Họ tên'
            csdl[gen][field2] = noidung
        elif field == 2:
            field2 = 'Dept'
            csdl[gen][field2] = noidung
        else:
            print('Nhập theo hướng dẫn')
        print('Mã gen\t\tHọ tên\t\tBộ phận')
        print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')
    else:
        print(f'Không tồn tại mã nhân viên {gen}')
def delcsdl() :
    gen = int(input('Nhập mã số nhân viên muốn xóa: '))
    print('Mã gen\t\tHọ tên\t\tBộ phận')
    print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')
    if csdl.get(gen) != None:
        del csdl[gen]
    else:
        print(f'Không tồn tại mã nhân viên {gen}')

import main_QLNS
main_QLNS.main()
# while True:
#     print('-------------------------')
#     print('Nhấn 1: Hiện thị CSDL')
#     print('Nhấn 2: Thêm CSDL')
#     print('Nhấn 3: Sửa CSDL')
#     print('Nhấn 4: Xóa CSDL')
#     print('Nhấn 5: Thoát')
#
#     sl = len( csdl )
#     lc = int(input('Nhập lựa chọn :'))
#
#     if lc == 1:
#         if sl == 0 :
#             print(' Cơ sở dữ liệu trống ')
#         else:
#             listgen = list(csdl.keys())
#             print('Mã gen\t\tHọ tên\t\tBộ phận')
#             for i in range(0,sl) :
#                 gen = listgen[i]
#                 print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')
#
#
#
#     elif lc == 2:
#         sl_new = int(input('Nhập số lượng nhân viên mới cần thêm : ') )
#         for i in range(sl+1,sl+sl_new+1) :
#             gen= int(input(f'Nhập số GEN cần thêm thứ {i} '))
#
#             while gen in csdl :
#                 print('Nhân viên đã tồn tại')
#                 gen = int(input(f'Nhập số GEN cần thêm thứ {i} '))
#             csdl.setdefault(gen)
#             name = input('Nhập tên: ')
#             bophan = input('Nhập Dept : ')
#             csdl[gen] = {'Gen': gen, 'Họ tên': name, 'Dept': bophan}
#
#     elif lc == 3:
#         gen = int(input('Nhập mã nhân viên cần sửa : '))
#         if csdl.get(gen) != None:
#             print('Mã gen\t\tHọ tên\t\tBộ phận')
#             print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')
#
#             field = int(input('Nhập trường cần thay đổi [1] Họ tên, [2] Bộ phận:'))
#
#             noidung = input('Nhập nội dung thay đổi : ')
#             if field == 1:
#                 field2 = 'Họ tên'
#                 csdl[gen][field2] = noidung
#             elif field == 2:
#                 field2 = 'Dept'
#                 csdl[gen][field2] = noidung
#             else :
#                 print('Nhập theo hướng dẫn')
#             print('Mã gen\t\tHọ tên\t\tBộ phận')
#             print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')
#         else:
#             print(f'Không tồn tại mã nhân viên {gen}')
#     elif lc ==4:
#         gen= int(input('Nhập mã số nhân viên muốn xóa: '))
#         print('Mã gen\t\tHọ tên\t\tBộ phận')
#         print(f'{csdl[gen]["Gen"]}\t\t{csdl[gen]["Họ tên"]}\t\t{csdl[gen]["Dept"]}')
#         if csdl.get(gen) != None:
#             del csdl[gen]
#         else:
#             print(f'Không tồn tại mã nhân viên {gen}')
#     elif lc == 5:
#             break
#     else:
#         print('Nhập nội dung yêu cầu')
# def main():
#     while True:
#         title()
#         if lc == 1:
#             hienthi()
#         elif lc == 2:
#             themcsdl()
#         elif lc == 3:
#             suacsdl()
#         elif lc ==4:
#             delcsdl()
#         elif lc == 5:
#                 break
#         else:
#             print('Nhập nội dung yêu cầu')
