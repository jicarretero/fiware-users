import json

import sys
import json
import requests
import os
import datetime
import time


def load_json_file(file_name):
    data=json.loads(open(file_name,'r').read())
    return data

def get_dict_from_data(data, data_key, key_field):
    return dict(zip( [k[key_field] for k in data[data_key]],  data[data_key]))

def get_filtered_data(data, data_key, contained_field):
    return filter(lambda x: contanied_field in x, data[data_key])

def ts_milis():
    return int(time.mktime(datetime.datetime.now().timetuple()) * 1000)
