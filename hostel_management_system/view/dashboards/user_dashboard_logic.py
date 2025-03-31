from utils import fetch_login_data
from controllers.user_controller_logic import user_controller
import time

def fetch_user_data(id):
    data = fetch_login_data()
    for records in data:
        if id == records["id"]:
            return records

def user_dashboard(id):
    print("-------------------------------------------------------------")
    print(f"Welcome to the user dashboard")
    print("-------------------------------------------------------------")

    student_data_dict = fetch_user_data(id)
    print(f"room status: {student_data_dict["room_status"]}")
    print(f"allocated room: {student_data_dict["allocated_room"]}")
    print(f"fine due: {student_data_dict["fine_due"]}")
    print(f"wallet balance: {student_data_dict["wallet"]}")
    print("-------------------------------------------------------------")
    time.sleep(2)

    user_controller(id)
