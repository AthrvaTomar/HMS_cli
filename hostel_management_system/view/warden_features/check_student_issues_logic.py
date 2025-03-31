from utils import fetch_issue_data,write_issue_data

def check_student_issues():
    data = fetch_issue_data()
    data_enumerated = list(enumerate(data,1))
    for records in data_enumerated:
        print(records)

    remove_issue = input("enter issue numbers (comma seprated) that have been resolved: ")
    if not remove_issue:
        print("no issues resolved")
    else:
        remove_issue_list = remove_issue.split(",")
        final_data = data_enumerated[:]
        for item in remove_issue_list:
            for records in data_enumerated:
                if int(item) == int(records[0]):
                    final_data.remove(records)
                    print(f"{records[1]} has been resolved")
        data = []
        for records in final_data:
            data.append(records[1])
        write_issue_data(data)