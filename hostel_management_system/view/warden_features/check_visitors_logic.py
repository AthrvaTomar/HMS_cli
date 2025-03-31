from utils import fetch_visitor_data

def check_visitors():
    data = fetch_visitor_data()
    for records in data:
        print("")
        print(records["id"])
        print(records["name"])
        print(records["email"])
        print(records["student_visiting"])
        print(records["arrival_date"])
        print(records["arrival_time"])
        print("")
