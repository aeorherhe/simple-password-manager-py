import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = 'white'
BLACK = 'black'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    user_password = password_entry.get()

    new_data = {website: {'email': email, 'password': user_password}}

    if len(website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Error", message="Please enter all values")
    else:
        try:
            with open('data.json', 'r') as pass_saved:
                prev_data = json.load(pass_saved)
        except FileNotFoundError:
            with open('data.json', 'w') as pass_saved:
                json.dump(new_data, pass_saved, indent=4)
        else:
            # update previous data in database
            prev_data.update(new_data)

            # re-open file and write the update file to save
            with open('data.json', 'w') as pass_saved:
                json.dump(prev_data, pass_saved, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_db():
    website = website_entry.get()
    try:
        with open('data.json') as pass_saved:
            data_db = json.load(pass_saved)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No password found')
    else:
        if website in data_db:
            result = data_db[website]
            # display search result to user
            messagebox.showinfo(title=website, message=f"Email: {result['email']}\nPassword: {result['password']}")
        else:
            messagebox.showinfo(title='Error', message=f"No details found for {website}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(width=200, height=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

gen_btn = Button(text="Generate Password", command=gen_password, width=15)
gen_btn.grid(column=2, row=3)

add_btn = Button(text="add", width=35, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text='Search', width=15, command=search_db)
search_btn.grid(column=2, row=1)

# ------------------ Inputs ----------------- #

website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'example@test.com')

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)


window.mainloop()
