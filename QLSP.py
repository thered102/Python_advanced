from tkinter import *
wd = Tk()
wd.geometry('600x400')
wd.title('QLSP')
csdl = {1: {'maSP': 1, 'tenSP': 'Laptop', 'soluong': 10}}
def hienthi():
    if csdl.__len__() == 0:
        lb_hienthi.config(text=' Cơ sở dữ liệu trống ')
    else:
        text_hienthi = ''
        for i in csdl:
            text_hienthi += f'{csdl[i]["maSP"]}\t{csdl[i]["tenSP"]}\t{csdl[i]["soluong"]}\n'
        lb_hienthi.config(text=text_hienthi)
def them():
    new_maSP = int(maSP.get())
    new_tenSP = tenSP.get()
    new_slSP = int(slSP.get())
    # new = {'maSP': new_maSP, 'tenSP': new_tenSP, 'soluong': new_slSP}
    csdl.setdefault(new_maSP)
    csdl[new_maSP] = {'maSP': new_maSP, 'tenSP': new_tenSP, 'soluong': new_slSP}

def sua():
    sua_maSP = int(maSP.get())
    sua_tenSP = tenSP.get()
    sua_slSP = int(slSP.get())
    # new = {'maSP': new_maSP, 'tenSP': new_tenSP, 'soluong': new_slSP}
    csdl.setdefault(sua_maSP)
    csdl[sua_maSP] = {'maSP': sua_maSP, 'tenSP': sua_tenSP, 'soluong': sua_slSP}
def xoa():
    xoa_maSP = int(maSP.get())
    csdl.pop(xoa_maSP)

lb_maSP = Label(wd, text='Mã sản phẩm:')
lb_tenSP = Label(wd, text='Tên saản phẩm:')
lb_slSP = Label(wd, text='SL sản phẩm:')

maSP = StringVar()
et_maSP = Entry(wd, textvariable=maSP)
tenSP = StringVar()
et_tenSP = Entry(wd, textvariable=tenSP)
slSP = StringVar()
et_slSP = Entry(wd, textvariable=slSP)

bt_hienthi = Button(wd, text='Hiển thị CSDL', command=hienthi, height=5)
bt_them = Button(wd, text='Thêm CSDL', command=them, height=5)
bt_sua = Button(wd, text='Sửa CSDL', command=sua, height=5)
bt_xoa = Button(wd, text='Xóa CSDL', command=xoa, height=5)

lb_title = Label(wd, text='Mã sản phẩm\tTên sản phẩm\tSố lượng')
lb_hienthi = Label(wd, text='')

# Gui
lb_maSP.grid(row=0, column=0)
lb_tenSP.grid(row=1, column=0)
lb_slSP.grid(row=2, column=0)
et_maSP.grid(row=0, column=1)
et_tenSP.grid(row=1, column=1)
et_slSP.grid(row=2, column=1)
bt_hienthi.grid(row=3, column=0)
bt_them.grid(row=3, column=1)
bt_sua.grid(row=3, column=2)
bt_xoa.grid(row=3, column=3)

lb_title.grid(row=4, column=0)
lb_hienthi.grid(row=5, column=0)


mainloop()