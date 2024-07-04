from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
        
    password_list = []
    
    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = letter_list + symbol_list + numbers_list
    
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, password)
    
    pyperclip.copy(password)#puts new generated password in users clipboard 
    
def find_password():
    website = website_entry.get()
    email = username_entry.get()
    
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    
    
    for key, value in data.items():
        
        if website == key:
            new_password = value.get("password")
            if new_password:
                messagebox.showinfo(title=key, message=f"Email: {email}  \nPassword: {new_password}")
            
            else:
                messagebox.showinfo(title="Oops", message="No details for the website exists.")
                    
            

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You have entered the following details: \nEmail: {username} \nPassword: {password} \nAre you sure it's ready to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

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
website_entry = Entry(width=17)
website_entry.grid(column=1, row=1)
website_entry.focus()


username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "itk@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

#Button
password_button = Button(text="Generate Password", command=generate_password, width=14)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()