import os
import json

CURRENT_DIR = os.getcwd()
LOGIN_JSON_FILE_PATH = os.path.join(CURRENT_DIR, 'models', 'json', 'login_data.json')
VISITOR_JSON_FILE_PATH = os.path.join(CURRENT_DIR, 'models', 'json', 'visit_data.json')
ROOM_JSON_FILE_PATH = os.path.join(CURRENT_DIR, 'models', 'json', 'room_data.json')
ISSUE_JSON_FILE_PATH = os.path.join(CURRENT_DIR, 'models', 'json', 'issue_data.json')
CHANGE_ROOM_JSON_FILE_PATH = os.path.join(CURRENT_DIR, 'models', 'json', 'change_room_data.json')
WAIT_LIST_JSON_FILE_PATH = os.path.join(CURRENT_DIR, 'models', 'json', 'wait_list_data.json')
ADD_TO_WALLET_FILE_PATH = os.path.join(CURRENT_DIR, 'models', 'json', 'add_to_wallet.json')