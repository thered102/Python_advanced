from tkinter import *
from tkinter import messagebox
from tkinter import ttk
wd = Tk()
wd.geometry('300x200')
wd.title('MessageBox')
def msg():
    messagebox.showinfo('Information', 'xin chào các ban')
    messagebox.showerror('Error', 'Đã xảy ra sự cố')
    messagebox.showwarning('Warning', 'warning content')
    messagebox.askquestion('Ask question', 'Bạn có muốn tiếp tục?')
    messagebox.askyesno('Yes|No', 'bạn có muốn logout?')
    messagebox.askokcancel('OK - Cancel', 'Bạn có chắc chắn')
    messagebox.askretrycancel('Retry', 'Đã xảy ra ỗi, bạn có muốn thử lại?')
Button(wd, text='Kiểm tra', command=msg).pack()
n = StringVar()
thang = ttk.Combobox(wd, textvariable=n, width=15)
thang['values'] = ('Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12')
thang.current(0)
thang.pack()
mainloop()