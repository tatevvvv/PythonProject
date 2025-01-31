import json

with open("file.txt", 'r+') as f:
    f.write('[1 ,2 3]')
    x = json.load(f)