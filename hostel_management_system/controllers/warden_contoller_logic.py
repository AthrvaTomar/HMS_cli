from view.warden_features.approval_room_request_logic import approval_room_request
from view.warden_features.check_wait_list_logic import check_wait_list
from view.warden_features.change_room_request_logic import change_room_request
from view.warden_features.check_student_issues_logic import check_student_issues
from view.warden_features.issue_fines_logic import issue_fines
from view.warden_features.check_visitors_logic import check_visitors
from view.warden_features.search_logic import search
from view.warden_features.handle_wallet_request_logic import handle_wallet_request

def warden_contoller():
    print("-------------------------------------------------------------")
    print("welcome to warden options")
    print("-------------------------------------------------------------")

    while True:
        print("Enter 1 for Approve room requests")
        print("Enter 2 for check_wait_list")
        print("Enter 3 to room change request")
        print("Enter 4 for check student issues")
        print("Enter 5 for Issue fines to students")
        print("Enter 6 for checking visitors")
        print("Enter 7 to search by students or room")
        print("Enter 8 to handle wallet requests")
        print("Enter 0 to retuen to main menu")
        choice = int(input("Enter Your Choice :"))
        print("")
        if choice == 1:
            approval_room_request()
        elif choice == 2:
            check_wait_list()
        elif choice == 3:
            change_room_request()
        elif choice == 4:
            check_student_issues()
        elif choice == 5:
            issue_fines()
        elif choice == 6:
            check_visitors()
        elif choice == 7:
            search()
        elif choice == 8:
            handle_wallet_request()
        elif choice == 0:
            print("returning")
            return
        else:
            print("enter valid number")
