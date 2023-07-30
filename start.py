import os

try:
    os.system("python main.py")
except:
    os.system("python dependencies.py")
    os.system("python main.py")