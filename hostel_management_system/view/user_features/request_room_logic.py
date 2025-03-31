from utils import fetch_wait_list_data,write_wait_list_data,fetch_login_data,write_login_data

def request_room(id):
    data = fetch_wait_list_data()
    data.append(id)
    write_wait_list_data(data)

    data_two = fetch_login_data()
    for records in data_two:
        if records["id"] == id:
            records["room_status"] = "a room has been requested"
            print("Your request has been registered")
            print("please pay the fees to complete your application")
            print("")
            print(f"room status: {records["room_status"]}")
            print(f"allocated room: {records["allocated_room"]}")
            print("")
    write_login_data(data_two)
