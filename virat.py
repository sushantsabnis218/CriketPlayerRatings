from tkinter import *
from InfoAppend import *

def delete_root():
  root.destroy()
global root
root = Tk()
root.configure(background='light cyan')
root.geometry("400x700")
root.title("Player Information")
logo = PhotoImage(file="virat1.png")

w1 = Label(root, image=logo,height=170).pack()
Label(root, text=names[0],height='2',width='30',font=('Times',18,'bold'),bg='light cyan').pack()


for i in range(0,14):
  Label(root,text=text_var[0][i],font=('Times',10),width='40',height='2',bg='light cyan').pack()


Button(root,text = "back",height = "1", width = "6", command=delete_root,bg = "gray").place(x=2,y=10)
root.mainloop()
