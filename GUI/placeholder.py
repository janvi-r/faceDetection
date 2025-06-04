# import customtkinter
# import shelve
# # import student as s

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

# root = customtkinter.CTk()
# root.geometry("500x250")

# def register():
#     user_name = entry1.get()
#     # # Open shelf and save the name
#     # with shelve.open('studentInfo.db') as db:
#     #     # Save the user name
#     #     db[user_name] = s.Student(user_name, None, None)
#     #     print(f"Saved {user_name} to database.")
#     # db.close()

# def login():
#     print("Placeholder for login functionality")


# frame = customtkinter.CTkFrame(master = root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)

# label = customtkinter.CTkLabel(master=frame, text="Registration", font=("Arial", 24)) 

# label.pack(pady=12, padx=10)

# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Your Name")
# entry1.pack(pady=12, padx=10)
# # entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
# # entry2.pack(pady=12, padx=10)

# button = customtkinter.CTkButton(master=frame, text="Next", command=register)
# button.pack(pady=12, padx=10)

# checkbox = customtkinter.CTkCheckBox(master=frame, text="Already Have an Account? Login In", command=login)
# checkbox.pack(pady=12, padx=10)
# root.mainloop()