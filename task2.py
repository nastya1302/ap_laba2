import os
import shutil
import csv
from pathlib import Path

def copy_images(old_dir: str, new_dir: str, name: str) -> None:
    path = os.path.join(os.path.abspath(old_dir), name)
    list_images = os.listdir(path)
    for img in list_images:
        shutil.copy(
        os.path.join(path, img),
        os.path.join(new_dir, f'{name}_{img}')
        )

def creating_csvfile(namecsv: str, dir: str):
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', "Class name"])
        abs_paths = writing_absolute_path(dir)
        rel_paths = writing_relative_path(dir)
        for abs_path,rel_path in zip(abs_paths, rel_paths):
            filewriter.writerow([abs_path, rel_path, ])

def writing_absolute_path(dir: str):
    abs_path = os.path.join(os.path.abspath(dir))
    list_images = os.listdir(abs_path)
    rez_paths = []
    for i in list_images:
       rez_paths.append(os.path.join(abs_path, i))
    return rez_paths
    
def writing_relative_path(dir):
    rel_path = os.path.join(os.path.relpath(dir))
    list_images = os.listdir(rel_path)
    rez_paths = []
    for i in list_images:
       rez_paths.append(os.path.join(rel_path, i)) 
    return rez_paths

def main() -> None:
    new_dir = "dataset2"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    names = ("rose", "tulip")
    for i in names:
        copy_images("dataset1", "dataset2", i)
    creating_csvfile("Annotasion2", new_dir)

if __name__ == "__main__":
    main()