from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom 

class HotelManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")

        # Get Screen Dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM",
                          font=("times new roman", max(18, int(screen_width * 0.015)), "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=int(screen_height * 0.12), width=screen_width, height=int(screen_height * 0.05))

        # ================= Main Frame =================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=int(screen_height * 0.17), width=screen_width, height=int(screen_height * 0.8))

        # ================= Menu =================
        lbl_menu = Label(main_frame, text="MENU",
                         font=("times new roman", max(14, int(screen_width * 0.01)), "bold"),
                         bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=int(screen_width * 0.15), height=int(screen_height * 0.05))

        # ================= Button Frame =================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=int(screen_height * 0.05), width=int(screen_width * 0.15), height=int(screen_height * 0.20))

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        room_btn.grid(row=1,column=0)

        details_btn=Button(btn_frame,text="DETAILS",command=self.detailrooms,width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        details_btn.grid(row=2,column=0)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=16,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        logout_btn.grid(row=3,column=0)

       
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def detailrooms(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def logout(self):
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    object = HotelManagementSystem(root)
    root.mainloop()
