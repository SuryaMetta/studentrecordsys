#importing tkinter GUI
import tkinter as tk
from tkinter import ttk
 
studentdata_list = []  # Creating a list for storing user data
 
# Creation of a function that will be where the creation of the record of each individual student happens.
def student_info(roll, student_dict):
   global studentdata_list
 
   win = tk.Tk()  # Creation of a window.
   win.geometry("850x300")  # The size of the window holding the student record.
   win.title(f'STUDENT- {roll}')  # f followed by {} gives the value of the string in the print.
 
   # Creation of a label storing first name of student.
   fnlabel = tk.Label(win, text='First Name', bd=2, relief="groove")
   fnlabel.grid(row=0, column=0)#location
   fnentry = tk.Entry(win, width=50)
   fnentry.grid(row=0, column=1)
 
   # Creation of a label storing middle name of student.
   mnlabel = tk.Label(win, text='Middle Name', bd=2, relief="groove")
   mnlabel.grid(row=1, column=0)
   mnentry = tk.Entry(win, width=50)
   mnentry.grid(row=1, column=1)
 
   # Creation of a label storing last name of student.
   lnlabel = tk.Label(win, text='Last Name', bd=2, relief="groove")
   lnlabel.grid(row=2, column=0)
   lnentry = tk.Entry(win, width=50)
   lnentry.grid(row=2, column=1)
   name= f"{fnentry.get()} {mnentry.get()} {lnentry.get()}" #storing the full name
 
   #creation of a checkbox for gender.
   malelabel=tk.Label(win, text='Male',bd=2, relief="groove")
   malelabel.grid(row=3,column=0)
   male=tk.IntVar()
   male_checkbox=tk.Checkbutton(win,variable=male,)
   male_checkbox.grid(row=3,column=1)
   femalelabel=tk.Label(win, text='Female',bd=2, relief="groove")
   femalelabel.grid(row=4,column=0)
   female=tk.IntVar()
   female_checkbox=tk.Checkbutton(win,variable=female,)
   female_checkbox.grid(row=4,column=1)
 
   #creation of a listbox with a selector button and scrollbar for choosing course,degree-specialization.
   choice_sc= None
   def on_select():
       nonlocal choice_sc  
       selected_index = courses_listbox.curselection()
       choice_sc= selected_index
       if selected_index:
           selected_course = courses_listbox.get(selected_index[0])
           selected_course_label.config(text=f'Selected Course: {selected_course}')
   courselabel = tk.Label(win, text='Faculty',bd=2, relief="groove")
   courselabel.grid(row=5, column=0)
   scrollbar = tk.Scrollbar(win, orient=tk.VERTICAL)
   scrollbar.grid(row=5, column=2, sticky="ns")    
   courses_listbox = tk.Listbox(win, yscrollcommand=scrollbar.set, height=3,width=30)
   courses = [  #options of choice box
       'Engineering & Technology',
       'Medicine & Health Sciences',
       'Management',
       'Science & Humanities',
       'Law',
       'Agricultural Sciences',
       'Distance Education',
       'Online Education'
   ]
   for course in courses:
       courses_listbox.insert(tk.END, course)
   courses_listbox.grid(row=5, column=1)
   scrollbar.config(command=courses_listbox.yview)
   select_button = tk.Button(win, text="Select", command=on_select)
   select_button.grid(row=6, column=0, columnspan=2)
   selected_course_label = tk.Label(win, text="")
   selected_course_label.grid(row=7, column=0, columnspan=2)
   deplabel=tk.Label(win, text='Department',bd=2, relief="groove")
   deplabel.grid(row=8,column=0)
   depentry=tk.Entry(win)
   depentry.grid(row=8,column=1)
   spelabel=tk.Label(win, text='Specialization',bd=2, relief="groove")
   spelabel.grid(row=8,column=2)
   speentry=tk.Entry(win)
   speentry.grid(row=8,column=3)
 
#function to signal completion of data entry of student
   def on_next():
       nonlocal student_dict
       name = f"{fnentry.get()} {mnentry.get()} {lnentry.get()}"
       student_dict['Name'] = name
       student_dict['Gender'] = 'Male' if male.get() == 1 else 'Female'
       student_dict['Faculty'] = courses_listbox.get(choice_sc[0])
       student_dict['Department'] = depentry.get()
       student_dict['Specialization'] = speentry.get()
       studentdata_list.append(student_dict)
       win.destroy()
 
   #creation of a button to move to the next student.
   next=tk.Button(win, text='NEXT',width=15,command=on_next)
   next.grid(row=9,column=2)
 
   win.mainloop() #loop for keeping continous user interactions.
 
#function to show the final data of all students
def student_records():
   global studentdata_list
   finaldisplay = tk.Tk()
   finaldisplay.geometry("850x300")
   finaldisplay.title('RECORDS')
 
   #creation of a table
   tree = ttk.Treeview(finaldisplay)
 
   #creating and defining columns of the table
   tree["columns"] = ("Roll Number", "Name", "Gender", "Faculty", "Department", "Specialization")
   tree.column("#0", width=0, stretch=tk.NO)
   tree.column("Roll Number", anchor=tk.W, width=80)
   tree.column("Name", anchor=tk.W, width=280)
   tree.column("Gender", anchor=tk.W, width=50)
   tree.column("Faculty", anchor=tk.W, width=160)
   tree.column("Department", anchor=tk.W, width=100)
   tree.column("Specialization", anchor=tk.W, width=130)
 
   #heading of the columns of table
   tree.heading("Roll Number", text="Roll Number", anchor=tk.W)
   tree.heading("Name", text="Name", anchor=tk.W)
   tree.heading("Gender", text="Gender", anchor=tk.W)
   tree.heading("Faculty", text="Faculty", anchor=tk.W)
   tree.heading("Department", text="Department", anchor=tk.W)
   tree.heading("Specialization", text="Specialization", anchor=tk.W)
 
   #fills in the values
   for i, student_dict in enumerate(studentdata_list):
       tree.insert("", i, values=(
           student_dict['Roll'],
           student_dict['Name'],
           student_dict['Gender'],
           student_dict['Faculty'],
           student_dict['Department'],
           student_dict['Specialization']
       ))
 
   tree.pack(expand=True, fill="both")
 
   finaldisplay.mainloop()
#main function
def main():
   global studentdata_list
   num = int(input("Enter the Number of Students:"))
   for _ in range(num): #loop to run as many times as there are students
       roll = input("Enter the roll number of Student:")
       student_dict = {'Roll': roll}
       student_info(roll, student_dict)
   student_records()
 
if __name__ == "_main_":
   main()