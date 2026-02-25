from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import sqlite3
from tkinter import messagebox


class Cust_Win:

    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(screen_width*0.85)}x{int(screen_height*0.78)}+198+170")

        #================variables================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        #================title================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=int(screen_width*0.85),height=50)
        #================labelframe================
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Coustomer Details",padx=2,font=("times new roman",12,"bold"))
        Labelframeleft.place(x=5,y=50,width=425,height=490)

        #================labels and entry================

        # custRef
        lbl_cust_ref=Label(Labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(Labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)
        
        # cust name
        cname=Label(Labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(Labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        # mother name
        lblmname=Label(Labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(Labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        # gender combobox
        label_gender=Label(Labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(Labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # postcode
        lblPostCode=Label(Labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(Labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)
        
        # mobilenumber
        lblMobile=Label(Labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(Labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        # email
        lblEmail=Label(Labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(Labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        # nationality
        lblNationality=Label(Labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(Labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Nepalese","American","Indian","British","African","Russian","Korean","Japanese")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        # idproof type combobox
        lblIdProof=Label(Labelframeleft,text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(Labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Citizenship","Driving License","PAN","Voter Card","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # id number
        lblIdNumber=Label(Labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(Labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # address
        lblAddress=Label(Labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(Labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        #================btns================
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_fields,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #================tabel frame & search system================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Deatils & Search System",padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Mobile","Refer No")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=15)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)

        #================Show data Table================

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email",
                                                                   "nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
           try:
             conn = sqlite3.connect('hotel.db')
             cursor = conn.cursor()
             cursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (self.var_ref.get(), self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                            self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                            self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get()))
             conn.commit()
             conn.close()
             self.fetch_data()
             messagebox.showinfo("Success", "Customer added successfully",parent=self.root)
           except Exception as es:
                messagebox.showwarning("Warning",f"Spme thing went wrong:{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for row in rows:
                self.Cust_Details_Table.insert('', END, values=row)
        conn.close()

    def get_cursor(self, event):
        selected_row = self.Cust_Details_Table.focus()  
        data = self.Cust_Details_Table.item(selected_row)  
        row = data['values'] if 'values' in data else None  

        if row:
            self.var_ref.set(row[0])
            self.var_cust_name.set(row[1])
            self.var_mother.set(row[2])
            self.var_gender.set(row[3])
            self.var_post.set(row[4])
            self.var_mobile.set(row[5])
            self.var_email.set(row[6])
            self.var_nationality.set(row[7])
            self.var_id_proof.set(row[8])
            self.var_id_number.set(row[9])
            self.var_address.set(row[10])
    
    def update_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                cursor.execute("""UPDATE customers SET Name=?, Mother=?, Gender=?, Post=?, Mobile=?, Email=?,
                                  Nationality=?, Id_proof=?, Id_number=?, Address=? WHERE Ref=?""", 
                               (self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                               self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                               self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get(), self.var_ref.get()))

                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Customer details updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete_data(self):
        selected_row = self.Cust_Details_Table.focus()  
        data = self.Cust_Details_Table.item(selected_row)  
        row = data['values'] if 'values' in data else None  

        if not row:
            messagebox.showerror("Error", "Please select a customer to delete", parent=self.root)
            return

        ref_id = row[0]  

        delete_data = messagebox.askyesno("Hotel Management System", 
                                      f"Are you sure you want to delete customer {ref_id}?", 
                                      parent=self.root)

        if delete_data:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM customers WHERE Ref=?", (ref_id,))
                conn.commit()
                conn.close()
    
                self.fetch_data() 
                messagebox.showinfo("Success", "Customer deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root)

    def reset_fields(self):
        self.var_ref.set(str(random.randint(1000, 9999)))
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("Male")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("Nepalese")
        self.var_id_proof.set("Citizenship")
        self.var_id_number.set("")
        self.var_address.set("")
    
    def search(self):
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()

        search_by = self.search_var.get()  
        search_value = self.txt_search.get()  

        if search_by == "Mobile":
            cursor.execute("SELECT * FROM customers WHERE mobile=?", (search_value,))
        elif search_by == "Ref":
            cursor.execute("SELECT * FROM customers WHERE ref=?", (search_value,))
        else:
            messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
            return

        rows = cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for row in rows:
                self.Cust_Details_Table.insert('', END, values=row)
        else:
            messagebox.showinfo("Info", "No matching records found", parent=self.root)
    
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
        
 