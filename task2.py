import os
import shutil
import csv


def copy_images(old_dir: str, new_dir: str, names: list) -> None:
    abs_path = os.path.abspath(new_dir)
    rel_path = os.path.relpath(new_dir) 
    for name in names:
        path = os.path.join(os.path.abspath(old_dir), name)
        list_images = os.listdir(path)
        for img in list_images:
            shutil.copy(
            os.path.join(path, img),
            os.path.join(new_dir, f'{name}_{img}')
            ) 
            with open('Annotasion2.csv', 'a') as f:
                filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
                filewriter.writerow([os.path.join(abs_path, f'{name}_{img}'), os.path.join(rel_path, f'{name}_{img}'), name])


def creating_csvfile(namecsv: str) -> None:
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])


def main() -> None:
    new_dir = "dataset2"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    class_name = ["rose", "tulip"]
    creating_csvfile("Annotasion2")
    copy_images("dataset1", "dataset2", class_name)


if __name__ == "__main__":
    main()