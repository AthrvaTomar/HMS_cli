from utils import fetch_login_data,write_login_data
from .login_logic import login

def check_credentials(name,email,password):
    if len(name)<3 or len(email)<8 or len(password)<8:
        print("enter valid name,email,password")
        register()
    if "@" not in email or "." not in email:
        print("email should have atleast 1 @ and .")
        register()
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True

    if not has_upper:
        print("Password must contain at least one uppercase letter.")
        register()

    if not has_lower:
        print("Password must contain at least one lowercase letter.")
        register()

    if not has_digit:
        print("Password must contain at least one digit.")
        register()
    

def register():
    print("-------------------------------------------------------------")
    print("welcome to registration page")
    print("-------------------------------------------------------------")
    print("")
    print("Enter both name and email as 0 if you wish to return")
    name = input("enter your name: ")
    email = input("enter your email: ")

    if name == "0" and email == "0":
        print("")
        return
    
    password = input("enter your password: ")
    try:
        age = int(input("enter your age: "))
    except Exception as e:
        print(e)
        register()

    check_credentials(name,email,password)

    data = fetch_login_data()
    if data != []:
        id = int(data[-1]["id"]) + 1
    else:
        id = 1 
    new_user = {"id":id,"name":name,"email":email,"password":password,"age":age,
                "room_status":None,"allocated_room":None,"fine_due":None,"wallet":None}

    all_good_flag = True
    for records in data:
        if email in records["email"]:
            all_good_flag = False
    
    if all_good_flag:
        data.append(new_user)
        write_login_data(data)
        print("you have been registered, please login")
        print("-------------------------------------------------------------")
        login()
