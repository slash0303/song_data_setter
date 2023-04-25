import eyed3
from eaxtension import LogE

name = input("Enter song name: ")

if name.find(".")==-1:
    ext = input("extension cannot found. please enter the extension: ")
    if ext.find(".")==-1:
        name += ("." + ext)
    else:
        name += ext
    LogE.g("modify", f"file name is modified to '{name}'")
    
LogE.g("song name", name)

song = eyed3.load(name)