import os
import json
from constants import LOGIN_JSON_FILE_PATH,VISITOR_JSON_FILE_PATH,ROOM_JSON_FILE_PATH,ADD_TO_WALLET_FILE_PATH
from constants import ISSUE_JSON_FILE_PATH,CHANGE_ROOM_JSON_FILE_PATH,WAIT_LIST_JSON_FILE_PATH

def get_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(e)

fetch_login_data = lambda: get_data(LOGIN_JSON_FILE_PATH)
fetch_visitor_data = lambda: get_data(VISITOR_JSON_FILE_PATH)
fetch_room_data = lambda: get_data(ROOM_JSON_FILE_PATH)
fetch_issue_data = lambda: get_data(ISSUE_JSON_FILE_PATH)
fetch_change_room_data = lambda: get_data(CHANGE_ROOM_JSON_FILE_PATH)
fetch_wait_list_data = lambda: get_data(WAIT_LIST_JSON_FILE_PATH)
fetch_add_to_wallet_data = lambda: get_data(ADD_TO_WALLET_FILE_PATH)
