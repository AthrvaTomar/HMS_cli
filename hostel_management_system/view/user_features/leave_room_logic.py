from utils import fetch_login_data,write_login_data,fetch_room_data,write_room_data
from .pay_fine_logic import pay_fine

def leave_room(id):
    data = fetch_login_data()
    room_data = fetch_room_data()
    for records in data:
        if id == records["id"]:
            print(f"starting leave room process for {records["name"]}")
            print(f"checking for any due fines")
            if records["fine_due"]:
                pay_fine(id)
                print("fine payed")
                records["room_status"] = "room vacated"
                for room in room_data:
                    if room["student_one"] == records["name"] and room["room_no"] == records["allocated_room"]:
                        room["student_one"] = None
                    if room["student_two"] == records["name"] and room["room_no"] == records["allocated_room"]:
                        room["student_two"] = None
                records["allocated_room"] = None
            else:
                print("No fine due")
                records["room_status"] = "room vacated"
                for room in room_data:
                    if room["student_one"] == records["name"]:
                        room["student_one"] = None
                    if room["student_two"] == records["name"]:
                        room["student_two"] = None
                records["allocated_room"] = None

    write_login_data(data)
    write_room_data(room_data)
