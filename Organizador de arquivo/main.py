import os
import shutil
from tkinter.filedialog import askdirectory


def Select_dir():
    path = askdirectory()
    print(path)

    for item in os.listdir(path):
        File_name, File_ext = os.path.splitext(item)
        File_ext = File_ext[1:]
        print(f"-- {File_name} - {File_ext}")

    for item in os.listdir(path):
        File_name, File_ext = os.path.splitext(item)
        File_ext = File_ext[1:]
        folder = f"{path}/{File_ext}"
        
        if not os.path.exists(folder):
            os.makedirs(folder)
        else:
            pass

        print(f"Movendo {File_name}.{File_ext}")

        shutil.move(f"{path}/{File_name}.{File_ext}", f"{folder}/{File_name}.{File_ext}")

Select_dir()

os.system("pause")