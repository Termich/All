import json
import pickle

with open('group.json','r') as f:
    js = json.load(f)

with open('group.dat', 'r') as f:
    pi = pickle.load(f)

print(js)

print(pi)