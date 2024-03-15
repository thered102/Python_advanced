from tkinter import *
import serial
import continuous_threading

wd = Tk()
wd.geometry('600x400')
wd.title('Giao diện giám sát & điều khiển')
conn = serial.Serial('COM7', baudrate=9600, timeout=1)
def on():
    data = 'S'
    conn.write(data.encode('utf-8'))
def off():
    data = 'A'
    conn.write(data.encode('utf-8'))
bt_on = Button(wd, text='On', command=on)
bt_on.pack()
bt_off = Button(wd, text='Off', command=off)
bt_off.pack()


if __name__ == '__main__':

    mainloop()