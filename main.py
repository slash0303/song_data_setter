import eyed3
import os
from eaxtension import LogE

# command text alias
command_alias = {"exit" : 1 }

def change_meta():
    name = input("Enter song name: ")

    if name[0] == "/":
    elif name.find(".")==-1:
        ext = input("extension cannot found. please enter the extension: ")
        if ext.find(".")==-1:
            name += ("." + ext)
        else:
            name += ext
        LogE.g("modify", f"file name is modified to '{name}'")

    LogE.g("song name", name)

    song = eyed3.load(name)

mode = input("What do you want?[change metadata/ls]: ")

if "cmd".find(mode) or "change metadata".find(mode):
    change_meta()