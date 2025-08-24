from faceDetection import *
import customtkinter
from dataset import create

class Registration:
    def __init__(self, master):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.master = master
        self.master.title("Registration")
        self.master.geometry("500x250")

        self.frame = customtkinter.CTkFrame(master=self.master)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Registration", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter Your Name")
        self.entry1.pack(pady=12, padx=10)

        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Already Have an Account? Login In", command=self.login)
        self.checkbox.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=self.frame, text="Next", command=self.register)
        self.button.pack(pady=12, padx=10)

    def register(self):
        user_name = self.entry1.get()
        # Save to database or perform registration logic here
        print(f"Registered user: {user_name}")
        create(user_name)

    def login(self):
        print("Placeholder for login functionality")
        everything()
