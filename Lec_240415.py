# 2024/04/15 AI프로그래밍및실습 해양학전공
from tkinter import *

# window 예제
#window = Tk()
#window.title("윈도창 연습")
#window.geometry("400x100")        # 사이즈
#window.resizable(width = True, height = True)

#label1 = Label(window, text = "COOKBOOK~~ Python을")
#label2 = Label(window, text = "열심히", font = ("맑은고딕", 30), fg = "red")
#label3 = Label(window, text = "공부 중입니다.", bg = "pink", width = 20, height = 5, anchor = SE)

#label1.pack()
#label2.pack()
#label3.pack()

#window.mainloop()


# GIF 예제
from tkinter import *
window = Tk()

photo = PhotoImage(file = "GIF1.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()
