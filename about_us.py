from tkinter import *
def delete_root():
  root.destroy()

global root
root = Tk()
root.configure(background='light cyan')
root.geometry("1100x700")
root.title("About Us")

Label(root, text="Alone we can do so little;\ntogether we can do so much.",height='8',width='100',font=('Times',20,'bold'),bg='light cyan',fg='green').pack()


Label(root, text="Roll No\t\t\t Name \t \t\t\tContact No",height='2',width='100',font=('Times',18,'bold'),bg='light cyan',fg='orange red').pack()

team_members=["125\t\tMr. Sabnis Sushant Suhas  \t\t\t8378012416","138\t\tMr. Shirke Aniket Bhausaheb\t\t9975759566","140\t\tMr. Somwanshi Adesh Sainath\t\t7620086531","142\t\tMr. Sonawane Anand Rajendra\t\t7620893217"]
for i in range(4):
  Label(root, text=team_members[i],height='2',width='100',font=('Times',18),bg='light cyan').pack()

Button(root,text = "back",height = "2", width = "20", command=delete_root,bg = "gray").pack(side=BOTTOM)


root.mainloop()
