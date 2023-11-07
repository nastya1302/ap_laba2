import os
import shutil
from random import randint

def copy_images(old_dir: str, new_dir: str, names: str) -> None:
    for name in names:
        path = os.path.join(os.path.abspath(old_dir), name)
        list_images = os.listdir(path)
        for img in list_images:
            shutil.copy(
            os.path.join(path, img),
            os.path.join(new_dir, f'{randint(0,10000)}')
            )

def main():
    new_dir = "dataset3"
    names = ('rose', 'tulip')
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    copy_images("dataset1", new_dir, names)

if __name__ == "__main__":
    main()