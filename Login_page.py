import sqlite3
from tkinter import *
list1 = []

def get_value():
    message = code_entry.get()
    return f"{message}"

########
def check():
    name = name_entry.get()
    password = password_entry.get()
    code = code_entry.get()
    print(name,password,code)
    conn = sqlite3.connect('aftab_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM teachers_data')
    students_data = cursor.fetchall()
    print(students_data)
    for row in students_data:
            if name in row:
                button_submit.config(state=NORMAL)
                list1.append(name)
                
            else:
                button_submit.config(state=DISABLED)
                print("testing is on")
    
    get_value()
    
    if len(list1) > 0:
        button_submit.config(state=NORMAL)
    else:
        button_submit.config(state=DISABLED)
def dash():
    root.destroy()
    import teacher_dashboard
        

root = Tk()
root.geometry("1200x700")
root.title("Student attendance management ")
frame1 = Frame(root, borderwidth=5, bg="black", relief=SUNKEN)
frame1.pack(side=TOP, ipady=200)

frame2 = Frame(frame1, borderwidth=5, bg="white", relief=SUNKEN)
frame2.pack(side=TOP, padx=40, pady=40)

logo1 = PhotoImage(file="logo.png")
logo1 = logo1.subsample(8, 8)

label = Label(frame2, text="ACCOUNT LOGIN PAGE", fg="black", bg="yellow", font=("helvetica bold", 24))
label.pack(padx=1200)

labe2 = Label(frame2, text="", fg="black", bg="white")
labe2.pack(padx=200)

label_logo = Label(frame2, image=logo1)
label_logo.pack(ipadx=5, ipady=5)

labe3 = Label(frame2, text="VIJAYA VITTALA INSTITUTE OF TECHNOLOGY", fg="red", bg="white",
              font=("helvetica bold", 12))
labe3.pack(padx=20)
labe4 = Label(frame2, text="PLEASE ENTER THE DETAILS TO LOGIN ", fg="BLUE", bg="white",
              font=("helvetica bold", 12))
labe4.pack(padx=20)
labe5 = Label(frame2, text="CLASS DATA WILL OCCUR AS PER THE CLASS CODE", fg="BLUE", bg="white",
              font=("helvetica bold", 12))
labe5.pack(padx=20)
labe6 = Label(frame2, text="This project is prototype, made by AFTAB AND MOHAMMAD SAAD KHAN of 5th sem ,3rd year ,AI&ML Branch", fg="green", bg="white",
              font=("helvetica bold", 12))
labe6.pack(padx=20)

entry_frame = Frame(frame2, borderwidth=5, bg="white", relief=SUNKEN)
entry_frame.pack(side=TOP, ipady=600, ipadx=200, padx=10, pady=10)

name = Label(entry_frame, text="user_name", bg='white', font=("Helvetica bold", 13))
name.pack(side=TOP, pady=10, anchor='n')
name_entry = Entry(entry_frame, borderwidth=5)
name_entry.pack(side=TOP, pady=10, anchor='n')

password = Label(entry_frame, text="password", bg='white', font=("Helvetica bold", 13))
password.pack(side=TOP, pady=10, anchor='n')
password_entry = Entry(entry_frame, borderwidth=5)
password_entry.pack(side=TOP, pady=10, anchor='n')

code = Label(entry_frame, text="code", bg='white', font=("Helvetica bold", 13))
code.pack(side=TOP, pady=10, anchor='n')
code_entry = Entry(entry_frame, borderwidth=5)
code_entry.pack(side=TOP, pady=10, anchor='n')

# Declare button_submit before using it in the check function
button_submit = Button(entry_frame, text="SUBMIT", state=DISABLED, command=dash, fg="white", bg="blue",
                       font=("Helvetica bold", 12))
button_submit.pack(side=TOP, pady=10, anchor='n')

button_check = Button(entry_frame, text="check", command=check, fg="white", bg="blue",
                      font=("Helvetica bold", 12))
button_check.pack(side=TOP, pady=10, anchor='n')

root.mainloop()





