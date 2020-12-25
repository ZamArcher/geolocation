#
# import os
# import tempfile
# import json
# import argparse
#
# storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# current_dict = {}
#
# if os.path.exists(storage_path) == True:
#     with open(storage_path, 'r') as f:
#         current_dict = json.load(f)
#
# parser = argparse.ArgumentParser(description='Process some integers.') # задаем парсер
# parser.add_argument('--key', action="store", dest='key')
# parser.add_argument('--val', action="store", dest='val')
# args = parser.parse_args()
#
# with open(storage_path, 'w') as f:
#     if args.key in current_dict:
#         if isinstance(current_dict[args.key], list):
#             current_dict[args.key].append(args.val)
#         else:
#             current_dict[args.key] = [current_dict[args.key], args.val]
#     else:
#         current_dict[args.key] = args.val
#     json.dump(current_dict, f)
#
# if args.val is None:
#     if current_dict[args.key]:
#         delimiter = ', '
#         current_dict[args.key] = [x for x in current_dict[args.key] if x]
#         output = delimiter.join(current_dict[args.key])
#         print(output)
#     else:
#         print('')

import argparse
import json
import os
import tempfile


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()


def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def get(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])


def main(storage_path):
    args = parse()

    if args.key and args.val:
        put(storage_path, args.key, args.val)
    elif args.key:
        print(*get(storage_path, args.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)