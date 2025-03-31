from utils import fetch_login_data,write_login_data
from .add_to_wallet_logic import add_to_wallet

def pay_fees(id):
    data = fetch_login_data()
    for records in data:
        if id == records["id"]:
            if records["room_status"] == "a room has been requested":
                print(f"paying fees of {records["name"]}")
                surity = input("are you sure you wish to pay the fees (i.e. 2500): (Y/N)")
                if surity in "Yy":
                    if records["wallet"]:
                        if records["wallet"]>2500:
                            records["room_status"] = "fees paid"
                            records["wallet"]-=2500
                            print("the fees has been paid")
                            print("")
                            print(f"room status: {records["room_status"]}")
                            print(f"allocated room: {records["allocated_room"]}")
                            print("A room will be provided to you soon")
                            print("")
                        else:
                            print("")
                            print("insufficient balance, add amount to it")
                            print("")
                            add_to_wallet(id)
                    else:
                        print("")
                        print("your wallet is empty, add amount to it")
                        print("")
                        add_to_wallet(id)
                else:
                    print("the payment has been cancelled")
            else:
                print("please request a room first")


    write_login_data(data)