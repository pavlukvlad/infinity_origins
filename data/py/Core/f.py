import json, pygame, sys, os, inspect

def export_json(data, path, file):
    with open(path, 'w') as file:
        json.dump(data, file)

def import_json(data, path, file):
    with open(path) as file:
        data = json.load(file)

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]