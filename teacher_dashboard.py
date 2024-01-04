import sqlite3
import Login_page as p
st_code = 0
from tkinter import *
def update_data():
    conn = sqlite3.connect('aftab_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_data')
    root.destroy()
    

    
def dash():
    root.destroy()
    import Login_page




def frame_31():
    
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    frame31.pack(fill=BOTH, expand=True)
    frame5.pack_forget()
    frame6.pack_forget()
    frame4.pack_forget()
    frame7.pack_forget()

    sub_frame_31 = Frame(frame31, borderwidth=5, bg="grey")
    sub_frame_31.pack(fill=BOTH, side=TOP, ipady=700, ipadx=200, padx=10, pady=10, expand=True)
    st_code = Label(sub_frame_31,text="Student code",bg='white',font=("Helvetica bold",13))
    st_code.pack(side=TOP,pady=7,anchor='n')
    st_code_entry = Entry(sub_frame_31,borderwidth=5)
    st_code_entry.pack(side=TOP,pady=5,anchor='n')


    
    def code_value():
        global st_code  # Use the global keyword to modify the global variable
        st_code = st_code_entry.get()
        st_code =int(st_code)
        print(st_code,type(st_code))
    button_submit = Button(sub_frame_31, text="SUBMIT", fg="white", bg="green",command=code_value)
    button_submit.pack(side=LEFT,anchor='s', pady=10,padx=10,ipadx=10,ipady=5,)



   
def frame_4():
    
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    frame4.pack(fill=BOTH, expand=True)
    frame5.pack_forget()
    frame31.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()

    sub_frame_4 = Frame(frame4, borderwidth=5, bg="grey")
    sub_frame_4.pack(fill=BOTH, side=TOP, ipady=700, ipadx=200, padx=10, pady=10, expand=True)

    canvas = Canvas(sub_frame_4, relief=SUNKEN, bg='lightblue')
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(sub_frame_4, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas, bg='green')
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    inner_frame.bind("<Configure>", on_configure)
    headers = ["Name", "USN","Student code", "Classes_attended","Classes_Taken",]
    for col, header in enumerate(headers):
        label = Label(inner_frame, text=header, width=20, bg="pink", padx=5, pady=3, relief=SOLID)
        label.grid(row=0, column=col, sticky="nsew")

    conn = sqlite3.connect('aftab_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_data')
    cursor.execute('''
    SELECT student_data.NAME, student_data.USN, student_data.CODE, student_data.CLASS_T, student_data.CLASS_A
    FROM student_data
    WHERE student_data.CODE = ?
    ''', (st_code,))
    students_data = cursor.fetchall()
   
    
    for row, student in enumerate(students_data, start=1):
        for col, data in enumerate(student):
            label = Label(inner_frame, text=data, width=20, bg="lightyellow", padx=5, pady=3, relief=SOLID)
            label.grid(row=row, column=col, sticky="nsew")

    for col in range(len(headers)):
        inner_frame.grid_columnconfigure(col, weight=1)

    for row in range(len(students_data) + 1):  
        inner_frame.grid_rowconfigure(row, weight=1)

    conn.commit()
    conn.close()





def frame_5():
    
    def on_absent_click(absent, usn):
        
          

        
        conn = sqlite3.connect('aftab_data.db')
        cursor = conn.cursor()

        
        cursor.execute('SELECT CLASS_T FROM student_data WHERE USN = ?', (usn,))
        current_value = cursor.fetchone()[0]

        new_value = current_value + 1

        cursor.execute('UPDATE student_data SET CLASS_T = ? WHERE USN = ?', (new_value, usn))
        conn.commit()
        conn.close()

    def on_present_click(present, usn):
        
          
        conn = sqlite3.connect('aftab_data.db')
        cursor = conn.cursor()

        
        cursor.execute('SELECT CLASS_A FROM student_data WHERE USN = ?', (usn,))
        current_value = cursor.fetchone()[0]

        new_value = current_value + 1

        cursor.execute('UPDATE student_data SET CLASS_A = ? WHERE USN = ?', (new_value, usn))

        cursor.execute('SELECT CLASS_T FROM student_data WHERE USN = ?', (usn,))
        current_value1 = cursor.fetchone()[0]

        new_value1 = current_value1 + 1

        cursor.execute('UPDATE student_data SET CLASS_T = ? WHERE USN = ?', (new_value1, usn))

        conn.commit()
        conn.close()


        
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    frame5.pack(fill=BOTH, expand=True)
    frame4.pack_forget()
    frame31.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()

    sub_frame_5 = Frame(frame5, borderwidth=5, bg="grey")
    sub_frame_5.pack(fill=BOTH, side=TOP, ipady=700, ipadx=200, padx=10, pady=10, expand=True)

    canvas = Canvas(sub_frame_5, relief=SUNKEN, bg='lightblue')
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(sub_frame_5, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas, bg='green')
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    inner_frame.bind("<Configure>", on_configure)
    headers = ["Name", "USN","ABSENT","PRESENT"]
    for col, header in enumerate(headers):
        label = Label(inner_frame, text=header, width=20, bg="pink", padx=5, pady=3, relief=SOLID)
        label.grid(row=0, column=col, sticky="nsew")

    conn = sqlite3.connect('aftab_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_data')
    cursor.execute('''
    SELECT student_data.NAME, student_data.USN, student_data.CODE, student_data.CLASS_T, student_data.CLASS_A
    FROM student_data
    WHERE student_data.CODE = ?
    ''', (st_code,))


    students_data = cursor.fetchall()
    
    datas = []

    for data in students_data:
        modified_tuple = (data[0], data[1])
        datas.append(modified_tuple)


    
    for row, student in enumerate(datas, start=1):
        for col, data in enumerate(student):
            label = Label(inner_frame, text=data, width=20, bg="lightyellow", padx=5, pady=3, relief=SOLID)
            label.grid(row=row, column=col, sticky="nsew")
        absent = Button(inner_frame, text="ABSENT", command=lambda usn=student[1]: on_absent_click(absent, usn),bg="red",fg="white",font=("helvetica bold",10))
        absent.grid(row=row, column=len(student), sticky="nsew")

        present = Button(inner_frame, text="PRESENT", command=lambda usn=student[1]: on_present_click(present, usn),bg='green',fg="white",font=("helvetica bold",10))
        present.grid(row=row, column=len(student) + 1, sticky="nsew")
        
    for col in range(len(headers)):
        inner_frame.grid_columnconfigure(col, weight=1)

    for row in range(len(students_data) + 1):  
        inner_frame.grid_rowconfigure(row, weight=1)


def frame_6():
    frame6.pack(fill=BOTH, expand=True)
    frame5.pack_forget()
    frame31.pack_forget()
    frame4.pack_forget()
    frame7.pack_forget()
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    sub_frame_6 = Frame(frame6, borderwidth=5, bg="grey")
    sub_frame_6.pack(fill=BOTH, side=TOP, ipady=700, ipadx=200, padx=10, pady=10, expand=True)

    canvas = Canvas(sub_frame_6, relief=SUNKEN, bg='lightblue')
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(sub_frame_6, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = Frame(canvas, bg='green')
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    inner_frame.bind("<Configure>", on_configure)
    
    headers = ["Name", "USN", "Persentage","Classes_attended","Classes_Taken"]
    for col, header in enumerate(headers):
        label = Label(inner_frame, text=header, width=20, bg="pink", padx=5, pady=3, relief=SOLID)
        label.grid(row=0, column=col, sticky="nsew")

    conn = sqlite3.connect('aftab_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_data')
    cursor.execute('''
    SELECT student_data.NAME, student_data.USN, student_data.CODE, student_data.CLASS_T, student_data.CLASS_A
    FROM student_data
    WHERE student_data.CODE = ?
    ''', (st_code,))


    students_data = cursor.fetchall()
    
    
    students_data1 =[list(inner_row) for inner_row in students_data]


    for student in students_data1:
        attend_class = student[3]
        total_class_taken = student[4]
        
        print(attend_class,total_class_taken)
    
    
        if total_class_taken > 0:
            attendance_percentage = ( total_class_taken/attend_class )*100
        
            student[2]= str(attendance_percentage)+"%"
            
        else:
            student[2]=0
    print(attendance_percentage)




    
    for row, student in enumerate(students_data1, start=1):
        for col, data in enumerate(student):
            label = Label(inner_frame, text=data, width=20, bg="lightyellow", padx=5, pady=3, relief=SOLID)
            label.grid(row=row, column=col, sticky="nsew")

    for col in range(len(headers)):
        inner_frame.grid_columnconfigure(col, weight=1)

    for row in range(len(students_data) + 1): 
        inner_frame.grid_rowconfigure(row, weight=1)

def frame_7():
    frame7.pack(fill=BOTH, expand=True)
    frame5.pack_forget()
    frame31.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()
    def add_detail():
        name = st_name_entry.get()
        usn = st_usn_entry.get()
        count2 = classes_taken_entry.get()
        count1 = classes_attended_entry.get()
        code = st_code_entry.get()
        
        print(f"Values: Name={name}, USN={usn}, Classes Taken={count1}, Classes Attended={count2}, Code={code}")


        conn = sqlite3.connect("aftab_data.db")
        cursor = conn.cursor()

        try:
            
            cursor.execute('''SELECT * FROM student_data WHERE USN=?''', (usn,))
            existing_record = cursor.fetchone()

            if existing_record:
                
                cursor.execute('''UPDATE student_data SET NAME=?, CODE=?, CLASS_A=?, CLASS_T=? WHERE USN=?''',
                               (name, usn, code,count1, count2,))
            else:
                cursor.execute('''INSERT INTO student_data(NAME, USN, CODE, CLASS_A, CLASS_T) VALUES(?,?,?,?,?)''',
                               (name, usn,code, count1, count2))

            conn.commit()

            
            cursor.execute('''SELECT * FROM student_data WHERE USN=?''', (usn,))
            updated_record = cursor.fetchone()
            print(f"Updated Record: {updated_record}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

        finally:
            conn.close()

    sub_frame = Frame(frame7, borderwidth=5, bg="grey")
    sub_frame.pack(fill=BOTH, side=TOP, ipady=700, ipadx=200, padx=10, pady=10, expand=True)

    label_col_name1 = Label(sub_frame, text="New student entry", fg="brown", bg="white", font=("helvetica bold", 20),
                            relief=SUNKEN)
    label_col_name1.pack(side=TOP, anchor='n')

    entry_frame =Frame(sub_frame,borderwidth=5,bg="white",relief=SUNKEN)
    entry_frame.pack(side=TOP,ipady=600,ipadx=200,padx=10,pady=10)
    

    st_name = Label(entry_frame,text="Student Name",bg='white',font=("Helvetica bold",13))
    st_name.pack(side=TOP,pady=7,anchor='n')
    st_name_entry = Entry(entry_frame,borderwidth=5)
    st_name_entry.pack(side =TOP,pady=7,anchor='n')
    
    
    st_usn = Label(entry_frame,text="Student USN",bg='white',font=("Helvetica bold",13))
    st_usn.pack(side=TOP,pady=7,anchor='n')
    st_usn_entry = Entry(entry_frame,borderwidth=5)
    st_usn_entry.pack(side=TOP,pady=5,anchor='n')

        
    st_code = Label(entry_frame,text="Student code",bg='white',font=("Helvetica bold",13))
    st_code.pack(side=TOP,pady=7,anchor='n')
    st_code_entry = Entry(entry_frame,borderwidth=5)
    st_code_entry.pack(side=TOP,pady=5,anchor='n')
    
    
    classes_taken = Label(entry_frame,text="No of clases taken",bg='white',font=("Helvetica bold",11))
    classes_taken.pack(side=TOP,pady=7,anchor='n')
    classes_taken_entry = Entry(entry_frame,borderwidth=5)
    classes_taken_entry.pack(side=TOP,pady=5,anchor='n')
    
    
    classes_attended = Label(entry_frame,text="No of clases attended",bg='white',font=("Helvetica bold",11))
    classes_attended.pack(side=TOP,pady=7,anchor='n')
    classes_attended_entry = Entry(entry_frame,borderwidth=5)
    classes_attended_entry.pack(side=TOP,pady=5,anchor='n')
    
    

    

    button_add=Button(entry_frame,text="ADD",fg="white",bg="blue",font=("Helvetica bold",14),command=add_detail)
    button_add.pack(side=TOP,pady=10,anchor='n')
    


    

root = Tk()
root.geometry("1200x700")
root.title("Student attendance management system")
root.resizable(False, False)

frame1 = Frame(root, borderwidth=5, bg="blue")
frame1.pack(fill=BOTH, expand=True)

frame2 = Frame(frame1, borderwidth=5, bg="white", width=200)
frame2.pack(side=LEFT, fill=BOTH, expand=False)

frame3 = Frame(frame1, borderwidth=1, bg="white")
frame3.pack(fill=BOTH, expand=True)

frame31 = Frame(frame1, borderwidth=5, bg="pink", width=750, height=700)
frame4 = Frame(frame1, borderwidth=5, bg="lightgreen", width=750, height=700)
frame5 = Frame(frame1, borderwidth=5, bg="lightcoral", width=750, height=700)
frame6 = Frame(frame1, borderwidth=5, bg="lightblue", width=750, height=700)
frame7 = Frame(frame1, borderwidth=5, bg="lightgrey", width=750, height=700)

frame_31()

logo1 = PhotoImage(file="logo.png")
logo2 = logo1.subsample(8, 8)

label_logo = Label(frame3, image=logo2)
label_logo.pack(side=LEFT, anchor='nw', ipadx=5, ipady=5)

label_col_name = Label(frame3, text="VIJAYA VITTALA INSTITUTE OF TECHNOLOGY", fg="brown", bg="white",
                       font=("helvetica bold", 14))
label_col_name.pack(side=TOP, anchor='nw')

label_title = Label(frame3, text="Student Attendance Management System", fg="Red", bg="white",
                    font=("helvetica bold", 14))
label_title.pack(side=TOP, anchor='sw')
labe6 = Label(frame3, text="This project is prototype,made by AFTAB AND MOHAMMAD SAAD KHAN of 5th sem ,3rd year ,AI&ML Branch", fg="green", bg="white",
              font=("helvetica bold", 12))
labe6.pack(padx=20)



button_frame31 = Button(frame3, text="details", fg="black", bg="blue", command=frame_31)
button_frame31.pack(side=LEFT, anchor='sw', padx=5)

button_frame4 = Button(frame3, text="Student_list", fg="black", bg="lightgreen", command=frame_4)
button_frame4.pack(side=LEFT, anchor='sw', padx=5)

button_frame5 = Button(frame3, text="Update_Att", fg="black", bg="lightcoral", command=frame_5)
button_frame5.pack(side=LEFT, anchor='sw', padx=5)

button_frame6 = Button(frame3, text="Att_Percentage", fg="black", bg="lightblue", command=frame_6)
button_frame6.pack(side=LEFT, anchor='sw', padx=5)

button_frame7 = Button(frame3, text="Add_student", fg="black", bg="lightgrey", command=frame_7)
button_frame7.pack(side=LEFT, anchor='sw', padx=5)

button_EXIT = Button(frame2, text="EXIT", fg="white", bg="red",command=root.destroy)
button_EXIT.pack(side=LEFT,anchor='s', pady=10,padx=10,ipadx=10,ipady=5,)

root.mainloop()




