from tkinter import *
from tkinter import ttk
import pyodbc
wd = Tk()
wd.geometry('800x600')
wd.title("TreeView-QLNS")

def binding():
    et_bophan.delete(0, END)
    et_maNV.delete(0, END)
    et_tenNV.delete(0, END)
    # Trả về hàng đã chọn
    lc = my_tree.focus()
    # Trả về giá trị hàng đã chọn
    values = my_tree.item(lc, 'values')
    et_maNV.insert(0, values[0])
    et_tenNV.insert(0, values[1])
    et_bophan.insert(0, values[2])
def click(a):
    binding()
my_tree = ttk.Treeview(wd)
my_tree.pack()
# my_tree.bind("<Double-1>", click)
my_tree.bind("<ButtonRelease-1>", click)
# Định nghĩa các cột trong bảng
my_tree['columns'] = ['Magen', 'ht', 'bp']
# Tạo các cột
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('Magen', width=100, anchor=CENTER)
my_tree.column('ht', width=100, anchor=W)
my_tree.column('bp', width=100, anchor=CENTER)
# Nhãn cho các cột
my_tree.heading('#0', text="", anchor=CENTER)
my_tree.heading('Magen', text="Mã Gen", anchor=CENTER)
my_tree.heading('ht', text="Họ tên", anchor=CENTER)
my_tree.heading('bp', text="Bộ phận", anchor=CENTER)

# Thêm CSDL vào bảng

dem = 0
fr = Frame(wd)
fr.pack()
lb_maNV = Label(fr, text='Mã Nhân Viên:')
lb_tenNV = Label(fr, text='Tên Nhân Viên:')
lb_bophan = Label(fr, text='Bộ phận')
maNV = StringVar()
et_maNV = Entry(fr, textvariable=maNV)
tenNV = StringVar()
et_tenNV = Entry(fr, textvariable=tenNV)
bophan = StringVar()
et_bophan = Entry(fr, textvariable=bophan)
lb_maNV.grid(row=0, column=0)
lb_tenNV.grid(row=1, column=0)
lb_bophan.grid(row=2, column=0)
et_maNV.grid(row=0, column=1)
et_tenNV.grid(row=1, column=1)
et_bophan.grid(row=2, column=1)
connect = pyodbc.connect('Driver={SQL Server};'
                         'Server=LAPTOP-SATTI01\SQLEXPRESS;'
                         'Database=QL;'
                         'Trusted_Connection=yes')
cursor = connect.cursor()
def hienthi():
    cursor.execute('select * from QLNS')
    csdl = cursor.fetchall()
    global dem
    for j in my_tree.get_children():
        my_tree.delete(j)
    for i in csdl:
        dem += 1
        my_tree.insert('', index='end', iid=str(dem), text='', values=(i[0], i[1], i[2]))
bt_hienthi = Button(wd, text='Hiển thị', width=20, command=hienthi)
bt_hienthi.pack()

def them():
    new_maNV = int(maNV.get())
    new_tenNV = tenNV.get()
    new_bophan = bophan.get()
    cursor.execute(f"insert into QLNS values ('{new_maNV}', '{new_tenNV}', '{new_bophan}')")
    cursor.commit()
    # thêm vào treeview
    global dem
    dem += 1
    my_tree.insert('', index='end', iid=str(dem), text='', values=(new_maNV, new_tenNV, new_bophan))
    # xóa input
    et_bophan.delete(0, END)
    et_maNV.delete(0, END)
    et_tenNV.delete(0, END)

bt_them = Button(wd, text='Thêm', width=20, command=them)
bt_them.pack()

def sua():
    new_maNV = int(maNV.get())
    new_tenNV = tenNV.get()
    new_bophan = bophan.get()
    cursor.execute(f"update QLNS set Hoten='{new_tenNV}', Bophan='{new_bophan}' where MaGen='{new_maNV}'")
    cursor.commit()
    lc = my_tree.focus()
    my_tree.item(lc, text='', values=(new_maNV, new_tenNV, new_bophan))

bt_sua = Button(wd, text='Sửa', width=20, command=sua)
bt_sua.pack()

def xoa():
    xoa_maNV = int(maNV.get().strip())
    cursor.execute(f"delete QLNS where MaGen='{xoa_maNV}'")
    cursor.commit()
    lc = my_tree.selection()[0]
    my_tree.delete(lc)
bt_xoa = Button(wd, text='Xóa 1 bản ghi', width=20, command=xoa)
bt_xoa.pack()

def xoa2():
    lc = my_tree.selection()
    for j in lc:
        xoa_maNV = my_tree.item(j, 'values')[0]
        cursor.execute(f"delete QLNS where MaGen='{xoa_maNV}'")
        cursor.commit()
        my_tree.delete(j)
bt_xoa2 = Button(wd, text='Xóa nhiều bản ghi', width=20, command=xoa2)
bt_xoa2.pack()

def xoatatca():
    cursor.execute(f"delete from QLNS")
    cursor.commit()
    for i in my_tree.get_children():
        my_tree.delete(i)
bt_xoatatca = Button(wd, text='Xóa tất cả', width=20, command=xoatatca)
bt_xoatatca.pack()

mainloop()