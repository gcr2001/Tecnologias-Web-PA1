import os
from database import * 
import json

def extract_route(R):
    sindex = 3
    eindex = 0
    for i in range(sindex + 1, len(R)):
        if R[i] == " ":
            eindex = i
            break
    return R[sindex + 2: eindex]

def read_file(P):
    extensions = ['.txt', '.css', '.html', 'js']

    name, extension =os.path.splitext(P)

    if (extension in extensions):
        file_path = name + extension
        with open(file_path, "r") as file:
            return file.read()
    else:
        file_path = name + extension
        with open(file_path, "rb") as file:
            return file.read()

def load_data():
    database = Database(f'data/{db}')
    database.add(note)

def build_response(body='', code=200, reason='OK', headers=''):    
    if len(headers) > 0:
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()
        
    return f'HTTP/1.1 {code} {reason}\n\n{body}'.encode()
