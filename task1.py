import csv
import os

def writing_absolute_path(name: str) -> list:
    p = os.path.abspath('dataset')
    #print(p)
    path_n = os.path.join(p, name)
    rez = os.listdir(path_n)
    #print(path_n)
    rez_path = []
    for i in rez:
       rez_path.append(os.path.join(path_n, i))
    #for item in enumerate(rez_path):
    #    print(item) 
    return rez_path

def writing_relative_path(name: str) -> list:
    p = os.path.relpath('dataset')
    #print(p)
    path_n = os.path.join(p, name)
    rez = os.listdir(path_n)
    #print(path_n)
    rez_path = []
    for i in rez:
       rez_path.append(os.path.join(path_n, i))
    #for item in enumerate(rez_path):
    #    print(item) 
    return rez_path

def creating_csvfile(name: str, names: str) -> None:
    with open(name + ".csv", 'w', newline='') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])
    #p = os.path.abspath(name+".csv")
    #print(p)
        for i in names:
           filewriter.writerow([writing_absolute_path(i), writing_relative_path(i), i])
           #writing_absolute_path(i)
           #writing_relative_path(i)

def main()->None:
    #print(os.getcwd()) 
    names = ("rose", "tulip")
    creating_csvfile("Annotasion1", names)

if __name__ == "__main__":
    main()