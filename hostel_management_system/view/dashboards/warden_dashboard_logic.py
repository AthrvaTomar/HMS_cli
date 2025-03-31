from utils import fetch_login_data,fetch_room_data,fetch_wait_list_data
from utils import fetch_change_room_data,fetch_issue_data
from controllers.warden_contoller_logic import warden_contoller
import time

def get_student_count(data):
    count = len(data)-1
    return count

def get_room_count(data):
    count = len(data)
    return count

def get_occupied_room_count(data):
    count = 0
    for records in data:
        if records["student_one"]:
            count+=1
    return count

def get_wait_list_count(data):
    count = len(data)
    return count

def get_student_fine_count(data):
    count = 0
    for records in data:
        if records["fine_due"]:
            count+=1
    return count

def total_fine(data):
    count = 0
    for records in data:
        if records["fine_due"]:
            count += int(records["fine_due"])
    return count

def get_issue_count(data):
    count = len(data)
    return count

def get_change_room_count(data):
    count = len(data)
    return count

def warden_dashboard():
    print("\n warden dashboard \n")

    data = fetch_login_data()
    room_data = fetch_room_data()
    wait_list_data = fetch_wait_list_data()
    issue_data = fetch_issue_data()
    change_room_data = fetch_change_room_data()

    student_count = get_student_count(data)
    room_count = get_room_count(room_data)
    room_occupied = get_occupied_room_count(room_data)
    wait_list_len = get_wait_list_count(wait_list_data)
    fine_count = get_student_fine_count(data)
    fine_total = total_fine(data)
    issue_raised = get_issue_count(issue_data)
    change_room_requests = get_change_room_count(change_room_data)

    print(f"student count = {student_count}")
    print(f"room count  = {room_count}")
    print(f"rooms occupied = {room_occupied}")
    print(f"wait list count = {wait_list_len}")
    print(f"fine count = {fine_count}")
    print(f"total fine = {fine_total}")
    print(f"issues raised = {issue_raised}")
    print(f"change room requests = {change_room_requests}")
    time.sleep(2)

    warden_contoller()
