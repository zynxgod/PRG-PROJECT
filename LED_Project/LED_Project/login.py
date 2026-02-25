from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class SunsetHotelLogin:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('Sunset Hotel Management System')
        
        icon_image = Image.open(r"c:\Users\safal\Downloads\logo (2).png")
        self.icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(False, self.icon_photo)
        
        self.setup_database()
        self.setup_ui()
    
    def setup_database(self):
        conn = sqlite3.connect("signup.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sign (
                          email TEXT PRIMARY KEY,
                          password TEXT NOT NULL)''')
        conn.commit()
        conn.close()
    
    def setup_ui(self):
        self.login_frame = Frame(self.root)
        self.login_frame.pack(fill='both', expand=True)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        bg_image = Image.open(r"c:\Users\safal\Downloads\background.png")
        bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.login_frame, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.create_login_fields()
    
    def add_placeholder(self, entry, text, is_password=False):
        def on_entry_click(event):
            if entry.get() == text:
                entry.delete(0, END)
                entry.config(fg='black', show="*" if is_password else "")

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, text)
                entry.config(fg='gray', show="" if not is_password else "*")
        
        entry.insert(0, text)
        entry.config(fg='gray', show="" if not is_password else "*")
        entry.bind("<FocusIn>", on_entry_click)
        entry.bind("<FocusOut>", on_focus_out)
    
    def create_login_fields(self):
        frame = Frame(self.login_frame, bg='white', padx=40, pady=40)
        frame.place(relx=0.65, rely=0.4, anchor=CENTER)

        Label(frame, text="Login", font=("Arial", 22, 'bold'), bg='white').pack(pady=10)
        
        self.user = Entry(frame, font=("Arial", 14), bd=0, highlightthickness=1, highlightbackground="gray")
        self.user.pack(pady=5, ipadx=5, ipady=5, fill=X)
        self.add_placeholder(self.user, "Enter your email")
        
        self.code = Entry(frame, font=("Arial", 14), bd=0, highlightthickness=1, highlightbackground="gray", show="*")
        self.code.pack(pady=5, ipadx=5, ipady=5, fill=X)
        self.add_placeholder(self.code, "Enter your password", is_password=True)
        
        self.show_password_var = BooleanVar(value=False)
        Checkbutton(frame, text="Show Password", variable=self.show_password_var, command=self.toggle_password, bg='white').pack(anchor='w', pady=5)
        
        Button(frame, text="Forgot Password?", fg="blue", cursor="hand2", font=("Arial", 10, "underline"), bd=0, bg='white', command=self.forgot_password).pack(pady=5)
        Button(frame, text="Sign Up", fg="blue", cursor="hand2", font=("Arial", 10, "underline"), bd=0, bg='white', command=self.signup).pack(pady=5)
        
        Button(frame, text="SUBMIT", command=self.signin, font=("Arial", 14, 'bold'), bg="red", fg='white', width=15, height=1).pack(pady=10)
    
    def toggle_password(self):
        if self.show_password_var.get():
            self.code.config(show="")
        else:
            if self.code.get() != "Enter your password":
                self.code.config(show="*")
    
    def forgot_password(self):
        messagebox.showinfo("Password Reset", "Redirecting to password reset...")
    
    def signup(self):
        self.root.destroy()
        os.system("python signup.py")
    
    def signin(self):
        username = self.user.get().strip()
        password = self.code.get().strip()
        
        if not username or not password or username == "Enter your email" or password == "Enter your password":
            messagebox.showerror("Error", "Please input all the details.")
        else:
            try:
                conn = sqlite3.connect("signup.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM sign WHERE email=? AND password=?", (username, password))
                if cursor.fetchone():
                    conn.close()
                    messagebox.showinfo("Success", "Login successful! Exiting application.")
                    self.root.destroy()
                else:
                    messagebox.showerror("Error", "Invalid information")
                    conn.close()
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
    
    def on_closing(self):
        if messagebox.askyesno("Exit", "Are you sure you want to close the window?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = SunsetHotelLogin(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
