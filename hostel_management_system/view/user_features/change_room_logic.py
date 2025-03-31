from utils import fetch_change_room_data,write_change_room_data,fetch_login_data

def change_room(id):
    data = fetch_login_data()
    room_change_data = fetch_change_room_data()
    for records in data:
        if id == records["id"]:
            if not records["allocated_room"]:
                if id not in room_change_data:
                    room_change_data.append(id)
                    print("your request has been registered")
                else:
                    print("your request is under process")
            else:
                print("no room has been alloted to you")
                print("please apply for one before changing it")

    write_change_room_data(room_change_data)