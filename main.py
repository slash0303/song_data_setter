import eyed3
from eaxtension import LogE

name = input("Enter song name: ")

if name.find(".")==-1:
    ext = input("extension cannot found. please enter the extension: ")
    if ext.find(".")==-1:
        name += ("." + ext)
    else:
        name += ext
    LogE.d("modify", f"file name is modified to '{name}'")
    
LogE.d("song name", name)