from utils import fetch_login_data
from constants import LOGIN_JSON_FILE_PATH,VISITOR_JSON_FILE_PATH,ROOM_JSON_FILE_PATH,ADD_TO_WALLET_FILE_PATH
from constants import ISSUE_JSON_FILE_PATH,CHANGE_ROOM_JSON_FILE_PATH,WAIT_LIST_JSON_FILE_PATH
import json

def write_data(file_path, new_data):
    with open(file_path, 'w') as file:
        json.dump(new_data, file, indent=4)

# using lambda (input): functioncall(file_path,input_data)
write_login_data = lambda new_data: write_data(LOGIN_JSON_FILE_PATH, new_data)
write_visitor_data = lambda new_data: write_data(VISITOR_JSON_FILE_PATH, new_data)
write_room_data = lambda new_data: write_data(ROOM_JSON_FILE_PATH, new_data)
write_issue_data = lambda new_data: write_data(ISSUE_JSON_FILE_PATH, new_data)
write_change_room_data = lambda new_data: write_data(CHANGE_ROOM_JSON_FILE_PATH, new_data)
write_wait_list_data = lambda new_data: write_data(WAIT_LIST_JSON_FILE_PATH, new_data)
write_add_to_wallet_data = lambda new_data: write_data(ADD_TO_WALLET_FILE_PATH, new_data)
