# Imports
import hashlib
import tkinter as tk
 
# Definitions
logged_in = False
syntax_check_bool = True
you_have_mail = False
duplicate = False
email_syntax_check = None

# Tkinter functions
def email_field():
    email_entry.get()

# Checks if user chose to login
def login():
    global logged_in_as
    global logged_in

    # Hashes the password before checking it against the hashed accounts.txt
    account_password_login_hashed = hashlib.sha256(account_password_login.encode('utf-8')).hexdigest()

    # Opens account.txt in read mode and compares hashed user password input with the hashed password found in accounts.txt
    with open("accounts.txt", "r", encoding="utf-8") as account:
        # Iterates through each line in accounts.txt to compare it to user's alleged password
        for line in account:
            line = line.strip()
            x, y = line.split("|")
            if x == account_email_login and y == account_password_login_hashed:
                print("Login successful! Welcome back!")
                logged_in = True
                logged_in_as = account_email_login
                break
            else:
                print("Password or email incorrect.")

# Checks if user chose to signup
def signup():
    wn.destroy()
    wn_signup = tk.Tk()

    wn_signup.geometry("650x500")
    wn_signup.title("Undemail Signup")
    wn_signup.config(background="#ffffff")
    
    global email_entry
    email_entry = tk.Entry()
    email_entry.pack()

    email_entry_button = tk.Button(text="Done")
    email_entry_button.pack()
    account_password_hashed = hashlib.sha256(account_password.encode('utf-8')).hexdigest()
    # Checks for corrext xxx@xxx.xxx email format
    email_format_check_len = len(account_email)
    email_format_check_at = account_email.find("@")
    email_format_check_dot = account_email.find(".")
    print(email_format_check_at, email_format_check_dot,email_format_check_len)
    if email_format_check_at > 0 and email_format_check_at < email_format_check_dot and email_format_check_len > email_format_check_dot:
        email_syntax_check = True
    else:
        email_syntax_check = False

    # Checks if the account email is duplicate
    with open("accounts.txt", "r", encoding="utf-8") as account:
        for line in account:
            line = line.strip()
            x = line.split("|")[0]
            if x == account_email:
                duplicate = True
    if duplicate:
        print("Sorry, that email is already taken.")
    elif not duplicate and email_syntax_check:
        with open("accounts.txt", "a", encoding="utf-8") as account:
            account.write(f"{account_email}|{account_password_hashed}\n")
        print("Account created successfully! Please log in to continue.")

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

welcome_text = tk.Label(wn, text="Welcome to undemail!", font=("Arial", 20, "bold"))
welcome_text.place(x=180, y=50)

login_button = tk.Button(text="Login")
login_button.config(command=login)
login_button.place(x=370, y=350)

signup_button = tk.Button(text="Signup")
signup_button.config(command=signup)
signup_button.place(x=200, y=350)

wn.mainloop()