import os
import re
import json
from google.protobuf import json_format

def append_unique(l, i):
    if not i in l:
        l.append(i)

def initial_state(generators):
    state = {}
    state['types'] = generators.keys()
    state['generators'] = generators
    for key in generators:
        state[key] = {}

    return state

def message_to_json(message):
    json = json_format.MessageToJson(message)
    return re.sub(r' +', ' ', json.replace('\n', ''))

def process_input(state, path, process):
    if os.path.isdir(path):
        for item in os.listdir(path):
            with open(item) as input:
                state = process(state, input)
    else:
        with open(path) as input:
            state = process(state, input)

    return state

def output_state(state, path):
    json = []
    for type in state['types']:
        for key in state[type]:
            message = message_to_json(state[type][key])
            json.append(message)
    out = '\n'.join(json)
    outhandle = open(path, 'w')
    outhandle.write(out)
    outhandle.close()

class RecordGenerator(object):
    def __init__(self, name):
        self.name = name

    def schema(self):
        raise Exception('schema() not implemented')

    def gid(self, data):
        raise Exception('gid() not implemented')

    def update(self, record, data):
        raise Exception('update() not implemented')

    def create(self, data):
        record = self.schema()
        gid = self.gid(data)
        record.gid = gid
        record.type = self.name
        self.update(record, data)
        return record

    def find(self, state, data):
        gid = self.gid(data)
        record = state[self.name].get(gid)
        if record is None:
            record = self.create(data)
            state[self.name][gid] = record
        return record
