import eyed3
import os
from eaxtension import LogE

# command text alias
command_alias = {"exit" : 1 }

# metadata change manual
meta_man = ["song name",
            "artist name",
            "album",
            "album art",
            "lyrics (txt file location)",]

# metadata change function
def change_meta():
    name = input("Enter song name: ")

    # command
    if name[0] == "/":
        pass
        # TODO : make command feature
    # intergrity check
    elif name.find(".")==-1:
        ext = input("extension cannot found. please enter the extension: ")
        if ext.find(".")==-1:
            name += ("." + ext)
        else:
            name += ext
        LogE.g("modify", f"file name is modified to '{name}'")

    LogE.g("music file name", name)

    # music load
    song = eyed3.load(name)

    for i, x in enumerate(meta_man):
        a = input("Enter '" + x + "' (pass key: /!/): ")


mode = input("What do you want?[change metadata/ls]: ")

if "cmd".find(mode) or "change metadata".find(mode):
    change_meta()