from utils import fetch_add_to_wallet_data,write_add_to_wallet_data

def add_to_wallet(id):
    wallet_request_data = fetch_add_to_wallet_data()

    add_to_wallet_amount = input("Enter the amount you want to add to your wallet: ")
    temp_dict = {"id":id,"add_to_wallet_amount":add_to_wallet_amount}

    wallet_request_data.append(temp_dict)
    print("your request has been submitted")
    print("")
    
    write_add_to_wallet_data(wallet_request_data)
