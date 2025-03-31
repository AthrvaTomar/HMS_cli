# from view import change_room, leave_room, pay_fees, pay_fine, raise_issue, request_room
# we will not use relative path to avoid circular import error
from view.user_features.change_room_logic import change_room
from view.user_features.leave_room_logic import leave_room
from view.user_features.pay_fees_logic import pay_fees
from view.user_features.pay_fine_logic import pay_fine
from view.user_features.raise_issue_logic import raise_issue
from view.user_features.request_room_logic import request_room
from view.user_features.add_to_wallet_logic import add_to_wallet

def user_controller(id):
    print("Welcome to user options")
    print("-------------------------------------------------------------")
    
    while True:
        print("Enter 1 for Request room")
        print("Enter 2 for Pay fees")
        print("Enter 3 for Pay fine")
        print("Enter 4 to Raise issue")
        print("Enter 5 for room change request")
        print("Enter 6 for room leave request")
        print("Enter 7 to add money to wallet")
        print("Enter 0 to retuen to main menu")
        choice = int(input("Enter Your Choice :"))
        print("")
        if choice == 1:
            request_room(id)
        elif choice == 2:
            pay_fees(id)
        elif choice == 3:
            pay_fine(id)
        elif choice == 4:
            raise_issue(id)
        elif choice == 5:
            change_room(id)
        elif choice == 6:
            leave_room(id)
        elif choice == 7:
            add_to_wallet(id)
        elif choice == 0:
            print("returning")
            return
        else:
            print("enter valid number")