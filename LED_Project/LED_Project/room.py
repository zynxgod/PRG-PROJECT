from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import sqlite3
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(screen_width*0.85)}x{int(screen_height*0.78)}+198+170")

        #================varibales================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #================title================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=int(screen_width*0.85),height=50)

        #================labelframe================
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",padx=2,font=("times new roman",12,"bold"))
        Labelframeleft.place(x=5,y=50,width=425,height=490)

        #================labels and entry================

        # customer contact
        lbl_cust_contact=Label(Labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(Labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)

        # featch data button
        btnFetchData=Button(Labelframeleft,command=self.Fetch_contact,text="Featch Data",font=("arial",9,"bold"),bg="black",fg="gold",width=9)
        btnFetchData.place(x=340,y=4)

        # check in date
        check_in_date=Label(Labelframeleft,text="Check-in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(Labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        # check out date
        lbl_Check_out=Label(Labelframeleft,text="Check-Out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(Labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        # room type
        label_RoomType=Label(Labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
 
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT RoomType FROM room_details")
        rows = cursor.fetchall()

        combo_RoomType=ttk.Combobox(Labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # available
        lblRoomAvailable=Label(Labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT RoomNo FROM room_details")
        rows1 = cursor.fetchall()

        combo_RoomNo=ttk.Combobox(Labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows1
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)
        
        # meal
        label_Meal=Label(Labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        label_Meal.grid(row=5,column=0,sticky=W)

        combo_Meal=ttk.Combobox(Labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Meal["value"]=("BreakFast","Lunch","Dinner")
        combo_Meal.current(0)
        combo_Meal.grid(row=5,column=1)

        # no of days
        lblNoOfDays=Label(Labelframeleft,text="No Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(Labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        # paid tax
        lblNoOfDays=Label(Labelframeleft,text="Paid tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(Labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        # sub total
        lblNoOfDays=Label(Labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(Labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        # total cost 
        lblIdNumber=Label(Labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(Labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #================bill button================

        btnBill=Button(Labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #================btns================
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #================right side image================
        img3=Image.open(r"c:\Users\safal\Downloads\room.png")
        img3 = img3.resize((500,300), Image.LANCZOS)   
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg3=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg3.place(x=750, y=55, width=500, height=300)

        #================tabel frame & search system================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils & Search System",padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=15)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)

        #================Show data Table================

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal",
                                                                   "noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
   

        self.room_table["show"]="headings"
        
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()

                cursor.execute('''
                INSERT INTO room_bookings (
                    CustomerContact, CheckInDate, CheckOutDate, RoomType,
                    RoomNumber, MealPlan, NumberOfDays, PaidTax, SubTotal, TotalCost
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(),
                self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(),
                self.var_noofdays.get(), self.var_paidtax.get(), self.var_actualtotal.get(),
                self.var_total.get()
                ))

                conn.commit()
                conn.close()
                self.fetch_data()  
                messagebox.showinfo("Success", "Room Booked successfully", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM room_bookings")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert('', END, values=row)
            conn.close()

    def get_cursor(self, event):
        selected_row = self.room_table.focus()  
        data = self.room_table.item(selected_row)  
        row = data['values'] if 'values' in data else None  

        if row:
            self.var_contact.set(row[0])  
            self.var_checkin.set(row[1])  
            self.var_checkout.set(row[2])  
            self.var_roomtype.set(row[3])  
            self.var_roomavailable.set(row[4])  
            self.var_meal.set(row[5])  
            self.var_noofdays.set(row[6])  
            self.var_paidtax.set(row[7])  
            self.var_actualtotal.set(row[8]) 
            self.var_total.set(row[9])  

    def update_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a booking to update", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()

                cursor.execute('''
                    UPDATE room_bookings SET
                    CustomerContact = ?, CheckInDate = ?, CheckOutDate = ?, RoomType = ?,
                    RoomNumber = ?, MealPlan = ?, NumberOfDays = ?, PaidTax = ?, SubTotal = ?, TotalCost = ?
                    WHERE CustomerContact = ?
                ''', (
                    self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(),
                    self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(),
                    self.var_noofdays.get(), self.var_paidtax.get(), self.var_actualtotal.get(),
                    self.var_total.get(), self.var_contact.get()
                ))

                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Booking updated successfully", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a booking to delete", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()

                cursor.execute("DELETE FROM room_bookings WHERE CustomerContact = ?", (self.var_contact.get(),))

                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Booking deleted successfully", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("Single")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
    
    def search_data(self):
        search_by = self.search_var.get()
        search_value = self.txt_search.get()

        if search_value == "":
            messagebox.showerror("Error", "Please enter a search value", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()

                if search_by == "Contact":
                    cursor.execute("SELECT * FROM room_bookings WHERE CustomerContact=?", (search_value,))
                elif search_by == "Room":
                    cursor.execute("SELECT * FROM room_bookings WHERE RoomNumber=?", (search_value,))

                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.room_table.delete(*self.room_table.get_children())
                    for row in rows:
                        self.room_table.insert('', END, values=row)
                else:
                    messagebox.showinfo("Info", "No records found", parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
          
        

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn = sqlite3.connect('hotel.db')
            cursor = conn.cursor()
            query = "SELECT Name FROM customers WHERE Mobile = ?"
            cursor.execute(query, (self.var_contact.get(),))
            row = cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=430,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                #==============Gender===================
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                query = "SELECT Gender FROM customers WHERE Mobile = ?"
                cursor.execute(query, (self.var_contact.get(),))
                row = cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #===============email================
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                query = "SELECT Email FROM customers WHERE Mobile = ?"
                cursor.execute(query, (self.var_contact.get(),))
                row = cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #===============nationality================
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                query = "SELECT Nationality FROM customers WHERE Mobile = ?"
                cursor.execute(query, (self.var_contact.get(),))
                row = cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #===============address===================
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                query = "SELECT Address FROM customers WHERE Mobile = ?"
                cursor.execute(query, (self.var_contact.get(),))
                row = cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl1=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl1.place(x=90,y=120)


    def total(self):
        try:
        
            inDate = self.var_checkin.get()
            outDate = self.var_checkout.get()

        
            inDate = datetime.strptime(inDate, "%d/%m/%Y")  
            outDate = datetime.strptime(outDate, "%d/%m/%Y")  

        
            num_days = abs((outDate - inDate).days)
            self.var_noofdays.set(num_days)

        
            room_costs = {
                "Single": 5000,  
                "Double": 8000,  
                "Luxury": 12000  
            }

            meal_costs = {
                "Breakfast": 1000,  
                "Lunch": 2000,      
                "Dinner": 3000     
            }

            room_type = self.var_roomtype.get()
            meal_plan = self.var_meal.get()

        
            if room_type in room_costs:
                room_cost = room_costs[room_type] * num_days
            else:
                raise ValueError("Invalid room type selected.")

        
            if meal_plan in meal_costs:
                meal_cost = meal_costs[meal_plan] * num_days
            else:
                raise ValueError("Invalid meal plan selected.")

        
            subtotal = room_cost + meal_cost

       
            tax = subtotal * 0.1

        
            total_cost = subtotal + tax

        
            self.var_paidtax.set(f"Rs. {tax:.2f}")
            self.var_actualtotal.set(f"Rs. {subtotal:.2f}")
            self.var_total.set(f"Rs. {total_cost:.2f}")

        except ValueError as e:
        
            messagebox.showerror("Error", f"Invalid input: {str(e)}", parent=self.root)
        except Exception as e:
        
            messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)


                
if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
        