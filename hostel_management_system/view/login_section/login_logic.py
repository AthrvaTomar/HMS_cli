from utils import fetch_login_data
# from view import user_dashboard, warden_dashboard
# here we are using the below method of importing to avoid importing partially initialized module
# as if we import it above way it trys to import files that have still not been initialized
from ..dashboards.user_dashboard_logic import user_dashboard
from ..dashboards.warden_dashboard_logic import warden_dashboard

def check_user_email_pass(email:str,password:str)->bool:
    data = fetch_login_data()
    for records in data:
        if email == records["email"] and password == records["password"]:
            return True
    return False

def get_user_id(email:str,password:str)->int:
    data = fetch_login_data()
    for records in data:
        if email == records["email"] and password == records["password"]:
            return int(records["id"])

def login():
    print("-------------------------------------------------------------")
    print("Welcome to login page")
    print("-------------------------------------------------------------")
    print("")
    print("Enter both email and password as 0 if you wish to return")
    email = input("Enter email :")
    password = input("Enter password :")
    print("-------------------------------------------------------------")
    print("")
    if email == "0" and password == "0":
        return

    flag_one = check_user_email_pass(email,password)
    if not flag_one:
        print("Enter valid email or password")
        login()
    else:
        if email == "warden@gmail.com":
            warden_dashboard()
        else:
            print("Correct id and password")
            print("-------------------------------------------------------------")
            id = get_user_id(email,password)
            user_dashboard(id)

