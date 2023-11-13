import os
import shutil
import csv
import random 
from typing import List


def copy_images(old_dir: str, new_dir: str, names: List[str]) -> None:
    """
    The function copies one image from the old directory to the new one, 
    changing the name, and immediately writes its absolute, relative paths and class name to the .csv file.
    """
    abs_path:str = os.path.abspath(new_dir)
    rel_path:str = os.path.relpath(new_dir)
    random_number:List[str] = random.sample((range(0,10000)), 2000) 
    count:int = 0
    for name in names:
        path:str = os.path.join(os.path.abspath(old_dir), name)
        list_images:List[str] = os.listdir(path)
        for img in list_images:
            new_name:str = f'{random_number[count]}'.zfill(5)
            shutil.copy(
            os.path.join(path, img),
            os.path.join(new_dir, f'{new_name}.jpg')
            ) 
            with open('Annotasion3.csv', 'a') as f:
                filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
                filewriter.writerow([os.path.join(abs_path, f'{new_name}.jpg'), os.path.join(rel_path, f'{new_name}.jpg'), name])
                count += 1


def creating_csvfile(namecsv: str) -> None:
    """
    The function creates a .csv file and records the column names.
    """
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])


def main(names: List[str], old_dir: str, new_dir: str) -> None:
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    creating_csvfile("Annotasion3")
    copy_images("dataset1", new_dir, names)


if __name__ == "__main__":
    main(["rose", "tulip"], 'dataset1', 'dataset3')