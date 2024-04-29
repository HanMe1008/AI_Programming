# 2024/04/15 AI프로그래밍및실습 해양학전공

# GUI 예제
"""
from tkinter import *
window = Tk()

window.title("윈도창 연습")
window.geometry("400x100")        # 사이즈
window.resizable(width = True, height = True)

label1 = Label(window, text = "COOKBOOK~~ Python을")
label2 = Label(window, text = "열심히", font = ("맑은고딕", 30), fg = "red")
label3 = Label(window, text = "공부 중입니다.", bg = "pink", width = 20, height = 5, anchor = SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
"""

# GIF 예제
"""
from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "GIF1.gif")
photo2 = PhotoImage(file = "GIF2.gif")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side = LEFT)
label2.pack()

window.mainloop()
"""

# 이벤트 처리 1
"""
from tkinter import *
window = Tk()

button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

button1.pack()

window.mainloop()
"""

# 이벤트 처리 2
"""
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def myFunc():
    messagebox.showinfo("심슨 버튼", "심슨이 귀엽죠? ^^")

## 메인 코드 부분 ##
window = Tk()

photo = PhotoImage(file = "gif1.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()
"""

# CheckButton()
"""
from tkinter import *
from tkinter import messagebox
window = Tk()

## 함수 선언 부분 ##
def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요.")

## 메인 코드 부분 ##
chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()
"""

# Radiobutton()
from tkinter import *
window = Tk()

def myFunc():
    if var.get() == 1:
        label1.configure(text = "파이썬")
    elif var.get() == 2:
        label1.configure(text = "C++")
    else:
        label1.configure(text = "Java")

var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc)

label1 = Label(window, text = "선택한 언어 : ", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()