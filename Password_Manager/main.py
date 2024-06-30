from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    with open("data.txt", "a") as file:
        contents = f"{website} | {username} | {password}\n"
        file.write(contents)
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = my_pass)
canvas.grid(column=1, row=0)

#Labels
website_label = Label()
website_label.config(text="Website: ")
website_label.grid(column=0, row=1)

username_label = Label()
username_label.config(text="Email/Username: ")
username_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password: ")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "itk@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

#Button
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()