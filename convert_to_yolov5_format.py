import argparse


def name_to_class(name):
    if name.__eq__("Bus"):
        return "0"
    elif name.__eq__("Car"):
        return "1"
    elif name.__eq__("Vehicle_registration_plate"):
        return "2"
    elif name.__eq__("Motorcycle"):
        return "3"
    else:
        return "no_class"


def main():
    with open('tr.txt', 'r+') as f:
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
    main()
