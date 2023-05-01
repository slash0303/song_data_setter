import eyed3
import os
import glob
from eaxtension import LogE

# command mode: - fucntion alias
command_alias = {"ls": "" }

# metadata: change manual
meta_man = ["title of song",
            "name of artist",
            "name of album",
            "name of album artist",
            "lyrics (txt file path)",]

ext_list = [".mp3", ".wav", ".m4a", ".mpeg"]
ext_in = False

# metadata change function
def change_meta_manual():
    while True:
        try:
            name = input("Enter file name: ")

            # command
            if name[0] == "/":
                pass
                # TODO make command feature
            # file name intergrity check
            else:
                for x in ext_list:
                    if name.find(x) != -1:
                        ex_in = True
                if ext_in:
                    pass
                else:
                    ext = input("extension cannot found. please enter the extension: ")
                    if ext.find(".")==-1:
                        name += ("." + ext)
                    else:
                        name += ext

                # music load
            song = eyed3.load(name)
            song = song.tag
            break
        except:
            print("file name is incorrect. please re-write file name.")

    LogE.g("modify", f"file name is modified to '{name}'")

    LogE.g("music file name", name)

    input_list = {}

    # change meta data
    for x in meta_man:
        data_input = input("Enter '" + x + "' (pass key: /!/): ")
        if data_input == "/!/":
            input_list[x] = ""
            continue
        if x == "title of song":
            song.title = data_input
            input_list[x] = data_input
        elif x == "name of artist":
            song.artist = data_input
            input_list[x] = data_input
        elif x == "name of album":
            song.album = data_input
            input_list[x] = data_input
        elif x == "name of album artist":
            song.album_artist = data_input
            input_list[x] = data_input
        elif x.find("lyrics") != -1:
            lyr_dir = x
            try:
                with open(lyr_dir, "r", encoding="utf-8") as lyr:
                    song.lyrics = lyr
                input_list[x] = data_input
            except:
                LogE.e("FileNotFoundError", f"path '{data_input}' is wrong path.")
                input_list[x] = ""

    # check input value before saving data
    for x in input_list.keys():
        if input_list[x] == "":
            i = "[Unchanged]"
        else:
            i = input_list[x]
        LogE.g(x, i)
    save_yn = input("is it correct?[Y/n]: ")
    if save_yn == "N" or save_yn == "n":
        pass
    else:
        song.save(version=eyed3.id3.ID3_V2_3)

def change_meta_auto():
    #TODO use beautifulsoup or spotify web api to find data of song in internet.
    pass

# select mode
mode = input("What do you want?[change metadata/command mode]: ")
if "change metadata".find(mode) != -1:
    # select manual or automatic
    mode = input("manual / automatic: ")
    if "manual".find(mode) != -1:
        change_meta_manual()
    elif "automatic".find(mode) != -1:
        # input path and intergrity test
        while True:
            path = input("please enter working path(default value is pwd): ")
            if path == "":
                pass
            else:
                try:
                    os.chdir(path)
                    break
                except Exception as e:
                    LogE.e(e, f"path '{path}'is wrong path.")
        # select all or decide in automatic menu
        mode = input("all of file / decide: ")
        if "all of file".find(mode) != -1:
            file_list = []
            for x in ext_list:
                file_list += glob.glob("*"+x)
            for file in file_list:
                change_meta_auto()
        elif "decide".find(mode) != -1:
            pass
            #TODO get file name from user input and modify one of file

elif "command mode".find(mode) != -1:
    pass
    # TODO make command feature