


from tkinter import *
import os
import time
from squad import *
from InfoAppend import *
from tkinter import messagebox  
flag1=0
flag2=0

def delete13():
  screen12.destroy()

def delete12():
  screen11.destroy()

def delete11():
  screen10.destroy()

def delete0():
  screen1.destroy()
def delete1():
  screen2.destroy()
def delete2():
  screen3.destroy()
  after_login()
 
def delete3():
  screen4.destroy()
 
def delete4():
  screen5.destroy()

def delete5():
	screen7.destroy()

def delete6():
  screen8.destroy()

def delete7():
  screen.destroy()  

def delete8():
  screen6.destroy()
def delete9():
  screen9.destroy()

def data_cleaning():
  global screen8
  global flag2
  flag2=1
  screen8=Toplevel(screen6)
  screen8.configure(background='light cyan')
  screen8.geometry('400x200')
  screen8.title("Message Box")
  Label(screen8, text = "\n\nData Processed Successfully!\n\n ",font=("TkHeadingFont",17), fg='black',bg = "light cyan").pack()
  os.system("python3 squad.py")
  time.sleep(1)
  Button(screen8,text = "Back",height = "1", width = "15", bg = "gray",command=delete6).pack()
  
def data_processing():
  global flag1
  flag1=1
  global screen7
  screen7=Toplevel(screen6)
  screen7.configure(background='light cyan')
  screen7.geometry('400x200')
  screen7.title("Message Box")
  Label(screen7, text = "\n\nData Pre-Processed Successfully !\n\n ", font=("TkHeadingFont",17),fg='black',bg = "light cyan").pack()
  os.system("python3 datacleaning.py")
  time.sleep(1)
  Button(screen7,text = "Back",height = "1", width = "15", bg = "gray",command=delete5).pack()
  

def warning_one():
  global screen10
  print("Flag2  ",flag2)
  screen10=Toplevel(screen6)
  screen10.configure(background='light cyan')
  screen10.geometry('600x200')
  screen10.title("Message Box")
  Label(screen10, text = "\n\nPlease Pre-Process Data and Process data\n\n ",font=("TkHeadingFont",17), fg='black',bg = "light cyan").pack()
  Button(screen10,text = "Back",height = "1", width = "15", bg = "gray",command=delete11).pack()
  
  

def warning_two():
  global screen11
  screen11=Toplevel(screen6)
  screen11.configure(background='light cyan')
  screen11.geometry('600x200')
  screen11.title("Message Box")
  Label(screen11, text = "\n\nPlease Process Data\n\n ",font=("TkHeadingFont",17), fg='black',bg = "light cyan").pack()
  Button(screen11,text = "Back",height = "1", width = "15", bg = "gray",command=delete12).pack()
  
  
def warning_three():
  global screen12
  screen12=Toplevel(screen6)
  screen12.configure(background='light cyan')
  screen12.geometry('600x200')
  screen12.title("Message Box")
  Label(screen12, text = "\n\nPlease Pre-Process Data\n\n ",font=("TkHeadingFont",17), fg='black',bg = "light cyan").pack()
  Button(screen12,text = "Back",height = "1", width = "15", bg = "gray",command=delete13).pack()
  
  




       
def after_login():

  global screen6
  screen6= Toplevel(screen2)
  screen6.configure(background='white')
  screen6.title("Cricket for good!")
  screen6.geometry("1200x800")
  Label(screen6, text = "\n\nWelcome To Cricket Players' Squad Recommendation System\n\n",font = ('Times', 26), fg='royal blue',bg = "white").pack()
  Button(screen6,text = "Data Pre-Processing", height = "2", width = "30",command=data_processing,bg = "SlateBlue1").pack()
  Label(screen6,text = "\n").pack()
  Button(screen6,text = "Data Processing",height = "2", width = "30", command=check1,bg = "SlateBlue1").pack()
  Label(screen6,text = "\n").pack()
  Button(screen6,text = "Display Squad",height = "2", width = "30", command=check,bg = "SlateBlue1").pack()
  
  Button(screen6,text = "Log Out",height = "2", width = "20", command=delete8,bg = "red2").pack(side=BOTTOM)  

def a1():
  os.system("python3 virat.py")

def a2():
  os.system("python3 shikhar.py")

def a3():
  os.system("python3 shreyas.py")

def a4():
  os.system("python3 rohit.py")
def a5():
  os.system("python3 gg.py")
def a6():
  os.system("python3 hardik.py")
def a7():
  os.system("python3 stuart.py")
def a8():
  os.system("python3 ravindra.py")
def a9():
  os.system("python3 kuldeep.py")
def a10():
  os.system("python3 amit.py")
def a11():
  os.system("python3 jasprit.py")
def a12():
  os.system("python3 chahal.py")
def a13():
  os.system("python3 mohammnd.py")
def a14():
  os.system("python3 dhoni.py")
def a15():
  os.system("python3 klrahul.py")

def display_squad():
  global screen9
  screen9=Toplevel(screen6)
  screen9.configure(background='light cyan')
  screen9.title("Welcome")
  screen9.geometry("1200x800")
  Label(screen9, text ="\nIndian Cricket Players Squad\n ",font=("Times",28), fg='royal blue',bg = "light cyan").pack()
  screen9.title("Teamwork makes the Dreamwork !")

  Button(screen9,text=names[0],relief=RIDGE,width=25,command=a1,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[1],relief=RIDGE,width=25,command=a2,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[2],relief=RIDGE,width=25,command=a3,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[3],relief=RIDGE,width=25,command=a4,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[4],relief=RIDGE,width=25,command=a5,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[5],relief=RIDGE,width=25,command=a6,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[6],relief=RIDGE,width=25,command=a7,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[7],relief=RIDGE,width=25,command=a8,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[8],relief=RIDGE,width=25,command=a9,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[9],relief=RIDGE,width=25,command=a10,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[10],relief=RIDGE,width=25,command=a11,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[11],relief=RIDGE,width=25,command=a12,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[12],relief=RIDGE,width=25,command=a13,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[13],relief=RIDGE,width=25,command=a14,font=("Times",14),bg="light cyan").pack()
  Button(screen9,text=names[14],relief=RIDGE,width=25,command=a15,font=("Times",14),bg="light cyan").pack()
  
  option_list=['Batsmen','Bowlers','AllRounders As Batsman','AllRounders As Bowler','Wicket Keeper','BatsmenRatings','BowlingRatings','WicketKeepersRatings']
  global var1
  var1 = StringVar(screen9)
  var1.set('<-select option->')
  Label(screen9, text = "Visualization\n",font = ('TkHeadingFont', 14), fg='black',bg = "light cyan").place(x=120,y=475)
  opt1=OptionMenu(screen9,var1,*option_list)
  opt1.place(x=100,y=500)
  Button(screen9,text="Display",command=ok,height = "1", width = "10",bg="white smoke").place(x=127,y=533)
  Button(screen9,text = "Quit",height = "1", width = "10", command=delete9,bg = "gray").place(x=1000,y=600) 
def ok():
  global visualization_choice
  visualization_choice=var1.get()
  if(visualization_choice=='Batsmen'):
    #Batsman Graph
    os.system("python3 graph_batsmen.py")
  elif (visualization_choice=='Bowlers'):
    os.system("python3 graph_bowler.py")
  elif (visualization_choice=='AllRounders As Batsman'):
    os.system("python3 graph_allrounder_as_batsman.py")
  elif (visualization_choice=='AllRounders As Bowler'):
    os.system("python3 graph_allrounder_as_bowler.py")
  elif (visualization_choice=='Wicket Keeper'):
    os.system("python3 graph_wicketkeeper.py")
  elif (visualization_choice=='BatsmenRatings'):
    os.system("python3 graph_batsmen_ratings.py")
  elif (visualization_choice=='BowlingRatings'):
    os.system("python3 graph_bowlers_ratings.py")
  elif (visualization_choice=='WicketKeepersRatings'):
    os.system("python3 graph_wicketkeepers_ratings.py") 





def check1():
  global flag1
  if(flag1==0):
    warning_three()
  else:
    data_cleaning()   




def check():
  global flag1
  global flag2
  if(flag1==0 and flag2==0):
    warning_one()
  elif(flag1==1 and flag2==0):
    warning_two()
  elif(flag1==1 and flag2==1):
    display_squad() 



def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.configure(background='light cyan')
  screen3.title("Success")
  screen3.geometry("200x150")
  Label(screen3, text = "\n\nLogin Success\n\n", fg='black',bg = "light cyan").pack()
  Button(screen3, text = "Next",  bg = "gray",command =delete2).pack()
 
def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.configure(background='light cyan')
  screen4.title("Success")
  screen4.geometry("200x150")
  Label(screen4, text = "\n\nPassword Error\n\n", fg='black',bg = "light cyan").pack()
  Button(screen4, text = "Back", bg = "gray", command =delete3).pack()
 
def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.configure(background='light cyan')
  screen5.title("Success")
  screen5.geometry("200x150")
  Label(screen5, text = "\n\nUser Not Found\n\n", fg='black',bg = "light cyan").pack()
  Button(screen5, text = "Back", bg = "gray", command =delete4).pack()
 
   
def register_user():
  username_info = username.get()
  password_info = password.get()
 
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)
 
  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
 
def login_verify():
   
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
 
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
 
  else:
        user_not_found()
   
 
 
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.configure(background='light cyan')
  screen1.title("Register")
  screen1.geometry("300x250")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(screen1, text = "Please enter details below",fg='black',bg = "light cyan").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ",fg='black',bg = "light cyan").pack()
  
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ",fg='black',bg = "light cyan").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register",cursor='plus', width = 10, height = 1,bg = "orange red", command = register_user).pack()
  Button(screen1, text = "Back", bg = "gray", command =delete0).pack()


def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.configure(background='light cyan')
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login", fg='black',bg = "light cyan").pack()
  Label(screen2, text = "").pack()
 
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(screen2, text = "Username*" ,fg='black',bg = "light cyan").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "Password*", fg='black',bg = "light cyan").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1,bg = "green",command = login_verify).pack()
  Button(screen2, text = "BACK", bg = "gray", command =delete1).pack()

def About_us():
  os.system('python3 about_us.py')



def main_screen():
  global screen
  screen = Tk()
  screen.configure(background='white')
  screen.geometry("1200x800")
  screen.title("Cricket Player Recommendation System")
  Label(text = "\n\n\nIndian Cricket Team Recommendation System \n\n", fg='royal blue',bg = "white", font = ('Times', 28)).pack()
  
  Button(text = "Login", height = "3", width = "40",bg = "green", command = login).pack()
  Label(text='\n').pack()
  Button(text = "Register",cursor='plus',height = "3", width = "40", bg = "orange red",command = register).pack()
  Button(screen, text = "Quit",height = "1",cursor='arrow', width = "20" ,bd=3,bg = "gray", command =delete7,activeforeground='red').pack(side=BOTTOM)
  Button(screen,text = "About Us", cursor='arrow',height = "1", width = "10",bg = "white smoke",command=About_us).place(x=5,y=670)


  screen.mainloop()
 
main_screen()
  
