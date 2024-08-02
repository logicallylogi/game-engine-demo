from lib.Stage import get_stage
from lib.Save import autosave, load_save
from pickle import load

player = load_save()

with open("level.dat", "rb") as f:
    level = load(f)
    print(level)

print(player)

player["stage"] = 0

while True:
    if player["stage"] == -1:
        exit(0)
    player["stage"] = get_stage(player["stage"])
    player = autosave(player)
