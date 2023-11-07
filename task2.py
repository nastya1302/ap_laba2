import os

def main() -> None:
    if not os.path.isdir('dataset2'):
        os.mkdir('dataset2')

if __name__ == "__main__":
    main()