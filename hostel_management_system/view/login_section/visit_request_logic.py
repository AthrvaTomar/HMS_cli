from utils import fetch_login_data
from utils import fetch_visitor_data,write_visitor_data

def check_name_email(name,email):
    if len(name) <3:
        print("lenght of name should be more then 3")
        visit_request()
    if "@" not in email or "." not in email:
        print("email should have atleast 1 @ and .")
        visit_request()

def check_student(student):
    data = fetch_login_data()
    flag = False
    for records in data:
        if student == records["name"]:
            flag = True
    if not flag:
        print("student not found")
        visit_request()

def check_date(date):
    if not (0<int(date[0:2])<32 and 0<int(date[3:5])<13 and 2024<int(date[6:10])):
        print("incorrect date or format")
        visit_request()

def check_time(time):
    if not (0<=int(time[0:2])<25 and 0<=int(time[3:5])<60):
        print("incorrect time or format")
        visit_request()

def visit_request():
    print("-------------------------------------------------------------")
    print("welcome to visit request page")
    print("-------------------------------------------------------------")
    print("")
    print("Enter both name and email as 0 if you wish to return")
    name = input("enter your name: ")
    email = input("enter your email: ")

    if name == "0" and email == "0":
        print("")
        return

    try:
        check_name_email(name,email)
        student_visiting = input("enter student's name you are visisting: ")
        check_student(student_visiting)
        arrival_date = input("enter arrival date (dd/mm/yyyy): ")
        check_date(arrival_date)
        arrival_time = input("enter arrival time (in 24hr clock - HH:MM): ")
        check_time(arrival_time)
    except:
        print("")
        print("invalid input")
        visit_request()

    data = fetch_visitor_data()
    if data != []:
        id = int(data[-1]["id"]) + 1
    else:
        id = 1 
    new_request = {"id": id,"name":name,"email":email,"student_visiting":student_visiting,
                   "arrival_date":arrival_date,"arrival_time":arrival_time}
    
    slot_count = 0
    for records in data:
        # check the slot is not booked by more then 5 people
        if arrival_date in records["arrival_date"] and arrival_time in records["arrival_time"]:
            slot_count+=1
    if slot_count > 5 :
        print("Slot full try different time")
        visit_request()
    else:
        data.append(new_request)
        write_visitor_data(data)
        print("slot book")
        print(f"{slot_count} people have booked same slot as you")
        print("-------------------------------------------------------------")
