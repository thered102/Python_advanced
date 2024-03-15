from tkinter import *
wd = Tk()
wd.geometry('600x400')
wd.title('mywindow')
def processCheckButton():
    if check_var.get() == 'a':
        print(et.get())
    else:
        et.delete(0,END)
lb = Label(wd, text='Thiết bị 1', font=('Arial', 20, 'bold'))
check_var = StringVar()
cbt = Checkbutton(wd, text='ON/OFF', variable=check_var, onvalue='a', offvalue='b', command=processCheckButton)
lb.grid(row=0, column=0)
cbt.grid(row=0, column=1)
lb1 = Label(wd, text='User name:')
check = StringVar()
et = Entry(wd, textvariable=check, show='*')
lb1.grid(row=1, column=0)
et.grid(row=1, column=1)
mainloop()