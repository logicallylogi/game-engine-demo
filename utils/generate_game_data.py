from pickle import dump
from importlib import import_module

stages = import_module("data.levels")
levels = []

for i in stages.__all__:
    levels.append(stages.__dict__[i].__dict__[i])

data = {
    "stages": levels
}

print(data)

with open("level.dat", "wb") as f:
    dump(data, f)

print("Gamedata exported successfully")
