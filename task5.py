import os
from typing import List


class MyIterator:
    def __init__(self, class_name: str):
        self.class_name:str = class_name
        self.counter:int = 0
        self.data:List[str] = os.listdir(os.path.join('dataset1', class_name))
        self.limit:int = len(self.data)

    def __next__(self):
        if self.counter < self.limit:
            path:str = os.path.join(self.class_name, self.data[self.counter])
            self.counter += 1
            return path
        else:
            raise StopIteration


def main(name: str):
    class_name:MyIterator = MyIterator(name)

    for _ in range(5):
        print(next(class_name))


if __name__ == "__main__":
    main('rose')