# 간단한 원을 그리는 GUI 프로그래밍

from tkinter import *

window = Tk()
canvas = Canvas(window, height=1000, width=1000, bg='white')
canvas.pack()

cx=1000//2
cy=1000//2
r = 400
canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline="red")

window.mainloop()