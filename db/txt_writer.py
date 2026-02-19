import os
from config import TXT_FILE

def write_to_txt(labels, row_data):
    file_exists = os.path.isfile(TXT_FILE)
    with open(TXT_FILE, 'a') as f:
        if not file_exists:
            f.write(",".join(labels) + "\n")
        f.write(",".join(row_data) + "\n")