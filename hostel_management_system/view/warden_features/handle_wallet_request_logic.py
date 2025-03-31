from utils import fetch_add_to_wallet_data,write_add_to_wallet_data
from utils import fetch_login_data,write_login_data

def handle_wallet_request():
    data = fetch_login_data()
    add_to_wallet_data = fetch_add_to_wallet_data()

    if len(add_to_wallet_data) == 0:
        print("No add to wallet requests")
        print("")
        return

    processed = []

    for records in data:
        for val in add_to_wallet_data:
            if records["id"] == val["id"]:
                print(f"{val["id"]} is requesting to add {val["add_to_wallet_amount"]}")
                flag = True
                while flag:
                    choice = input("Enter Y/y to approve and N/n to reject: ")

                    if choice in "yY":
                        processed.append(val)
                        if not records["wallet"]:
                            records["wallet"] = int(val["add_to_wallet_amount"])
                        else:
                            records["wallet"] += int(val["add_to_wallet_amount"])
                        print(f"{records["id"]} now has balance {records["wallet"]}")
                        flag = False
                    elif choice in "nN":
                        processed.append(val)
                        print(f"{records["id"]} has balance {records["wallet"]}")
                        flag = False
                    else:
                        print("Enter either Y/y or N/n")

                write_login_data(data)

    for records in processed:
        add_to_wallet_data.remove(records)

    write_add_to_wallet_data(add_to_wallet_data)
