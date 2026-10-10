# Imports
import hashlib
import tkinter as tk
 
# Definitions
logged_in = False
syntax_check_bool = True
you_have_mail = False
duplicate = False
email_syntax_check = None
found_correct_email = False
BG = "#ffffff"


# Tkinter functions
def email_field_check():
    global signup_email
    signup_email = email_entry.get()
    print(signup_email)
    
    # Checks for corrext xxx@xxx.xxx email format
    email_format_check_len = len(signup_email)
    email_format_check_at = signup_email.find("@")
    email_format_check_dot = signup_email.find(".")

    global email_syntax_check

    if email_format_check_at > 0 and email_format_check_at < email_format_check_dot and email_format_check_len > email_format_check_dot:
        email_syntax_check = True
    else:
        email_syntax_check = False

    # Checks if the account email is duplicate
    global duplicate
    with open("accounts.txt", "r", encoding="utf-8") as account:
        for line in account:
            line = line.strip()
            x = line.split("|")[0]
            if x == signup_email:
                duplicate = True
            else:
                duplicate = False

    if not duplicate and email_syntax_check:
        email_field()
    elif not email_syntax_check:
        signup_screen(error=True)
    elif duplicate:
        signup_screen(duplicate=True)

def email_field():
    wn_signup.destroy()
    
    global wn_signup_password
    wn_signup_password = tk.Tk()

    wn_signup_password.geometry("650x500")
    wn_signup_password.title("Undemail Signup")
    wn_signup_password.config(background="#ffffff")

    password_label = tk.Label(text="Please enter password:", bg=BG)
    password_label.config(font=("Arial", 16, "bold"))
    password_label.place(x=208, y=150)

    global password_entry
    password_entry = tk.Entry(show="*")
    password_entry.place(x=250, y=250)

    password_entry_button = tk.Button(text="Done")
    password_entry_button.place(x=303, y=300)
    password_entry_button.config(command=password_field)

def password_field():
    global signup_password
    signup_password = password_entry.get()
    print(signup_password)

    wn_signup_password.destroy()

    logged_in_wn = tk.Tk()
    logged_in_wn.config(bg="#FFFFFF")
    logged_in_wn.geometry("650x500")

    account_password_hashed = hashlib.sha256(signup_password.encode('utf-8')).hexdigest()

    if duplicate:
        print("Sorry, that email is already taken.")
    elif not duplicate and email_syntax_check:
        with open("accounts.txt", "a", encoding="utf-8") as account:
            account.write(f"{signup_email}|{account_password_hashed}\n")
        print("Account created successfully! Please log in to continue.")

def password_field_login_get():
    global login_password
    login_password = password_entry.get()
    print(login_password) 


    account_password_login_hashed = hashlib.sha256(login_password.encode('utf-8')).hexdigest()

    # Opens account.txt in read mode and compares hashed user password input with the hashed password found in accounts.txt
    with open("accounts.txt", "r", encoding="utf-8") as account:

        # Iterates through each line in accounts.txt to compare it to user's alleged password
        for line in account:
            num_of_lines = len(account.readlines())
            line = line.strip()
            x, y = line.split("|")

            with open("accounts.txt", "r", encoding="utf-8") as account:
                # Iterates through each line in accounts.txt to compare it to user's alleged password
                for line in account:
                    line = line.strip()
                    x, y = line.split("|")
                    if x == login_email and y == account_password_login_hashed:
                        found_correct_email = True

                        break

                if found_correct_email:
                    print("Login successful! Welcome back!")
                    global logged_in
                    global logged_in_as
                    logged_in = True
                    logged_in_as = login_email
                else:
                    print("Incorrect email or password.")         


def password_field_login():
    global login_email
    login_email = email_entry_login.get()
    print(login_email)

    wn_login.destroy()

    global wn_login_password
    wn_login_password = tk.Tk()

    wn_login_password.geometry("650x500")
    wn_login_password.title("Undemail Signup")
    wn_login_password.config(background="#ffffff")

    password_label_login = tk.Label(text="Please enter password:", bg=BG)
    password_label_login.config(font=("Arial", 16, "bold"))
    password_label_login.place(x=213, y=150)

    global password_entry
    password_entry = tk.Entry(show="*")
    password_entry.place(x=250, y=250)

    global password_entry_button_login
    password_entry_button_login = tk.Button(text="Done")
    password_entry_button_login.place(x=303, y=300)
    password_entry_button_login.config(command=password_field_login_get)

# Function that runs when you press login
def login_screen():
    wn.destroy()

    global wn_login
    wn_login = tk.Tk()
    wn_login.config(bg="#FFFFFF")
    wn_login.geometry("650x500")

    email_label_login = tk.Label(text="Please enter email to log in:", bg=BG)
    email_label_login.config(font=("Arial", 16, "bold"))
    email_label_login.place(x=195, y=150)

    global email_entry_login
    email_entry_login = tk.Entry()
    email_entry_login.place(x=250, y=250)

    email_entry_button_login = tk.Button(text="Done")
    email_entry_button_login.place(x=303, y=300)
    email_entry_button_login.config(command=password_field_login)

# Checks if user chose to signup
def signup_screen(error=False, duplicate=False):
    if not error and not duplicate:
        wn.destroy()
        global wn_signup
        wn_signup = tk.Tk()

        wn_signup.geometry("650x500")
        wn_signup.title("Undemail Signup")
        wn_signup.config(background="#ffffff")

        email_label = tk.Label(text="Please enter email to sign up:", bg=BG)
        email_label.config(font=("Arial", 16, "bold"))
        email_label.place(x=180, y=150)

        global email_entry
        email_entry = tk.Entry()
        email_entry.place(x=250, y=250)

        email_entry_button = tk.Button(text="Done")
        email_entry_button.place(x=303, y=300)
        email_entry_button.config(command=email_field_check)

    elif error:
        syntax_error = tk.Label(text="Email must be in xxx@xxx.xxx format.", fg="#ff3333", bg=BG)
        syntax_error.place(x=215, y=350)
    elif duplicate:
        duplicate_error = tk.Label(text="That email already exists!", fg="#ff3333", bg=BG)
        duplicate_error.place(x=250, y=350)
        


if logged_in:
    yorn = input("Would you like to send an email [1] or check inbox [2]? \n[1] [2]")
    if yorn.lower() == "1":
        receiver_email = input("Please input receiver email: ")
        email_subject = input("Please input email subject: ")
        email_body = input("Please input email contents: ")
        syntax_check = receiver_email + email_subject + email_body
        for char in syntax_check:
            if char == "|":
                syntax_check_bool = False
        if syntax_check_bool:
            with open ("mail.txt", "a", encoding="utf-8") as mail:
                mail.write(f"{logged_in_as}|{receiver_email}|{email_subject}|{email_body}")
    elif yorn.lower() == "2":
        with open("mail.txt", "r", encoding="utf-8") as mail:
            for line in mail:
                line = line.strip()
                sender, receiver, subject, body = line.split("|")
                if receiver == logged_in_as:
                    you_have_mail = True
                else:
                    you_have_mail = False
        if you_have_mail:
            print(f"FROM: {sender} \nTO: {receiver} \nSUBJECT: {subject} \nCONTENT: {body}")
        
        elif not you_have_mail:
            print("You have no mail.")

# Tkinter
wn = tk.Tk()

wn.geometry("650x500")
wn.title("Undemail")
wn.config(background="#ffffff")

welcome_text = tk.Label(wn, text="Welcome to undemail!", font=("Arial", 20, "bold"), bg=BG)
welcome_text.place(x=180, y=50)

login_button = tk.Button(text="Login")
login_button.config(command=login_screen)
login_button.place(x=370, y=350)

signup_button = tk.Button(text="Signup")
signup_button.config(command=signup_screen)
signup_button.place(x=200, y=350)

wn.mainloop()