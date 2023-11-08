import os
import shutil
import csv
import random 


def copy_images(old_dir: str, new_dir: str, names: list) -> None:
    abs_path = os.path.abspath(new_dir)
    rel_path = os.path.relpath(new_dir)
    random_number = random.sample((range(0,10000)), 2000) 
    count = 0
    for name in names:
        path = os.path.join(os.path.abspath(old_dir), name)
        list_images = os.listdir(path)
        for img in list_images:
            new_name = f'{random_number[count]}'.zfill(5)
            shutil.copy(
            os.path.join(path, img),
            os.path.join(new_dir, f'{new_name}.jpg')
            ) 
            with open('Annotasion3.csv', 'a') as f:
                filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
                filewriter.writerow([os.path.join(abs_path, f'{new_name}.jpg'), os.path.join(rel_path, f'{new_name}.jpg'), name])
                count += 1


def creating_csvfile(namecsv: str) -> None:
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])


def main() -> None:
    new_dir = "dataset3"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    class_name = ["rose", "tulip"]
    creating_csvfile("Annotasion3")
    copy_images("dataset1", new_dir, class_name)


if __name__ == "__main__":
    main()