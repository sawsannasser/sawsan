import re

def validate_username(username):
    if len(username) == 0:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password should contain at least one special symbol."
    if not re.search(r"\d", password):
        return "Password should have one or more numbers."
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return "Password should have one or more uppercase and lowercase characters."
    return None

def validate_email(email):
    if "@" not in email:
        return "Email should have '@' symbol."
    username, domain = email.split("@")
    if not username.isalnum():
        return "Email should have alphanumeric characters before the '@' symbol."
    if not re.match(r"[a-zA-Z0-9]+\.[a-zA-Z]+", domain):
        return "After the '@' symbol, email should have letters with a '.' character in between."
    return None

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")
    
    username_error = validate_username(username)
    if username_error:
        print(username_error)
    
    password_error = validate_password(password)
    if password_error:
        print(password_error)
    
    email_error = validate_email(email)
    if email_error:
        print(email_error)
    
    if not username_error and not password_error and not email_error:
        print("All inputs are valid.")
    else:
        print("There are some errors in the inputs.")

if __name__ == "__main__":
    main()
