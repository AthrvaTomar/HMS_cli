from utils import fetch_issue_data,write_issue_data

def raise_issue(id):
    data = fetch_issue_data()
    issue_message = input("message for issue description: ")
    data.append(issue_message)
    write_issue_data(data)
    print("you issue has been registered")
