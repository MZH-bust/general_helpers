import json
from types import SimpleNamespace


def dict_to_singlenamespace(dic):
    return SimpleNamespace(**dic)


with open("config/testconfig.JSON") as json_data_file:
    data = json.load(json_data_file, object_hook=dict_to_singlenamespace)
