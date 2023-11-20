from tkinter import *
from tkinter import filedialog
from itertools import *
import threading
import re
import time
import os


root = Tk()
root.title("Password Generator")
root.geometry("700x300")
root.config(bg="white")

# main func for passwordgenetaror-----------

##new window top level

## Help of app
def help_window_func():
    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.geometry('600x400')
    text_help = Text(help_window,font=('8'))
    text_help.pack()
    with open("Help.txt","r") as file:
        for line in file.readlines():
            text_help.insert(END,line)

### app info
def app_info_func():
    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.geometry('600x400')
    app_info = {'subject': 'project python course( Penetration Test for login)', 'student': 'Abolhasab Binandeh',
          'sir': 'Siyavash Ganji', 'date': 'summer and fall of 2018','thank you so much sir ganji':'good luck and im waiting for next project' }
    text_info = Text(help_window,font=('8'))
    text_info.pack()
    for key , val in app_info.items():
       text_info.insert(END,f"{key} --> {val}\n")



### create menu

menu = Menu(root,bg="light yellow",font=('8'))
root.config(menu=menu)
file_menu = Menu(menu,bg="light yellow")
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="make password.txt",command=lambda:create_password_txt_func(),font=('6'))
file_menu.add_command(label="make data.txt",command=lambda:create_data_txt_func(),font=('6'))
help_menu = Menu(menu,bg="light yellow")
menu.add_cascade(label = "Help",menu=help_menu)
about_menu= Menu(menu,bg="light yellow")
help_menu.add_command(label="help",command=lambda :help_window_func(),font=('6'))
label_info = Label()
help_menu.add_command(label="app info",command=lambda: app_info_func(),font=('6'))



# pass_generator --> generate password and store in file:
def pass_generator(pattern_first):
    global time_start
    global time_end
    global end_constant
    global start_constant
    global password_file_txt_location

    print(password_file_txt_location)
    with open(password_file_txt_location, "a")as file:
        for pro in combinations(pattern_first, len(pattern_first)):
            first_pass = start_constant + ''.join(pro) + end_constant
            file.write(first_pass)
            file.write("\n")

    print(round(time.time() - time_start))
# ---> first_generaor is for generate first pattern without combination
def first_generator_complete(repeat_num, repeat_uppercase, repeat_lowercase, repeat_simbol):
    for com_num in product("9081726354", repeat=int(repeat_num)):
        for com_upper in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=int(repeat_uppercase)):
            for com_lower in product("abcdefghijklmnopqrstuvwxyz", repeat=int(repeat_lowercase)):
                for com_simbol in product('"\'\!#$%&()*+,-./:;<=>?@[\]^_`{|}~ ؛', repeat=int(repeat_simbol)):
                    pattern_first = ''.join(com_num) + ''.join(com_upper) + ''.join(com_lower) + ''.join(com_simbol)
                    t = threading.Thread(target=pass_generator(pattern_first))
                    t.start()
global end_constant, start_constant
end_constant = ""
start_constant = ""
def password_generator_func():
    if entry_pass_pattern.get()=="" :
        error_equation_pass.set(" error: pattern filed should not empty:")
    elif browse_create_file_Entry_box.get() == "":
        error_equation_pass.set("error: browse field shouldot empty!")
    else:
        global time_start
        global time_end
        global end_constant
        global start_constant
        time_start = time.time()

        repeat_num, repeat_uppercase, repeat_lowercase, repeat_simbol = 0, 0, 0, 0
        input_str = entry_pass_pattern.get()
        pattern_pass = re.compile("((\d+)#{1}(\d+)&{1}(\d+)@{1}(\d+)!{1}){1}").search(input_str)
        if pattern_pass == None:
            error_equation_pass.set("not match with sintax pattern: insert such as '3#3&3@3!' ")
        else:
            repeat_num, repeat_uppercase, repeat_lowercase, repeat_simbol = 0, 0, 0, 0
            repeat_num = int((re.compile("((\d+)#{1}(\d+)&{1}(\d+)@{1}(\d+)!{1}){1}").search(input_str)).group(2))
            repeat_uppercase = int((re.compile("((\d+)#{1}(\d+)&{1}(\d+)@{1}(\d+)!{1}){1}").search(input_str)).group(3))
            repeat_lowercase = int((re.compile("((\d+)#{1}(\d+)&{1}(\d+)@{1}(\d+)!{1}){1}").search(input_str)).group(4))
            repeat_simbol = int((re.compile("((\d+)#{1}(\d+)&{1}(\d+)@{1}(\d+)!{1}){1}").search(input_str)).group(5))
            start_constant = entry_pass_start.get()
            end_constant =  entry_pass_end.get()
            t = threading.Thread(
                target=first_generator_complete(repeat_num, repeat_uppercase, repeat_lowercase, repeat_simbol))
            t.start()

### end of func passwordgenertor

def browse_save_file_func():
    global password_file_txt_location
    with open("password.txt",'a') as file:
        pass
    path_file_location = filedialog.askopenfilename(parent=frame2,title="select file",filetypes =(("file","password.txt",".csv"),("all files","*.*")))
    browse_create_file_equation.set(path_file_location)
    password_file_txt_location = path_file_location
    if os.stat(password_file_txt_location).st_size != 0 :
        error_equation_pass.set(" txt file is not empty !! are you sure to continue ...")
#### define function for creating password.txt
def create_password_txt_func():
    if os.path.isfile("password.txt") == True:
        error_equation_pass.set("password.txt is exist. you dont need to create again")
    else:
        with open("password.txt","a") as file:
            success_equation_pass.set("creating password.txt is successfull")

### define function for creating data.txt
def create_data_txt_func():
    if os.path.isfile("data.txt") == True:
        error_equation_pass.set("data.txt is exist. you dont need to create again")
    else:
        with open("password.txt","a") as file:
            success_equation_pass.set("creating data.txt is successfull")
            with open("data.txt","w") as file:
                file.write("{}")


## Frame
frame1 = Frame(root,bg = "white")
frame1.grid(row=0,pady=25)
frame2 = Frame(root,bg="white")
frame3 = Frame(root,bg='white')
frame2.grid(row=1)
frame3.grid(row=2)

# define equation ---
entry_pass_start_equation = StringVar()
entry_pass_pattern_equation = StringVar()
entry_pass_end_equation = StringVar()

### define button for create file data.txt and password.txt
#create_button = Button(frame1,bg="dark salmon",width = 70,height=1,font=('10'))
#create_button.pack(side = LEFT,)
#create_button = Button(frame1,bg="dark salmon",width = 35,height=1,font=('10'))
#create_button.pack(side = RIGHT)

# define entry for first start
label1 = Label(frame2,text = "  START with:",font=('6'),bg="white")
label1.grid(row=1,column=0)
entry_pass_start = Entry(frame2,width=30,font=('10'),textvariable = entry_pass_start_equation)
entry_pass_start.grid(row=1,column=1)
entry_pass_start_equation.set("start")

# password pattern
label2 = Label(frame2,text = "PATTERN:",font=('6'),bg="white")
label2.grid(row=2,column=0)
entry_pass_pattern = Entry(frame2,width=30,font=('10'),textvariable = entry_pass_pattern_equation)
entry_pass_pattern.grid(row=2,column=1)
entry_pass_pattern_equation.set("1#0&0@0!")

# password end
label3 = Label(frame2,text = "END with:",font=('6'),bg='white')
label3.grid(row=3,column=0)
entry_pass_end = Entry(frame2,width=30,font=('10'),textvariable = entry_pass_end_equation)
entry_pass_end.grid(row=3,column=1)
entry_pass_end_equation.set("end")

btn_browse_location_create_file = Button(frame2,text="brwose",bg="dark salmon",font=('5'),command= lambda:browse_save_file_func())
btn_browse_location_create_file.grid(row=4,column=0)
browse_create_file_equation = StringVar()
browse_create_file_Entry_box = Entry(frame2,width=50,font=('10'),text = browse_create_file_equation)
browse_create_file_Entry_box.grid(row=4,column=1)


btn_pass_generator = Button(frame3,text="generate password",bg="dark salmon",width=15,height=1,font=('5'),command=lambda:password_generator_func())
btn_pass_generator.grid(row=0,column=0,padx=2)
btn_pass_generator_stop = Button(frame3,text="exit",width=15,height=1,bg="dark salmon",font=('5'),command=lambda:quit())
btn_pass_generator_stop.grid(row=0,column=1,padx=2)
### error reporting
error_equation_pass = StringVar()
label_error = Label(frame3,textvariable = error_equation_pass,fg="red",font=('6'),bg="white")
label_error.grid(row=2,column=0)
success_equation_pass = StringVar()
label_success = Label(frame3,textvariable = success_equation_pass,fg="green",font=('6'),bg="white")
label_success.grid(row=2,column=0)


root.mainloop()