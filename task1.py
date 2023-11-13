import csv
import os
from typing import List


def writing_absolute_path(name: str, dir: str) -> List[str]:
    """
    The function gets the absolute path of the specified directory 
    and a list of the names of the elements in it. Adds absolute paths of elements to the list.
    """
    abs_path:str = os.path.join(os.path.abspath(dir), name)
    list_images:List[str] = os.listdir(abs_path)
    rez_paths:List[str] = []
    for i in list_images:
       rez_paths.append(os.path.join(abs_path, i))
    return rez_paths


def writing_relative_path(name: str, dir: str) -> List[str]:
    """
    The function gets the relative path of the specified directory 
    and a list of the names of the elements in it. Adds relative paths of items to the list.
    """
    rel_path:str = os.path.join(os.path.relpath(dir), name)
    list_images:List[str] = os.listdir(rel_path)
    rez_paths:List[str] = []
    for i in list_images:
       rez_paths.append(os.path.join(rel_path, i)) 
    return rez_paths


def creating_csvfile(namecsv: str, name: str) -> None:
    """
    The function creates a .csv file and records the column names.
    """
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])


def write_path(namecsv: str, name: str, dir: str):
    """
    The function opens a .csv file and writes absolute and relative paths to the desired columns.
    """
    with open(namecsv + ".csv", 'a', newline='') as f:
        filewriter = csv.writer(f, delimiter=",", lineterminator='\r')
        abs_paths:List[str] = writing_absolute_path(name, dir)
        rel_paths:List[str] = writing_relative_path(name, dir)
        for abs_path,rel_path in zip(abs_paths, rel_paths):
            filewriter.writerow([abs_path, rel_path, name])


def main(name1: str, name2: str, dir: str) -> None:
    creating_csvfile("Annotasion1", dir)
    write_path("Annotasion1", name1, dir)
    write_path("Annotasion1", name2, dir)


if __name__ == "__main__":
    main('rose', 'tulip', 'dataset1')