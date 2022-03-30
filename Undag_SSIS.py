from tkinter import *
from tkinter import ttk
from tkinter.font import ITALIC
import tkinter.messagebox
import tkinter.ttk as ttk
import csv
import os
import time


class Student:
    
    def __init__ (self,root):
        self.root = root
        blank_space = ""
        self.root.title(200 * blank_space + "Student Information System")
        self.root.geometry("1174x700+200+50")
        self.root.configure(bg="white")
        self.root.resizable(False,False)
        self.data = dict()
        self.temp = dict()
        self.filename = "Data.csv"

        #========= VARIABLES =========#
        IDNum = StringVar()
        FName = StringVar()
        MName = StringVar()
        LName = StringVar()
        Course = StringVar()
        YLevel = StringVar()
        Gender = StringVar()
        sbar = StringVar()
        
        if not os.path.exists('Data.csv'):
            with open('Data.csv', mode='w') as csv_file:
                fieldnames = ["ID Number", "First Name", "Middle Name", "Last Name","Course", "Year Level", "Gender"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        
        else:
            with open('Data.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student ID Number"]] = {'First Name': row["First Name"], 'Middle Name': row["Middle Name"], 'Last Name': row["Last Name"], 'Course': row["Course"],'Year Level': row["Year Level"], 'Gender': row["Gender"]}
            self.temp = self.data.copy()
        
        
         
         #========= FRAMES =========#
        
        bgf = Frame(self.root, bd=7, width=1700, height=1700, relief=RIDGE, bg="#003A6C")
        bgf.grid()

        frame1 = Frame(root, bg = "#003A6C", relief= GROOVE, borderwidth = 5)
        frame1.place(x=15, y=15, width = 300, height = 673)

        
        dataentryframe2 = Frame(root, bg = "#6C3200", relief= RIDGE)
        dataentryframe2.place(x=25, y=530, width = 280, height = 140)

        SFrame = Frame(root, bg = "#6C3200", width = 300, height = 100, relief = RIDGE)
        SFrame.grid(row =3, column =0)
        SFrame.place(x = 580, y = 170)


        showdataframe = Frame(root, bg = "white", relief = GROOVE, borderwidth = 5)
        showdataframe.place(x= 340, y = 280, width = 800, height = 400)

        titledataframe = Frame(root, bg = "#003A6C", relief = RIDGE)
        titledataframe.place (x = 340, y = 15, width = 800, height = 145)

        #========= ENTRY =========#
        self.ID = Label(frame1, font=('Vogue',12), text="STUDENT ID:",bg="#003A6C", fg = "white", bd=5 , anchor=W)
        self.ID.grid(row=0, column=0, sticky=W, padx=5)
        self.IDtxt = Entry(frame1, font=('times',12), width=40, justify='center', textvariable = IDNum)
        self.IDtxt.grid(row=0, column=1)
        self.ID.place(x = 90, y = 65)
        self.IDtxt.place(x = 20, y = 85, width =250)
        self.IDtxt.insert(0, "YYYY-NNNN")

        self.FName = Label(frame1, font=('Vogue',12), text="First Name:",bg="#003A6C", fg = "white", bd=5 , anchor=W)
        self.FName.grid(row=0, column=0, sticky=W, padx=5)
        self.FNametxt = Entry(frame1, font=('times',12), width=40, justify='center', textvariable = FName)
        self.FNametxt.grid(row=0, column=1)
        self.FName.place(x = 90, y = 125)
        self.FNametxt.place(x = 20, y = 145, width =250)

        self.MName = Label(frame1, font=('Vogue',12), text="Middle Initial:",bg="#003A6C", fg = "white", anchor=W)
        self.MName.grid(row=0, column=0, sticky=W, padx=5)
        self.MNametxt = Entry(frame1, font=('times',12), width=40, justify='center', textvariable = MName)
        self.MNametxt.grid(row=0, column=1)
        self.MName.place(x = 90, y = 185)
        self.MNametxt.place(x = 20, y = 205, width =250)

        self.LName = Label(frame1, font=('Vogue',12), text="Last Name:",bg="#003A6C", fg = "white", bd=5 , anchor=W)
        self.LName.grid(row=0, column=0, sticky=W, padx=5)
        self.LNametxt = Entry(frame1, font=('times',12), width=40, justify='center', textvariable = LName)
        self.LNametxt.grid(row=0, column=1)
        self.LName.place(x = 90, y = 245)
        self.LNametxt.place(x = 20, y = 265, width =250)

        self.Course = Label(frame1, font=('Vogue',12), text="Course:",bg="#003A6C", fg = "white", bd=5 , anchor=W)
        self.Course.grid(row=0, column=0, sticky=W, padx=5)
        self.Coursetxt = Entry(frame1, font=('times',12), width=40, justify='center', textvariable = Course)
        self.Coursetxt.grid(row=0, column=1)
        self.Course.place(x = 100, y = 305)
        self.Coursetxt.place(x = 20, y = 325, width =250)

        self.YLevel = Label(frame1, font=('Vogue',12), text="Year Level:",bg="#003A6C", fg = "white", bd=5 , anchor=W)
        self.YLevel.grid(row=0, column=0, sticky=W, padx=5)
        self.YLevel.place(x = 90, y = 365)

        self.pYLevel = ttk.Combobox(frame1, font=('times',12,'bold'), state='readonly', width=39, textvariable = YLevel)
        self.pYLevel['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year')
        self.pYLevel.grid(row=6, column=1)
        self.pYLevel.place(x=20,y=385, width=250)


        self.Gender = Label(frame1, font=('Vogue',12), text="Gender:",bg="#003A6C", fg = "white", bd=5 , anchor=W)
        self.Gender.grid(row=0, column=0, sticky=W, padx=5)
        
        self.Gender.place(x = 100, y = 425)
    
        self.pGender = ttk.Combobox(frame1, font=('times',12,'bold'), state='readonly', width=40, textvariable = Gender)
        self.pGender['values'] = ('Female', 'Male')
        self.pGender.grid(row=5, column=1)
        self.pGender.place(x = 20, y = 445, width = 250)

        self.sbar = Entry(SFrame, font=('times',12,'bold'), textvariable = sbar, width = 29 )
        self.sbar.place(x=35,y=20)





        #========= TITLE =========#
        title=Label(titledataframe, text = "Student Information System", font = ('Old English Text MT', 48), foreground = 'white', background = '#003A6C')
        title.place(x=13, y=25)

        title2=Label(titledataframe, text = "SAINT CLAIRE'S ACADEMY", font = ('times', 20), foreground = 'white', background = '#003A6C')
        title2.place(x=225, y=5)

        title2=Label(titledataframe, text = "VERITAS LIBERABIT VOS", font = ('times', 18, ITALIC), foreground = 'white', background = '#003A6C')
        title2.place(x=255, y=95)


        #========= FUNCTIONS =========#
        def Exit():
            Exit = tkinter.messagebox.askyesno("St. Claire's Student Information System","Are you sure you want to leave?")
            if Exit > 0:
                root.destroy()
                return

            
        def Add():
            with open('Data.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if IDNum.get()=="" or FName.get()=="" or MName.get()=="" or LName.get()=="" or YLevel.get()=="":
                    tkinter.messagebox.showinfo("SC-SIS","This field is required.")
                else:
                    self.data[IDNum.get()] = {'Last Name': LName.get(), 'First Name': FName.get(), 'Middle Name': MName.get(), 'Course': Course.get(),'Year Level': YLevel.get(), 'Gender': Gender.get()}
                    self.Save()
                    tkinter.messagebox.showinfo("SC-SIS", "Thank you!")
                Clear()
                Display()

               
        
        def Clear():
            IDNum.set("")
            FName.set("")
            MName.set("")
            LName.set("")
            Course.set("")
            YLevel.set("")
            Gender.set("")
        
        
        def Display():
            tree.delete(*tree.get_children())
            with open('Data.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    IDNumber=row['Student ID Number']
                    FirstName=row['First Name']
                    MiddleName=row['Middle Name']
                    LastName=row['Last Name']
                    Course=row['Course']
                    YearLevel=row['Year Level']
                    Gender=row['Gender']
                    tree.insert("",END, values=(IDNumber, FirstName, MiddleName, LastName, Course, YearLevel, Gender))
                    
      
        def Delete():
            if tree.focus()=="":
                tkinter.messagebox.showerror("SC-SIS","You may select your record to delete.")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.Save()
            tree.delete(tree.focus())
            tkinter.messagebox.showinfo("SC-SIS","Deleted successfully.")
       

        def Edit():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Select any record")
                return
            values = tree.item(tree.focus(), "values")
            IDNum.set(values[0])
            FName.set(values[1])
            MName.set(values[2])
            LName.set(values[3])
            Course.set(values[4])
            YLevel.set(values[5])
            Gender.set(values[6])

        def Search():
            if self.sbar.get() in self.data:
                vals = list(self.data[self.sbar.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.sbar.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
            elif self.sbar.get() == "":
                Display()
            else:
                tkinter.messagebox.showerror("Student Information System","Student not found")
                return


        def Update():
            with open('Data.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if IDNum.get()=="" or FName.get()=="" or MName.get()=="" or LName.get()=="" or YLevel.get()=="":
                    tkinter.messagebox.showinfo("SIS","Please select a student record from the table")
                else:
                    self.data[IDNum.get()] = {'First Name': FName.get(), 'Middle Name': MName.get(), 'Last Name': LName.get(), 'Course': Course.get(),'Year Level': YLevel.get(), 'Gender': Gender.get()}
                    self.Save()
                    tkinter.messagebox.showinfo("SIS", "Updated")
                Clear()
                Display() 

        def time1():
            time_string = time.strftime("%H:%M:%S")
            date_string = time.strftime("%d:%m:%y")
            clock.config(text="Time: "+time_string+"\n""Date: "+date_string, font =('Vogue', 15, 'bold'))
            clock.after(200, time1)

        #========= BUTTONS =========#
        button1 = Button(dataentryframe2, text = "Clear Input", font = ('Vogue', 12), width = 12, padx=2, background = "#6C3200", foreground = "white", command=Clear)
        button1.place(x=10, y = 20)
        
        button2 = Button(dataentryframe2, text = "Add Student", font = ('Vogue', 12), width = 12, padx=2, background = "#6C3200", foreground = "white", command=Add)
        button2.place(x=140, y = 20)
        
        button3 = Button(dataentryframe2, text = "Update", font = ('Vogue', 12), width = 12, padx=2, background = "#6C3200", foreground = "white", command=Update)
        button3.place(x=10, y = 60)
        
        button4 = Button(dataentryframe2, text = "Delete", font = ('Vogue', 12), width = 12, padx=2, background = "#6C3200", foreground = "white", command=Delete)
        button4.place(x=10, y = 100)
        
        button6 = Button(dataentryframe2, text = "Edit", font = ('Vogue', 12), width = 12, padx=2, background = "#6C3200", foreground = "white", command=Edit)
        button6.place(x=140, y = 60)
        
        button5 = Button(dataentryframe2, text = "Exit", font = ('Vogue', 12), width = 12, padx=2, background = "#6C3200", foreground = "white", command=Exit)
        button5.place(x=140, y = 100)

        clock = Label(frame1, font = ('vogue', 15, 'bold'), width = 15, relief = RIDGE, background = '#6C3200', foreground = 'white')
        clock.place(x = 70, y = 10, width = 150)
        time1()


        self.Search=Button(SFrame, pady=1,bd=4,font=('Vogue',12), padx=2, width=15, text='ID Number Search',background = "#6C3200", foreground = "white", command = Search)
        self.Search.place(x=80,y=50)
        



        #========= TREEVIEWS =========#
        scroll_y=Scrollbar(showdataframe, orient=VERTICAL)
        

        tree = ttk.Treeview(showdataframe, height=15, columns=("Student ID Number", "First Name", "Middle Name", "Last Name", "Course", "Year Level", "Gender"), yscrollcommand=scroll_y.set)
        scroll_y.config(command=tree.yview)
        scroll_y.pack(side=RIGHT, fill=Y)

        tree.heading("Student ID Number", text="Student ID Number")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Name", text="Middle Initial")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Course", text="Course")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Gender", text="Gender")
        tree['show'] = 'headings'

        tree.column("Student ID Number", width=100)
        tree.column("First Name", width=90)
        tree.column("Middle Name", width=95)
        tree.column("Last Name", width=100)
        tree.column("Course", width=70)
        tree.column("Year Level", width=70)
        tree.column("Gender", width=80)
        tree.pack(fill=BOTH,expand=1)
        
        Display()

    #======================#
    def Save(self):
        temps = []
        with open('Data.csv', "w", newline ='') as update:
            fieldnames = ["Student ID Number","First Name","Middle Name","Last Name","Course","Year Level","Gender"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)


        
        
        
        






if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
