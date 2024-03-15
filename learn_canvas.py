from tkinter import *
master = Tk()
w = Canvas(master, width=800, height=600)
# w.pack()

# vẽ vòng cung
# w.create_arc(10, 50, 240, 210, fill='blue', width=3)

# vẽ ảnh
# image = PhotoImage(file="canvas.png")
# w.create_image(0, 0, image=image, anchor=NW, state=NORMAL)
# w.pack()

# vẽ đường thẳng
# w.create_line(50, 50, 50, 100, width=3, fill='red')
# w.create_line(50, 100, 100, 100, width=3, fill='red')
# w.create_line(100, 100, 100, 150, width=3, fill='red')
# w.create_line(100, 150, 150, 150, width=3, fill='red')
# w.create_line(150, 150, 150, 200, width=3, fill='red')
# w.create_line(150, 200, 10, 200, width=3, fill='red')
# w.create_line(10, 200, 10, 50, width=3, fill='red')
# w.create_line(10, 50, 50, 50, width=3, fill='red')

# Label

label = Label(master, text='Tên đăng nhập')
label.pack()
mainloop()