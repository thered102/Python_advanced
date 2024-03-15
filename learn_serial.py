from tkinter import *
import serial
import continuous_threading

wd = Tk()
wd.geometry('600x400')
wd.title('Giao diện giám sát')

conn = serial.Serial('COM7', baudrate=9600, timeout=1)
def nd_da():
    data = conn.readline().decode('utf-8') # Đọc dữ liệu từ phần cứng (kiểu byte), chuyển kiểu byte sang kiểu dữ liệu python
    if len(str(data)) != 0:
        x = str(data).split('#')[0].replace('@', '')
        y = str(data).split('#')[1].replace('$', '')
        nd.config(text=f'Nhiệt độ: {x}')
        da.config(text=f'Độ ẩm: {y}')

fun = continuous_threading.PeriodicThread(1, nd_da)
fun.start()
nd = Label(wd, text=f'Nhiệt độ:')
da = Label(wd, text=f'Độ ẩm:')
nd.pack()
da.pack()
mainloop()
