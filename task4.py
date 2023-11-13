import os
from typing import List


def get_next(name_class: str) -> str:
    """
    The function gets the name of the class and returns 
    the relative path to the next image, when the images end returns None.
    """
    path:str = os.path.join('dataset1', name_class)
    name_list:List[str] = os.listdir(path)
    name_list.append(None)
    for i in range(len(name_list)):
        if name_list[i] is not None:
            yield os.path.join(path, name_list[i])
        else:
            yield None


def main(name: str) -> None:
    """
    The function main() receives the class name as input and passes it to the function, 
    which returns the relative path to the next image, and prints them.
    """
    print(*get_next(name))


if __name__ == "__main__":
    main('rose')