from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os
import subprocess

class SignUpApp:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('SIGN-UP')

        # Set window icon
        icon_image = Image.open(r"c:\Users\safal\Downloads\Gemini_Generated_Image_xi5sxvxi5sxvxi5s.png")
        self.icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(False, self.icon_photo)

        # Set background image
        self.login_frame = Frame(self.root)
        self.login_frame.pack(fill='both', expand=True)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        bg_image = Image.open(r"c:\Users\safal\Downloads\background.png")
        bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.login_frame, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create entry fields and buttons
        self.create_widgets()

    def create_entry(self, parent, label_text, placeholder, is_password=False):
        Label(parent, text=label_text, font=("Arial", 12, "bold"), fg="black", bg='white').pack(anchor=W, pady=(10, 0))
    
        entry_frame = Frame(parent, bg="white", highlightbackground="gray", highlightthickness=1)
        entry_frame.pack(fill=X, pady=5)

        entry = Entry(entry_frame, font=("Arial", 12), fg='gray', bd=0)
        entry.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        entry.insert(0, placeholder)
    
        entry.bind("<FocusIn>", lambda event: self.on_focus_in(entry, placeholder))
        entry.bind("<FocusOut>", lambda event: self.on_focus_out(entry, placeholder))

        if is_password:
            entry.config(show='*')
            toggle_button = Button(entry_frame, text='👁‍🗨', bd=0, bg="white", 
                                   command=lambda: self.toggle_password(entry, toggle_button))
            toggle_button.pack(side=RIGHT, padx=5)
    
        return entry  # Return entry object

    def create_widgets(self):
        form_frame = Frame(self.root, bg='white', padx=40, pady=20)
        form_frame.place(relx=0.48, rely=0.2)

        self.email_entry = self.create_entry(form_frame, "Email", "Enter your email")  # Assign email entry
        self.password_entry = self.create_entry(form_frame, "Password", "Enter your password", is_password=True)
        self.confirm_password_entry = self.create_entry(form_frame, "Confirm Password", "Confirm your password", is_password=True)

        # Buttons container
        button_frame = Frame(form_frame, bg="white")
        button_frame.pack(fill=X, pady=20)
        
        Button(button_frame, text="BACK", font=("Arial", 14, "bold"), bg="red", fg='white', width=10, command=self.back_to_login).pack(side=LEFT, padx=5)
        Button(button_frame, text="SUBMIT", font=("Arial", 14, "bold"), command=self.submit, bg="red", fg='white', width=10).pack(side=LEFT, padx=5)

    def on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg='black')

    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='gray')

    def toggle_password(self, entry, button):
        if entry.cget('show') == '*':
            entry.config(show='')
            button.config(text='👁')
        else:
            entry.config(show='*')
            button.config(text='👁‍🗨')

    def submit(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        if email == "" or password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        conn = sqlite3.connect("signup.db")
        cursor = conn.cursor()

        # Check if email already exists
        cursor.execute("SELECT * FROM sign WHERE email=?", (email,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Email already registered! Please log in.")
            conn.close()
            return

        # Insert new user
        cursor.execute("INSERT INTO sign (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Account Created! Now, set up security questions.")
        
        # Redirect to forgot_password.py to set security questions
        self.root.destroy()
        subprocess.run(["python", "forgot_password.py", email])

    def back_to_login(self):
        self.root.destroy()  # Close signup page
        os.system("python login.py")  # Open login page

if __name__ == "__main__":
    root = Tk()
    app = SignUpApp(root)
    root.mainloop()