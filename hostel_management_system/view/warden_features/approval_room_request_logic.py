from utils import fetch_login_data,fetch_room_data,write_login_data,write_room_data
from utils import fetch_wait_list_data,write_wait_list_data

def approval_room_request():
    data = fetch_login_data()
    room_data = fetch_room_data()
    wait_list_data = fetch_wait_list_data()

    for records in data:
        if records["email"] == "warden@gmail.com":
             continue
        if records["room_status"] == "fees paid":
                for room in room_data:
                    if not room["student_one"]:
                        room["student_one"] = records["name"]
                        records["room_status"] = "room allocated"
                        records["allocated_room"] = room["room_no"]
                        print(f"{records["name"]} has been allocated {room["room_no"]}")
                        break
                    elif not room["student_two"]:
                        room["student_two"] = records["name"]
                        records["room_status"] = "room allocated"
                        records["allocated_room"] = room["room_no"]
                        print(f"{records["name"]} has been allocated {room["room_no"]}")
                        break
                else:
                    wait_list_data.append(records["id"])
                    print("room are full so you have been added to waiting list")
        else:
            print(f"{records["name"]} has not paid fees")

    write_login_data(data)
    write_room_data(room_data)
    write_wait_list_data(wait_list_data)
