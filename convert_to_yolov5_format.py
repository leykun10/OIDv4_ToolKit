import argparse
import os

with open('classes.txt', 'r') as f:
    data = f.read()
classes = [str(i) for i in data.split()]


def name_to_class(name):
    try:
        return str(classes.index(name))

    except ValueError:

        return "no Class"


def main(path):
    for file in os.listdir(path):
        data = os.path.join(path, file)
        with open(data, 'r+') as f:
            arrays = []
            for line in f:
                print(line)
                array = line.split(sep=" ")
                array[0] = name_to_class(array[0])

                line = " ".join(array)
                print(line)
                arrays.append(line)
            f.seek(0)
            f.writelines(arrays)
            f.truncate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Path to dataset')
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    main(str(args.path))
