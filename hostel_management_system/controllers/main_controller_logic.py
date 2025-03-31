from view import register
from view import visit_request
from view import login

# menu for users to register/login/visit request/exit
def main_controller_menu():
    """helps user navigate and authentication services"""

    # using while loop so that user does not exit program 
    # unxpectedly while returning to previous menu
    while True:
        print("Enter 1 for Registeration")
        print("Enter 2 for Login")
        print("Enter 3 for Visit request")
        print("Enter 4 to Exit")

        #adding a try-except bloct in starting to catch all exceptions
        try:
            choice = int(input("Enter Your Choice :"))
            if choice == 1:
                register()
            elif choice == 2:
                login()
            elif choice == 3:
                visit_request()
            elif choice == 4:
                break
            else:
                print("enter valid number")
                print("Enter number between 1-4")
                main_controller_menu()
        except Exception as e:
            print(e,"\n")
            main_controller_menu()
