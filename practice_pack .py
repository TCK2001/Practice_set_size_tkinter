from tkinter import*

#pratice pack pad(y)
win=Tk()
win.geometry("400x200")
win.title("TCK")
win.option_add("*Font","궁서 20")

ent=Entry(win)
ent.pack(side="top")

btn=Button(win)
btn.config(text="button")

def c():
    btn.pack(pady=ent.get()) # 위 아래로 간격 설정

btn.config(command=c)
btn.pack()


win.mainloop()

