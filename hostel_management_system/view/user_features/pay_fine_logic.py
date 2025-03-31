from utils import fetch_login_data,write_login_data
from .add_to_wallet_logic import add_to_wallet

def pay_fine(id):
    data = fetch_login_data()
    for records in data:
        if id == records["id"]:
            if records["fine_due"]:
                if records["wallet"]:
                    if records["wallet"]>records["fine_due"]:
                        records["wallet"]-=records["fine_due"]
                        print(f"paying fine of {records["fine_due"]}")
                        print(f"new wallet balance is {records["wallet"]}")
                        records["fine_due"] = None
                        print("")
                    else:
                        print("")
                        print("your don't have enough balance, please add amount to it")
                        print("")
                        add_to_wallet(id)
                else:
                    print("")
                    print("your wallet is empty, please add amount to it")
                    print("")
                    add_to_wallet(id)
            else:
                print("no fine present")
                print("")

    write_login_data(data)