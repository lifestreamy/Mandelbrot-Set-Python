from time import sleep
from tkinter import *

from tkinter import messagebox
import tkinter.ttk as ttk


def main():
    def Help():
        messagebox.showinfo("Help", "Версия 1.0:SNAPSHOT\n Автор: Lifestreamy")

    def Exit():
        a.destroy()
        exit()

    def Print():
        print("print")

    def Reset():
        print("reset")

    def Undo():
        print("undo")

    def Redo():
        print("redo")

    def _from_rgb(r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def ColorPoint(x, y, r, g, b):
        canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill=_from_rgb(r, g, b))

    print("start")
    a = Tk()
    a.title("Main Program")
    factor = 1.5
    dimension_x = int(1920 / factor)
    dimension_y = int(1080 / factor)
    a.geometry(str(dimension_x) + "x" + str(dimension_y))
    """MENU"""
    file_menu = Menu(tearoff=0)
    file_menu.add_command(label="New", font=("Georgia", 10))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", font=("Georgia", 10), command=Exit)
    menu = Menu()
    menu.add_cascade(label="File", menu=file_menu)
    menu.add_cascade(label="Help", command=Help)
    a.config(menu=menu)
    """FRAMES"""
    frame_work = Frame(a)
    frame_canvas = Frame(a)
    frame_work.grid(row=0, column=0)
    frame_canvas.grid(row=0, column=1, padx=8)
    """EDITS"""
    e1 = Entry(frame_work)
    e2 = Entry(frame_work)
    e3 = Entry(frame_work)
    e4 = Entry(frame_work)
    e5 = Entry(frame_work)
    e1.grid(row=0, column=1, padx=5, pady=5)
    e2.grid(row=1, column=1, padx=5, pady=5)
    e3.grid(row=2, column=1, padx=5, pady=5)
    e4.grid(row=3, column=1, padx=5, pady=5)
    e5.grid(row=4, column=1, padx=5, pady=5)
    """LABELS"""
    l1 = Label(frame_work, text="x1", font=("Georgia", 10))
    l2 = Label(frame_work, text="x2", font=("Georgia", 10))
    l3 = Label(frame_work, text="y1", font=("Georgia", 10))
    l4 = Label(frame_work, text="y2", font=("Georgia", 10))
    l5 = Label(frame_work, text="Iterations", font=("Georgia", 10))
    l6 = Label(frame_work, text="Time elapsed =", font=("Georgia", 10))
    l7 = Label(frame_work, text="...", font=("Georgia", 10))
    l1.grid(row=0, column=0, padx=5, pady=5)
    l2.grid(row=1, column=0, padx=5, pady=5)
    l3.grid(row=2, column=0, padx=5, pady=5)
    l4.grid(row=3, column=0, padx=5, pady=5)
    l5.grid(row=4, column=0, padx=5, pady=5)
    l6.grid(row=9, column=0, padx=5, pady=5)
    l7.grid(row=9, column=1, padx=5, pady=5)
    """BUTTONS"""
    b1 = Button(frame_work, text="print", font=("Georgia", 10), width=10, height=1, command=Print)
    b2 = Button(frame_work, text="reset", font=("Georgia", 10), width=10, height=1, command=Reset)
    b3 = Button(frame_work, text="undo", font=("Georgia", 10), width=10, height=1, command=Undo)
    b4 = Button(frame_work, text="redo", font=("Georgia", 10), width=10, height=1, command=Redo)
    b1.grid(row=5, column=0, padx=5, pady=5)
    b2.grid(row=6, column=0, padx=5, pady=5)
    b3.grid(row=7, column=0, padx=5, pady=5)
    b4.grid(row=8, column=0, padx=5, pady=5)
    "PROGRESS BAR"""
    pb = ttk.Progressbar(frame_work, orient="horizontal", maximum=100, value=0)
    pb.grid(row=10, column=0)
    pb.start()
    # pb.step(20)
    """CANVAS"""
    canvas = Canvas(frame_canvas, height=dimension_y, width=int(dimension_x * 4 / 5), )
    canvas.pack()
    canvas.create_rectangle(0, 0, canvas.winfo_reqwidth(), canvas.winfo_reqheight(), fill="#aaa")
    """MAIN LOOP"""
    a.mainloop()


if __name__ == '__main__':
    main()
