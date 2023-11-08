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
            new_path = shutil.copy(
            os.path.join(path, img),
            os.path.join(new_dir, f'{name}_{img}')
            ) 
            with open('Annotasion2.csv', 'a') as f:
                filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
                filewriter.writerow([os.path.join(abs_path, new_path), os.path.join(rel_path, new_path), name])

"""
def writing_absolute_path(dir: str) -> list:
    abs_path = os.path.join(os.path.abspath(dir))
    list_images = os.listdir(abs_path)
    rez_paths = []
    for i in list_images:
       rez_paths.append(os.path.join(abs_path, i))
    return rez_paths

def writing_relative_path(dir: str) -> list:
    rel_path = os.path.join(os.path.relpath(dir))
    list_images = os.listdir(rel_path)
    rez_paths = []
    for i in list_images:
       rez_paths.append(os.path.join(rel_path, i)) 
    return rez_paths

def creating_csvfile(namecsv: str, name: str) -> None:
    fields = ['Absolute path', 'Relative path', 'Class name']
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.DictWriter(f, delimiter=',', lineterminator='\r', fieldnames=fields)
        filewriter.writeheader()

def write_path(namecsv: str, name: str, dir: str):
    with open(f'{namecsv}.csv', 'a', newline='') as f:
        filewriter = csv.writer(f, delimiter=",", lineterminator='\r')
        abs_paths = writing_absolute_path(dir)
        rel_paths = writing_relative_path(dir)
        for abs_path,rel_path in zip(abs_paths, rel_paths):
            filewriter.writerow([abs_path, rel_path, name])
"""
def creating_csvfile(namecsv: str) -> None:
    with open(namecsv + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])
'''
def write_path(namecsv: str, classlist: list, dir: str) -> None:
    abs_paths = os.path.abspath(dir)
    rel_paths = os.path.relpath(dir) 
    print(classlist)   
    with open(f'{namecsv}.csv', 'a') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        for img in classlist[0]:
            for abs_path,rel_path in zip(abs_paths, rel_paths):
                filewriter.writerow([os.path.join(abs_path, img), os.path.join(rel_path, img), classlist[1]])
'''
def main() -> None:
    new_dir = "dataset2"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    class1 = "rose"
    class2 = "tulip"
    creating_csvfile("Annotasion2")
    copy_images("dataset1", "dataset2", [class1,class2])

    #write_path("Annotasion2", class1list, new_dir)

    #class2list = copy_images("dataset1", "dataset2", class2)
    #print(class1list, class2list)
    #copy_images("dataset1", "dataset2", class2)
    #write_path("Annotasion2", class2list, new_dir)

if __name__ == "__main__":
    main()