from tkinter import *
import os
 
def delete2():
  screen3.destroy()
 
def delete3():
  screen4.destroy()
 
def delete4():
  screen5.destroy()
   
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.configure(background='SkyBlue4')
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Successfull!", fg='tan1',bg = "SkyBlue4").pack()
  Button(screen3, text = "OK",  bg = "SlateBlue1",command =delete2).pack()
 
def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.configure(background='SkyBlue4')
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error!", fg='tan1',bg = "SkyBlue4").pack()
  Button(screen4, text = "OK", bg = "SlateBlue1", command =delete3).pack()
 
def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.configure(background='SkyBlue4')
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found", fg='tan1',bg = "SkyBlue4").pack()
  Button(screen5, text = "OK", bg = "SlateBlue1", command =delete4).pack()
 
   
def register_user():
  print("working")
   
  username_info = username.get()
  password_info = password.get()
 
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)
 
  Label(screen1, text = "Registration Successfull!", fg = "green" ,font = ("calibri", 11)).pack()
 
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
  screen1.configure(background='SkyBlue4')
  screen1.title("Register")
  screen1.geometry("300x250")
   
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
 
  Label(screen1, text = "Please enter the details below!",fg='tan1',bg = "SkyBlue4").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ",fg='tan1',bg = "SkyBlue4").pack()
  
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ",fg='tan1',bg = "SkyBlue4").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1,fg='tan1',bg = "SkyBlue4", command = register_user).pack()
 
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.configure(background='SkyBlue4')
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login!", fg='tan1',bg = "SkyBlue4").pack()
  Label(screen2, text = "").pack()
 
  global username_verify
  global password_verify
   
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(screen2, text = "Username * ", fg='tan1',bg = "SkyBlue4").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ", fg='tan1',bg = "SkyBlue4").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1,bg = "SlateBlue1",command = login_verify).pack()
   
   
def main_screen():
  global screen
  screen = Tk()

  screen.configure(background='SkyBlue4')
  screen.geometry("300x250")
  screen.title("Cricket Players Squad Recommandation System")
  Label(text = "Cricket Players Squad Recommandation System", fg='tan1',bg = "SkyBlue4", width = "300", height = "10", font = ('TkHeadingFont', 14)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30",bg = "SlateBlue1", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", bg = "SlateBlue1",command = register).pack()
 
  screen.mainloop()
 
main_screen()
  
