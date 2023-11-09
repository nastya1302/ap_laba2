import os


def get_next(name_class: str) -> str:
    path = os.path.join('dataset1', name_class)
    name_list = os.listdir(path)
    name_list.append(None)
    for i in range(len(name_list)):
        if name_list[i] is not None:
            yield os.path.join(path, name_list[i])
        else:
            yield None


def main(name: str) -> None:
    print(*get_next(name))


if __name__ == "__main__":
    main('rose')