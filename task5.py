import os


class MyIterator:
    def __init__(self, class_name):
        self.class_name = class_name
        self.counter = 0
        self.data = os.listdir(os.path.join('dataset1', class_name))
        self.limit = len(self.data)

    def __next__(self):
        if self.counter < self.limit:
            path = os.path.join(self.class_name, self.data[self.counter])
            self.counter += 1
            return path
        else:
            raise StopIteration


def main():
    class_rose = MyIterator('rose')

    for i in range(5):
        print(next(class_rose))


if __name__ == "__main__":
    main()