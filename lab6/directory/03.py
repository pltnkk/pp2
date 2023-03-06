import os

path = "/Users/kpiltann/Desktop/pp2"


if os.access(path, os.F_OK):
    print(f"File: {os.path.basename(path)}")
    print(f"Directory: {os.path.dirname(path)}")
else:
    print("Path is not executable")
