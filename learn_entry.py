from tkinter import *
wd = Tk()
wd.geometry('600x400')
wd.title('mywindow')
lb1 = Label(wd, text='User name:')
check = StringVar()
et = Entry(wd, textvariable=check, show='*')
lb1.grid(row=0, column=0)
et.grid(row=0, column=1)
mainloop()