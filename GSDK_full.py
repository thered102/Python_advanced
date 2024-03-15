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

class GSDK:
    def __init__(self):
        pass
    def refresh(self):
        global cbb_com
        comlist = serial.tools.list_ports.comports()
        connected = []
        for i in comlist:
            connected.append(i.device)
        cbb_com['values'] = connected


    def get_Com(self):
        global conn, select_baud, cbb_data, cbb_stop, cbb_time
        conn.port = cbb_com.get()
        conn.baudrate = select_baud.get()
        if cbb_data.get() == '7':
            conn.bytesize = serial.SEVENBITS
        elif cbb_data.get() == '8':
            conn.bytesize = serial.EIGHTBITS
        elif cbb_data.get() == '6':
            conn.bytesize = serial.SIXBITS
        else:
            pass
        if cbb_stop.get() == '1':
            conn.stopbits = serial.STOPBITS_ONE
        elif cbb_stop.get() == '1.5':
            conn.stopbits = serial.STOPBITS_ONE_POINT_FIVE
        elif cbb_stop.get() == '2':
            conn.stopbits = serial.STOPBITS_TWO

        conn.timeout = int(cbb_time.get())


    def connection(self):
        self.get_Com()
        self.hienthi()
        if conn.is_open == False:
            conn.open()
            messagebox.showinfo('Thông báo', 'Kết nối thành công')
        else:
            messagebox.showwarning('Cảnh báo', 'Cổng COM đã kết nối')


    def disconnect(self):
        if conn.is_open == True:
            if messagebox.askyesno('Xác nhận','Bạn có muốn ngắt kết nối hay không?') == True:
                conn.close()
        else:
            messagebox.showinfo('Thông báo', 'Cổng COM đã ngắt kết nối')


    dk = lambda x: conn.write(x.encode('utf-8'))
    def device(self):
        global dk, check
        if check.get() == 1:
            dk('S')
        else:
            dk('A')


    def device2(self):
        global dk, check2
        if check2.get() == 1:
            dk('S')
        else:
            dk('A')


    def nd_da(self):
        global nd, da
        if conn.is_open:
            data = conn.readline().decode('utf-8') # Đọc dữ liệu từ phần cứng (kiểu byte), chuyển kiểu byte sang kiểu dữ liệu python
            data = str(data)
            if len(str(data).strip()) != 0:
                start = data.index('@')
                end = data.index('#')
                x = data[start+1:end]
                start = end
                end = data.index('$')
                y = data[start+1:end]
                nd.config(text=f'Nhiệt độ: {x}')
                da.config(text=f'Độ ẩm: {y}')
                # thêm vào csdl
                try:
                    cursor.execute(f"insert into giamsat values ('{strftime('%H:%M:%S %x')}', '{float(x)}', '{float(y)}', '{check.get()}', '{check2.get()}')")
                    cursor.commit()
                except:
                    pass


    def time_show(self):
        global lb_timeclock
        timeclock = strftime('%y-%m-%d %H:%M:%S')
        lb_timeclock.config(text=timeclock)


    def hienthi(self):
        global cursor, my_tree
        cursor.execute('select * from giamsat')
        csdl = cursor.fetchall()
        global dem
        for j in my_tree.get_children():
            my_tree.delete(j)
        for i in csdl:
            dem += 1
            my_tree.insert('', index='end', iid=str(dem), text='', values=(i[0], i[1], i[2], i[3], i[4]))


    def export(self):
        global wd, connect
        i = strftime('%y%m%d_%H%M%S')
        sql_qr = pd.read_sql_query('select * from giamsat', connect)
        df = pd.DataFrame(sql_qr)
        df.to_csv(f'csdl_{i}.csv')
        os.system(f'start excel csdl_{i}.csv')


    def gui(self):
        global cbb_com, select_baud, cbb_baud, cbb_data, cbb_stop, cbb_time, wd, fr,bt_conn, bt_disconn, check, check2, nd,da,my_tree, lb_timeclock
        wd = Tk()
        wd.geometry('800x600')
        wd.title('Giao diện giám sát & điều khiển')
        fr = Frame(wd)
        fr.pack()
        lb_com = Label(fr, text='COM Port:')
        lb_com.grid(row=0, column=0)
        cbb_com = ttk.Combobox(fr)
        cbb_com.grid(row=0, column=1)
        comlist = serial.tools.list_ports.comports()
        connected = []
        for i in comlist:
            connected.append(i.device)
        cbb_com['values'] = connected
        cbb_com.current(0)

        lb_baud = Label(fr, text='Baudrate: ')
        lb_baud.grid(row=1, column=0)
        select_baud = StringVar()
        cbb_baud = ttk.Combobox(fr, textvariable=select_baud)
        cbb_baud['values'] = ['4800', '9600', '19200', '38400', '119200']
        cbb_baud.current(1)
        cbb_baud.grid(row=1, column=1)
        lb_data = Label(fr, text='Data bit: ')
        lb_data.grid(row=2, column=0)
        cbb_data = ttk.Combobox(fr)
        cbb_data['values'] = ['7', '8', '6']
        cbb_data.current(1)
        cbb_data.grid(row=2, column=1)
        lb_stop = Label(fr, text='Stop bit: ')
        lb_stop.grid(row=3, column=0)
        cbb_stop = ttk.Combobox(fr)
        cbb_stop['values'] = ['1', '1.5', '2']
        cbb_stop.current(0)
        cbb_stop.grid(row=3, column=1)
        lb_time = Label(fr, text='Time out: ')
        lb_time.grid(row=4, column=0)
        cbb_time = ttk.Combobox(fr)
        cbb_time['values'] = ['1', '3', '5', '10']
        cbb_time.current(0)
        cbb_time.grid(row=4, column=1)

        bt_conn = Button(fr, text='Connection', command=self.connection)
        bt_conn.grid(row=1, column=2)
        bt_disconn = Button(fr, text='Disconnect', command=self.disconnect)
        bt_disconn.grid(row=1, column=3)
        #
        check = IntVar()
        chkbt = Checkbutton(fr, text='Thiết bị 1', variable=check, onvalue=1, offvalue=0, command=self.device)
        chkbt.grid(row=3, column=4)
        check2 = IntVar()
        chkbt2 = Checkbutton(fr, text='Thiết bị 2', variable=check2, onvalue=1, offvalue=0, command=self.device2)
        chkbt2.grid(row=4, column=4)

        nd = Label(fr, text=f'Nhiệt độ:', width=15)
        da = Label(fr, text=f'Độ ẩm:')
        nd.grid(row=3, column=2)
        da.grid(row=4, column=2)
        #
        # Hiển thị treeview
        my_tree = ttk.Treeview(wd)
        my_tree.pack()
        my_tree['columns'] = ('time', 'temp', 'humi', 'tb1', 'tb2')
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('time', width=150, anchor=CENTER)
        my_tree.column('temp', width=100, anchor=CENTER)
        my_tree.column('humi', width=100, anchor=CENTER)
        my_tree.column('tb1', width=100, anchor=CENTER)
        my_tree.column('tb2', width=100, anchor=CENTER)
        # Nhãn cho các cột
        my_tree.heading('#0', text="", anchor=CENTER)
        my_tree.heading('time', text="Thời gian", anchor=CENTER)
        my_tree.heading('temp', text="Nhiệt độ", anchor=CENTER)
        my_tree.heading('humi', text="Độ ẩm", anchor=CENTER)
        my_tree.heading('tb1', text="Thiết bị 1", anchor=CENTER)
        my_tree.heading('tb2', text="Thiết bị 2", anchor=CENTER)
        #
        lb_timeclock = Label(fr, text='', background='yellow', font=('Arial', 12, 'bold'))
        lb_timeclock.grid(row=0, column=4)
        bt_update = Button(wd, text='Update CSDL', command=self.hienthi)
        bt_update.pack()
        bt_export = Button(wd, text='Export CSDL', command=self.export)
        bt_export.pack()
        lb_dev = Label(wd, text='Design by tinh.nv@samsung.com',)
        lb_dev.pack()


    def main(self):
        global dem, conn, cursor, connect
        self.gui()
        # refresh cổng com
        fun = continuous_threading.PeriodicThread(1, self.refresh)
        fun.start()
        conn = serial.Serial()
        # Kết nối CSDL
        dem = 0
        connect = pyodbc.connect('Driver={SQL Server};'
                                 'Server=LAPTOP-SATTI01\SQLEXPRESS;'
                                 'Database=GSDK;'
                                 'Trusted_Connection=yes')
        cursor = connect.cursor()
        # Điều khiển thiết bị
        fun1 = continuous_threading.PeriodicThread(1, self.nd_da)
        fun1.start()
        # Hiện thị thời gian
        fun3 = continuous_threading.PeriodicThread(0.001, self.time_show)
        fun3.start()
        # main
        mainloop()


if __name__ == '__main__':
    gsdk = GSDK()
    gsdk.main()
