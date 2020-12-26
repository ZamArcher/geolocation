
from functools import wraps
import json

def to_json(function_to_decorate):
    @wraps(function_to_decorate)
    def the_wrapper_around_the_original_function(*args, **kwargs):
        origin_dict = function_to_decorate(*args, **kwargs)
        json_value = json.JSONEncoder().encode(origin_dict)
        return json_value
    return the_wrapper_around_the_original_function

@to_json
def get_data():
    return {
        'data': 42
    }
print(get_data())  # вернёт '{"data": 42}'