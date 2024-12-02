import json
import os


def get(name):
    config = {}

    try:
        with open(os.getcwd() + '/' + name + '.json', 'r') as f:
            config = json.load(f)
            f.close()
    except FileNotFoundError:
        print('Config file not found')

    return config
