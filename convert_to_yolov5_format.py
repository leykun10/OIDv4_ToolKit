import argparse
import os
import cv2
import numpy as np

with open('classes.txt', 'r') as class_file:
    class_names = class_file.read()
classes = [str(i) for i in class_names.split()]


def name_to_class(array, shape):
    try:
        array[0] = str(classes.index(array[0]))
        array[3] = str((array[1] + ((array[3] - array[1]) / 2)) / int(shape[0]))
        array[4] = str((array[2] + ((array[4] - array[2]) / 2)) / int(shape[1]))
        array[1] = str(array[1] / int(shape[0]))
        array[2] = str(array[2] / int(shape[1]))

        return array

    except ValueError:
        print("class not available")


def main(path):
    label_path = os.path.join(path, "Label")
    for file in os.listdir(label_path):
        data = os.path.join(label_path, file)

        img_name = str.split(file, ".")[0] + ".png"
        print(os.path.join(path, img_name))
        image = cv2.imread(os.path.join(path, img_name))
        with open(data, 'r+') as f:
            arrays = []
            for line in f:
                print(line)
                labels = line.split(sep=" ")
                c_labels = [labels[0], float(labels[1]), float(labels[2]), float(labels[3]), float(labels[4])]
                m_labels = name_to_class(c_labels, image.shape)
                line = " ".join(m_labels)
                print(line)
                arrays.append(line + "\n")
            print(arrays[0], arrays[1])
            f.seek(0)
            f.writelines(arrays)
            f.truncate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Path to dataset')
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    main(str(args.path))
