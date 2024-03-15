import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import serial
import continuous_threading
import serial.tools.list_ports
from time import strftime
import pyodbc
import pandas as pd

class QLSP:
    def __init__(self):
        self.wd = Tk()
        self.status = False
        self.tongsp = 0
        self.spcao = 0
        self.sptb = 0
        self.spthap = 0
    def setupGui(self):
        self.wd.geometry('600x400')
        self.wd.title('QLSP')

        # self.lb_tongsp = Label(self.wd, text='tổng sp', background='pink', width=10, height=5).grid(row=0, column=1)
        self.lb_tongsp = Label(self.wd, text=f'{self.tongsp}', background='pink', width=10, height=5)
        self.lb_tongsp.grid(row=0, column=1)
        Label(self.wd, text='Tổng SP', width=12).grid(row=1, column=1)
        self.lb_spcao = Label(self.wd, text=f'{self.spcao}', background='purple', width=10,height=5)
        self.lb_spcao.grid(row=2, column=0)
        Label(self.wd, text='Số SP Cao', width=12).grid(row=3, column=0)
        self.lb_sptb = Label(self.wd, text=f'{self.sptb}', background='yellow', width=10,height=5)
        self.lb_sptb.grid(row=2, column=1)
        Label(self.wd, text='Số SP TB', width=12).grid(row=3, column=1)
        self.lb_spthap = Label(self.wd, text=f'{self.spthap}', background='gray', width=10,height=5)
        self.lb_spthap.grid(row=2, column=2)
        Label(self.wd, text='Số SP Thấp', width=12).grid(row=3, column=2)

        bt_start = Button(self.wd, text='Start', command=self.start, width=5, height=3)
        bt_start.grid(row=2, column=4)
        self.bt_stop = Button(self.wd, text='Stop', command=self.stop, width=5, height=3).grid(row=3, column=4)
        self.bt_cb1 =Button(self.wd, text='CB1', command=self.cambien1, width=5, height=3).grid(row=2, column=5)
        self.bt_cb2 =Button(self.wd, text='CB2', command=self.cambien2, width=5, height=3).grid(row=3, column=5)
        self.bt_cb2 =Button(self.wd, text='CB3', command=self.cambien3, width=5, height=3).grid(row=4, column=5)
        self.lb_status = Label(self.wd, text='Status:OFF', font=('Arial', 12, 'bold'), width=9)
        self.lb_status.grid(row=5,column=0)
        Label(self.wd, text='', width=3).grid(row=3, column=3)

    def main(self):
        fun1 = continuous_threading.PeriodicThread(0.1, self.tinhtong)
        fun1.start()
        mainloop()

    def start(self):
        if self.status == False:
            self.lb_status.config(text='Status:ON')
            self.status = True
    def stop(self):
        if self.status == True:
            self.lb_status.config(text='Status:OFF')
            self.status = False
    def cambien1(self):
        if self.status:
            connect = pyodbc.connect('Driver={SQL Server};'
                                          'Server=LAPTOP-SATTI01\SQLEXPRESS;'
                                          'Database=QLSP;'
                                          'Trusted_Connection=yes')
            cursor = connect.cursor()
            cursor.execute(
                f"insert into sanpham1 values ('{strftime('%y%H%M%S')}', '{strftime('%y-%m-%d')}', '1', '0', '0')")
            cursor.commit()
            self.spcao += 1
            self.lb_spcao.config(text=f'{self.spcao}')
            if self.spcao >= 20:
                self.spcao = 0

    def cambien2(self):
        if self.status:
            connect = pyodbc.connect('Driver={SQL Server};'
                                     'Server=LAPTOP-SATTI01\SQLEXPRESS;'
                                     'Database=QLSP;'
                                     'Trusted_Connection=yes')
            cursor = connect.cursor()
            cursor.execute(
                f"insert into sanpham1 values ('{strftime('%y%H%M%S')}', '{strftime('%y-%m-%d')}', '0', '1', '0')")
            cursor.commit()

            self.sptb += 1
            self.lb_sptb.config(text=f'{self.sptb}')
            if self.sptb >= 20:
                self.sptb = 0

    def cambien3(self):
        if self.status:
            connect = pyodbc.connect('Driver={SQL Server};'
                                     'Server=LAPTOP-SATTI01\SQLEXPRESS;'
                                     'Database=QLSP;'
                                     'Trusted_Connection=yes')
            cursor = connect.cursor()
            cursor.execute(
                f"insert into sanpham1 values ('{strftime('%y%H%M%S')}', '{strftime('%y-%m-%d')}', '0', '0', '1')")
            cursor.commit()
            self.spthap += 1
            self.lb_spthap.config(text=f'{self.spthap}')
            if self.spthap >= 20:
                self.spthap = 0
    def tinhtong(sefl):
        if sefl.status:
            connect = pyodbc.connect('Driver={SQL Server};'
                                     'Server=LAPTOP-SATTI01\SQLEXPRESS;'
                                     'Database=QLSP;'
                                     'Trusted_Connection=yes')
            cursor = connect.cursor()
            cursor.execute('select * from sanpham1')
            data = cursor.fetchall()
            sefl.tongsp = data.__len__()
            sefl.lb_tongsp.config(text=f'{sefl.tongsp}')



if __name__ == '__main__':
    qlsp = QLSP()
    qlsp.setupGui()
    qlsp.main()