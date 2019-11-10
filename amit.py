from tkinter import *
from batsmen import *
from wicketkeeping import *
from bowlers import *
from allrounders import *
from squad import *
def delete_root():
  root.destroy()
global root
root = Tk()
root.configure(background='light cyan')
root.geometry("400x700")
root.title("Player Information")
logo = PhotoImage(file="mishra.png")

w1 = Label(root, image=logo,height=170).pack()
Label(root,text="\n")
Label(root, text=names[9],height='2',width='30',font=('Times',18,'bold'),bg='light cyan').pack()

from InfoAppend import *
for i in range(0,14):
  Label(root,text=text_var[9][i],font=('Times',10),width='40',height='2',bg='light cyan').pack()

Button(root,text = "back",height = "1", width = "8", command=delete_root,bg = "gray").place(x=2,y=10) 
root.mainloop()
