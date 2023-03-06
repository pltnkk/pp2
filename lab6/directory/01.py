import os


put = "/Users/kpiltann/Desktop/pp2"


print("Directories:")
for papka in os.scandir(put):
    if papka.is_dir():
        print(papka.name)

print("\nFiles:")
for file in os.scandir(put):
    if file.is_file():
        print(file.name)


print("\nDirectories and Files:")
for all in os.scandir(put):
    if all.is_dir():
        print("Directory: " + all.name)
    elif all.is_file():
        print("File: " + all.name)


