# -*- coding: utf-8 -*-
import pickle
import zipfile
import os

def save_game(name, object):
    name = name.lower()
    with open(f"{name}.txt", "wb") as file: 
        pickle.dump(object, file)      
    zip = zipfile.ZipFile(f'saves/data/dates.zip', 'w')
    zip.write(f'{name}.txt', compress_type=zipfile.ZIP_DEFLATED)
    zip.close()
    os.remove(f"{name}.txt")

def load_game(name):
    name = name.lower()
    with zipfile.ZipFile("saves/data/dates.zip") as zf:
        zf.extract(f"{name}.txt", path="saves/data")
        with open(f"saves/data/{name}.txt", "rb") as f:
            object = pickle.load(f)
        os.remove(f"saves/data/{name}.txt")
    return object
