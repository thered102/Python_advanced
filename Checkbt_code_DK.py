from tkinter import *
from tkinter import ttk
import serial
import continuous_threading

wd = Tk()
wd.geometry('600x400')
wd.title('Giao diện giám sát & điều khiển')

check_com = StringVar()
com = ttk.Combobox(wd, textvariable=check_com)
com['values'] = ('COM 1', 'COM 2', 'COM 3', 'COM 4', 'COM 5', 'COM 6', 'COM 7', 'COM 8', 'COM 9', 'COM 10')
com.current(0)
conn = serial.Serial('COM7', baudrate=9600, timeout=1)
dk = lambda x: conn.write(x.encode('utf-8'))
def device():
    if check.get() == 1:
        dk('S')
    else:
        dk('A')
check = IntVar()
chkbt = Checkbutton(wd, text='Thiết bị 1', variable=check, onvalue=1, offvalue=0, command=device)
def ketnoi():
    pass
bt_conn = Button(wd, text='Connect', command=ketnoi)
com.pack()
bt_conn.pack()
chkbt.pack()
mainloop()