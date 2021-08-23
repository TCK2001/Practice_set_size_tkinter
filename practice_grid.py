from tkinter import*

#grid attribute no empty space
win=Tk()
win.geometry("600x400")
win.title("TCK_grid")
win.option_add("*Font","궁서 20")
#3x4 matrix
btn_list=[] #save the last use btn
col_num=3 # >
row_num=4 # ^
for i in range(0,col_num):
    for j in range(0,row_num):
        btn=Button(win)
        btn.config(text="({},{})".format(i,j))
        btn.grid(column=i,row=j,padx=10,pady=10) #간격 주기
        btn_list.append(btn)

btn1=Button(win)
btn1.config(text="new")
btn1.grid(column=2,row=0,rowspan=2)

btn1=Button(win)
btn1.config(text="renew")
btn1.grid(column=0,row=3,columnspan=2)
win.mainloop()