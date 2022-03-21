from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip 
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    #password_list = [random.choice(letters,symbols,numbers) for char in range(nr_letters,nr_symbols,nr_numbers)] 
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(0, 2))]
    password_numbers = [choice(numbers) for i in range(randint(1, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)

    # this already copys this to your clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website= website_entry.get()
    email= email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(website) ==0 or len(password) ==0:
        messagebox.showerror(title="Error",message="Please don't leave any feilds empty!")
    else:
        # First try this 
        try:
            with open("data.json","r") as data_file:
            # reading data
                data = json.load(data_file)

        # If file not found 
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                # saving updated data
                json.dump(new_data, data_file,indent=4)

        # If file was found, update it and start writing to it
        else:
            # updating old data with new data
                data.update(new_data)
                with open("data.json","w") as data_file:
                # saving updated data
                    json.dump(data, data_file,indent=4)

        # finally if errors or NO errors this executes
        # this just deletes the website and email entrys
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
def search():
    website = website_entry.get()
            # opening up file
    try :
        with open("data.json","r") as data_file:
                # reading data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found")
    else:
        search = {k:v for k,v in data.items() if website in k}
        if search:
            messagebox.showinfo(title="Search", message=f"These are your credentials \nEmail: {search[website]['email']} \nPassword: {search[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No information available from: {website}")
# -------------------------Search setup--------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
photo = PhotoImage(file="/Users/hectororopesa/Documents/GUI/password-manager-start/logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)


# website Entry --------------------------------
website_entry = Entry(width=20)
website_entry.grid(column=1,row=1)
website_entry.focus()
# website label --------------------------------
website_label = Label(text="Website Here: ")
website_label.grid(column=0,row=1)


# search button --------------------------------
search_button = Button(width=13,text="Search",command= search)
search_button.grid(column=2,row=1)

# Email Address/user name Entry --------------------------------
email_username_entry = Entry(width=38)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0,"Hector556@yelp.com")

# Email Address/user name label --------------------------------
email_username_label = Label(text="Email / Username: ")
email_username_label.grid(column=0,row=2)

# password Entry--------------------------------
password_entry = Entry(width= 20)
password_entry.grid(column=1,row=3)
# password label
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# generate password button --------------------------------
generate_password_butoon = Button(text="Generate Password",command=gen_password)
generate_password_butoon.grid(column=2,row=3)

# Add Button
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()
