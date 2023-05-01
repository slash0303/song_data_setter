import os

try:
    os.system("python main.py")
except:
    os.system("python dependency.py")
    os.system("python main.py")