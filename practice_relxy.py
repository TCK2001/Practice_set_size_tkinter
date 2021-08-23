from tkinter import*

win=Tk()
win.geometry("600x400")
win.title("TCK_relx,y")
win.option_add("*Font","궁서 20")

xx=0.3
yy=0.4

btn=Button(win)
btn.config(text="({},{})".format(xx,yy))
btn.place(relx=xx,rely=yy)
# relx,rely 는 절대위치가 아님 창 바뀌면 같이 바뀜 x=1,y=1(max length)
win.mainloop()