import csv
import os


def writing_absolute_path(name: str, dir: str) -> list:
    abs_path = os.path.join(os.path.abspath(dir), name)
    list_images = os.listdir(abs_path)
    rez_paths = []
    for i in list_images:
       rez_paths.append(os.path.join(abs_path, i))
    return rez_paths


def writing_relative_path(name: str, dir: str) -> list:
    rel_path = os.path.join(os.path.relpath(dir), name)
    list_images = os.listdir(rel_path)
    rez_paths = []
    for i in list_images:
       rez_paths.append(os.path.join(rel_path, i)) 
    return rez_paths


def creating_csvfile(namecsv: str, name: str) -> None:
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])


def write_path(namecsv: str, name: str, dir: str):
    with open(namecsv + ".csv", 'a', newline='') as f:
        filewriter = csv.writer(f, delimiter=",", lineterminator='\r')
        abs_paths = writing_absolute_path(name, dir)
        rel_paths = writing_relative_path(name, dir)
        for abs_path,rel_path in zip(abs_paths, rel_paths):
            filewriter.writerow([abs_path, rel_path, name])


def main() -> None:
    dir = "dataset1"
    class1 = "rose"
    class2 = "tulip"
    creating_csvfile("Annotasion1", dir)
    write_path("Annotasion1", class1, dir)
    write_path("Annotasion1", class2, dir)


if __name__ == "__main__":
    main()