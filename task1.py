import csv
import os

def creating_csvfile(name: str) -> None:
    with open(name + ".csv", 'w') as f:
        filewriter = csv.writer(f, delimiter=',', lineterminator='\r')
        filewriter.writerow(['Absolute path', 'Relative path', 'Class name'])
        

def main()->None:
    #print(os.getcwd()) 
    creating_csvfile("Annotasion dataset")

if __name__ == "__main__":
    main()