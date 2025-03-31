from utils import fetch_login_data,write_login_data

def issue_fines():
    data = fetch_login_data()

    id = input("Enter the id you wish issue fine on: ")
    amount = input("Enter the fine amount: ")

    for records in data:
        if int(records["id"]) == int(id):
            if not records["fine_due"]:
                records["fine_due"] = int(amount)
            else:
                records["fine_due"] += int(amount)
            print(f"{records["name"]} has been issued a total fine of {records["fine_due"]}")
    
    write_login_data(data)
