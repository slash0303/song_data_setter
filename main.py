import eyed3
import os
from eaxtension import LogE

# command mode: - fucntion alias
command_alias = {"ls": "" }

# metadata: change manual
meta_man = ["song name",
            "artist name",
            "album",
            "album artist",
            "lyrics (txt file location)",]

# metadata change function
def change_meta():
    while True:
        try:
            name = input("Enter file name: ")

            # command
            if name[0] == "/":
                pass
                # TODO : make command feature
            # file name intergrity check
            elif name.find(".mp3")==-1 or name.find(".wav")==-1 or name.find(".flac")==-1:
                ext = input("extension cannot found. please enter the extension: ")
                if ext.find(".")==-1:
                    name += ("." + ext)
                else:
                    name += ext

                # music load
                song = eyed3.load(name).tag
                break
        except:
            print("file name is incorrect. please re-write file name.")

    LogE.g("modify", f"file name is modified to '{name}'")

    LogE.g("music file name", name)



    # metadata: mode index - function mapping
    meta_alias = {0: song.title,
                  1: song.artist,
                  2: song.album,
                  3: song.album_artist,
                  4: song.lyrics}

    # change meta data
    for i, x in enumerate(meta_man):
        a = input("Enter '" + x + "' (pass key: /!/): ")
        meta_alias[i] = a

    for x in meta_alias.values():
        print(x)

    save_yn = input("is it correct?[Y/n]: ")
    if save_yn == "Y" or save_yn == "y":
        song.save()

mode = input("What do you want?[change metadata/command mode]: ")

if "change metadata".find(mode) != -1:
    change_meta()

elif "command mode".find(mode) != -1:
    pass
    # TODO : make command feature