from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sqlite3

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(screen_width*0.85)}x{int(screen_height*0.78)}+198+170")

        # ================ Title ================
        lbl_title = Label(self.root, text="ROOM ADDING DEPARTMENT", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=int(screen_width*0.85),height=50)

        
        # ================ Label Frame ================
        Labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", padx=2, font=("times new roman", 12, "bold"))
        Labelframeleft.place(x=5, y=50, width=425, height=350)

        # Floor Details
        lbl_floor = Label(Labelframeleft, text="Floor", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)
        self.var_floor = StringVar()
        enty_floor = ttk.Entry(Labelframeleft, textvariable=self.var_floor, font=("arial", 13, "bold"), width=20)
        enty_floor.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_RoomNo = Label(Labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)
        self.var_roomno = StringVar()
        enty_RoomNo = ttk.Entry(Labelframeleft, textvariable=self.var_roomno, font=("arial", 13, "bold"), width=20)
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(Labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)
        self.var_roomtype = StringVar()
        combo_RoomType = ttk.Combobox(Labelframeleft, textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=18, state="readonly")
        combo_RoomType["value"] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=2, column=1, sticky=W)

        # Buttons
        btn_frame = Frame(Labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # ================ Table Frame ================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", padx=2, font=("times new roman", 12, "bold"))
        Table_Frame.place(x=435, y=50, width=860, height=490)

        # Search By
        lblSearchBy = Label(Table_Frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)
        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=18, state="readonly")
        combo_Search["value"] = ("Floor", "RoomNo")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=18)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show Data Table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=("floor", "roomno", "roomtype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO room_details (floor, roomno, roomtype) VALUES (?, ?, ?)",
                               (self.var_floor.get(), self.var_roomno.get(), self.var_roomtype.get()))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = sqlite3.connect('hotel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM room_details")
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
            self.var_floor.set(row[0])
            self.var_roomno.set(row[1])
            self.var_roomtype.set(row[2])

    def update_data(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please select a room to update", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE room_details SET floor=?, roomno=?, roomtype=? WHERE roomno=?",
                               (self.var_floor.get(), self.var_roomno.get(), self.var_roomtype.get(), self.var_roomno.get()))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error", "Please select a room to delete", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM room_details WHERE roomno=?", (self.var_roomno.get(),))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("Single")

    def search_data(self):
        if self.search_var.get() == "" or self.txt_search.get() == "":
            messagebox.showerror("Error", "Please select a search option and enter a value", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('hotel.db')
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM room_details WHERE {self.search_var.get().lower()}=?", (self.txt_search.get(),))
                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.room_table.delete(*self.room_table.get_children())
                    for row in rows:
                        self.room_table.insert('', END, values=row)
                else:
                    messagebox.showinfo("Info", "No matching records found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop() 