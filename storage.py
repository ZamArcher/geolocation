
import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
current_dict = {}

if os.path.exists(storage_path) == True:
    with open(storage_path, 'r') as f:
        current_dict = json.load(f)

parser = argparse.ArgumentParser(description='Process some integers.') # задаем парсер
parser.add_argument('--key', action="store", dest='key')
parser.add_argument('--val', action="store", dest='val')
args = parser.parse_args()

with open(storage_path, 'w') as f:
    if args.key in current_dict:
        if isinstance(current_dict[args.key], list):
            current_dict[args.key].append(args.val)
        else:
            current_dict[args.key] = [current_dict[args.key], args.val]
    else:
        current_dict[args.key] = args.val
    json.dump(current_dict, f)

if args.val is None:
    if current_dict[args.key]:
        delimiter = ', '
        current_dict[args.key] = [x for x in current_dict[args.key] if x]
        output = delimiter.join(current_dict[args.key])
        print(output)
    else:
        print('')
