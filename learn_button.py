from tkinter import *
a = 300
b = 300
x = 300
y = 300
wd = Tk()
wd.geometry('800x600')
wd.title("mywindow")
# fr = Frame(wd)
# fr.pack()
def tien():
    global y
    y -= 10
    label2.config(text=f'Tọa độ x: {300-y}')

def trai():
    global x
    x -= 10
    label1.config(text=f'Tọa độ y: {x-300}')
def phai():
    global x
    x += 10
    label1.config(text=f'Tọa độ y: {x-300}')

def lui():
    global y
    y += 10
    label2.config(text=f'Tọa độ x: {300-y}')

def go():
    global x, y, a, b, cv
    # cv = Canvas(wd, width=600, height=600)
    # cv.grid(row=4, column=4)
    cv.create_line(a, b, x, y, width=3, fill='red')
    a = x
    b = y
Label(wd,text='  ').grid(row=0, column=1)
Label(wd,text='      ').grid(row=1, column=0)
Label(wd,text='      ').grid(row=4, column=2)
bt = Button(wd, text='Tiến', bg='red', command=tien)
# bt.pack(expand=True, side=LEFT, fill=BOTH) # bố trí theo khối
bt.grid(row=1, column=2)
# bt.place(x=50, y=50)
bt2 = Button(wd, text='Trái', bg='blue', command=trai)
# bt2.pack(expand=True, side=RIGHT, fill=BOTH)
bt2.grid(row=2, column=1)
# bt2.place(x=0, y=100)
bt3 = Button(wd, text='Phải', bg='green', command=phai)
# bt3.pack()
bt3.grid(row=2, column=4)
# bt3.place(x=50, y=100)
bt4 = Button(wd, text='Lùi', bg='yellow', command=lui)
# bt4.pack()
bt4.grid(row=3, column=2)
# bt4.place(x=50, y=200)
bt5 = Button(wd, text='Go', bg='gray', command=go)
# bt3.pack()
bt5.grid(row=5, column=2)

label1 = Label(wd, text=f'Tọa độ x: {x-300}')
label1.grid(row=2, column=5)
label2 = Label(wd, text=f'Tọa độ y: {300-y}')
label2.grid(row=3, column=5)
# canvas
cv = Canvas(wd, width=600, height=600)
cv.grid(row=6, column=5)
cv.create_line(300, 300, 300, 0)
cv.create_line(300, 300, 600, 300)

wd.mainloop()