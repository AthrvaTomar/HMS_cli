from utils import fetch_wait_list_data,fetch_login_data,fetch_room_data
from utils import write_room_data,write_login_data,write_wait_list_data

def get_occupied_room_count(data):
    count = 0
    for records in data:
        if records["student_one"] and records["student_two"]:
            count+=1
    return count


def get_name_by_id(id,data):
    for records in data:
        if id == records["id"]:
            temp_tuple = (records["id"],records["name"])
            return temp_tuple


def assign_room(id,wait_list_data,room_data,records):
    for room in room_data:
        if not room["student_one"]:
            room["student_one"] = records["name"]
            records["room_status"] = "room allocated"
            records["allocated_room"] = room["room_no"]
            print(f"{records["name"]} has been allocated {room["room_no"]}")
            return id
        elif not room["student_two"]:
            room["student_two"] = records["name"]
            records["room_status"] = "room allocated"
            records["allocated_room"] = room["room_no"]
            print(f"{records["name"]} has been allocated {room["room_no"]}")
            return id


def check_and_assign_rooms(data,wait_list_data):
    room_data = fetch_room_data()
    count = get_occupied_room_count(room_data)
    if count == len(room_data):
        print("rooms are full, assign room next time")
    else:
        processed_id = []
        for id in wait_list_data:
            records = [records for records in data if id == records['id']]
            records = records[0]
            returned_id = assign_room(id,wait_list_data,room_data,records)
            processed_id.append(returned_id)
        for id in processed_id:
            wait_list_data.remove(id)

        write_login_data(data)
        write_room_data(room_data)
        write_wait_list_data(wait_list_data)
        

def check_wait_list():
    data = fetch_login_data()
    wait_list_data = fetch_wait_list_data()

    for id in wait_list_data:
        student_id,name = get_name_by_id(id,data)
        print(student_id,name)

    process = input("would you like to provide them rooms (y/n): ")
    if process in "yY":
        check_and_assign_rooms(data,wait_list_data)
    else:
        print("Ok, maybe next time")
        print("")
