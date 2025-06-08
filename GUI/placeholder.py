import tkinter as tk
import customtkinter
import sys
import os

# Add the Registration folder to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
registration_path = os.path.join(current_dir, '..', 'Registration')
registration_path = os.path.abspath(registration_path)  # resolve full path
print("Adding to sys.path:", registration_path)
sys.path.append(registration_path)


#from faceDetection import create
#from faceDetection import everything
from Authentication.mainMultiImg import self.everything

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
       # create(user_name)

    def login(self):
        print("Placeholder for login functionality")
        self.everything()


#Create main window and run
if __name__ == "__main__":
    root = tk.Tk()
    app = Registration(root)
    root.mainloop()# import customtkinter
# import sys
# import os

# # Add the Registration folder to sys.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# registration_path = os.path.join(current_dir, '..', 'Registration')
# registration_path = os.path.abspath(registration_path)  # resolve full path
# print("Adding to sys.path:", registration_path)
# sys.path.append(registration_path)


# from faceDetection import create
# from faceDetection import everything

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")



# def main():

#     root = customtkinter.CTk()
#     root.geometry("500x250")



#     frame = customtkinter.CTkFrame(master = root)
#     frame.pack(pady=20, padx=60, fill="both", expand=True)

#     label = customtkinter.CTkLabel(master=frame, text="Registration", font=("Arial", 24)) 

#     label.pack(pady=12, padx=10)

#     entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Your Name")
#     entry1.pack(pady=12, padx=10)
#     # entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
#     # entry2.pack(pady=12, padx=10)


#     button = customtkinter.CTkButton(master=frame, text="Next", command=run_face_detection)
#     button.pack(pady=12, padx=10)

#     checkbox = customtkinter.CTkCheckBox(master=frame, text="Already Have an Account? Login In", command=login)
#     checkbox.pack(pady=12, padx=10)
#     root.mainloop()

#     def run_face_detection():
#         user_name = entry1.get()
#         root.destroy()
#         create(user_name)

# if __name__ == "__main__":
#     main()

# # def register():
# #     user_name = entry1.get()

# def login():
#     print("Placeholder for login functionality")
#     everything()