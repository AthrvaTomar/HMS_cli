from utils import fetch_login_data,fetch_room_data

def search():
    data = fetch_login_data()
    room_data = fetch_room_data()
    choice = input("do you want to search by - \n 1)student name \n 2)room number \n")
    if int(choice) == 1:
        name = input("Enter the student's name: ")
        for records in data:
            if records["name"] == name:
                print(f"\nid: {records["id"]} \nname: {records["name"]} \nemail: {records["email"]}")
                print(f"age: {records["age"]} \nroom status: {records["room_status"]}")
                print(f"allocated room: {records["allocated_room"]} \ndue fines: {records["fine_due"]} \n")
    elif int(choice) == 2:
        room_no = input("Enter the room number: ")
        for room in room_data:
            if int(room["room_no"]) == int(room_no):
                print(f"""\n{room["student_one"]} and {room["student_two"]} 
                      live in room number: {room["room_no"]}\n""")
