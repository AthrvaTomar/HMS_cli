from utils import fetch_change_room_data, fetch_login_data, fetch_room_data
from utils import write_change_room_data, write_login_data, write_room_data

def get_student_info(id,data):
    for records in data:
        if id == records["id"]:
            return records

def is_room_empty(room_data):
    count = 0
    for room in room_data:
        if room["student_one"] != None and room["student_two"] != None:
            count+=1
    if count != len(room_data):
        return True
    else:
        return False

def update_data(new_records,data):
    for records in data:
        if records["id"] == new_records["id"]:
            records = new_records
    write_login_data(data)

def allocate_room(records,old_room_no,room_data):
    if is_room_empty(room_data):
        for room in room_data:
            if room["room_no"] != old_room_no:
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
                temp_tuple = (False,records)
                return temp_tuple
        write_room_data(room_data)
        temp_tuple = (True,records)
        return temp_tuple
    else:
        temp_tuple = (False,records)
        return temp_tuple

def deallocate_current_room(old_room_no,name,room_data):
    for room in room_data:
        if room["room_no"] == old_room_no:
            if room["student_one"] == name:
                room["student_one"] = None
            elif room["student_two"] == name:
                room["student_two"] = None
    write_room_data(room_data)

def change_room_request():
    data = fetch_login_data()
    room_data = fetch_room_data()
    change_room_data = fetch_change_room_data()
    Processed_id = []

    for id in change_room_data:
        records = get_student_info(id,data)
        old_room_no = records["allocated_room"]
        name = records["name"]
        print("hello",old_room_no)
        flag_to_check_allocation,new_records = allocate_room(records,old_room_no,room_data)
        update_data(new_records,data)
        deallocate_current_room(old_room_no,name,room_data)

        if not flag_to_check_allocation:
            print("room are full")
            print("request rejected")
            print("apply again after sometime")
            print(f"your room is {new_records["allocated_room"]}")
            Processed_id.append(id)
        else:
            print("room changed")
            print(f"your room is {new_records["allocated_room"]}")
            Processed_id.append(id)

    print(change_room_data)
    print(Processed_id)
    
    for id in Processed_id:
        print(id)
        change_room_data.remove(id) 

    write_change_room_data(change_room_data)  
