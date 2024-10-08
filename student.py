from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")

        #_______VARIABLES_________
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #first image
        img=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\s3.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\s2.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\developer.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\bg.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #title
        title_lbl=Label(bg_img,text="Student Management System" ,font=("times new roman",35,"bold"),bg="white", fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=47)

        #main frame
        main_farme=Frame(bg_img,bd=2,bg="white")
        main_farme.place(x=5,y=55,width=1480,height=600)
        

        #left label frame
        Left_frame=LabelFrame(main_farme,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=500)

        #image
        #img_left=Image.open(r"C:\Users\iram2\OneDrive\Desktop\FACE RECOGNIATION\college_images\developer.jpg")
        #img_left=img_left.resize((600,130))
        #self.photoimg_left=ImageTk.PhotoImage(img_left)

        #f_lbl=Label(Left_frame,image=self.photoimg_left)
        #f_lbl.place(x=5,y=0,width=600,height=130)

        #Course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=600,height=110)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CS","IT","Civil","Mechanical","Electrical","Telecommunication")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","SEM-1","SEM-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Class Student informatio
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information", font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=120,width=600,height=300)
        
        #ID
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #class Division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,sticky=W)
        
        #Rollno
        roll_no_label=Label(class_Student_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=17,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        #Gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,sticky=W)
        
        #DOB
        dob_label=Label(class_Student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=17,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)
          

        #Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)
        
        #phone no
        phone_label=Label(class_Student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=17,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,sticky=W)
        
        #Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,sticky=W)

       
        
        #teacher
        teacher_label=Label(class_Student_frame,text="Teacher:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=17,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take photo Sample" , value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo Sample" , value="No")
        radiobtn2.grid(row=6,column=1)

        #button Frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=195,width=600,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame2=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame2.place(x=5,y=235,width=600,height=40)
       
        take_photo_btn=Button(btn_frame2,text="Take photo Sample",command=self.generate_dataset,width=32,font=("times new roman",12,"bold"),bg="blue",fg="red")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame2,text="Update photo Sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="red")
        update_photo_btn.grid(row=1,column=1)



        #right label frame
        Right_frame=LabelFrame(main_farme,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=610,height=500)
        
        #search frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System", font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=0,width=600,height=67)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="purple",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=10,state="readonly")
        search_combo["values"]=("Select","Phone_no","Roll_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)



        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=70,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #teacher_entry=ttk.Entry(class_Student_frame,width=17,font=("times new roman",12,"bold"))
        #teacher_entry.grid(row=4,column=3,padx=10,sticky=W)


        #_________________function decration_____________

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@1234" , database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
                                                                                                              self.var_dep.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_std_id.get(),
                                                                                                              self.var_std_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get()
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #____________ FETCH DATA __________________
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@1234" , database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
       


#__________________get cursor ___________________________
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus) 
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #___________update function____________
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        
        else:
            try:
                Update=messagebox.askyesno("Update", "Do ypu want to update student details",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="Test@1234" , database="face_recognition")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update student set Dep=%s,Course=%s,Year1=%s,Semester=%s,Student_id=%s,St_Name=%s,Division=%s,Rollno=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.var_std_id.get()

                                                                                                                                                                                                                                                    


                                                                                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details Successfully UPDATED",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #_______________delete function______________________________
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete Student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@1234" , database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Dlete","Successfully deleted the student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #____________reset function__________________________
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Geneder")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    #___________________________GENERATE DATA SET TAKE PHOTO SAMPLE_____________
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="Test@1234" , database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year1=%s,Semester=%s,Student_id=%s,St_Name=%s,Division=%s,Rollno=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.var_std_id.get()==id+1

                                                                                                                                                                                                                                                    


                                                                                                                                                                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_dat()
                    conn.close()
                    #_________load predifiend data on face frontals from openvcv__________

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3(default value)
                        #Minimum Neighbour=5
                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                    #to open webcamera
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            # yaha face h my_frame
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                        
                        
                    
                
                    


        






                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                     
                                                                                                             


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()