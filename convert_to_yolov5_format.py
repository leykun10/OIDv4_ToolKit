import argparse
import os
import cv2
import numpy as np

if os.getcwd().__contains__("OIDv4_ToolKit"):
    class_path = "classes.txt"
else:
    class_path = os.path.join(os.getcwd(), "OIDv4_ToolKit/classes.txt")

with open(class_path, 'r') as class_file:
    class_names = class_file.read()
classes = [str(i) for i in class_names.split()]


def name_to_class(coords, shape):
    try:
        coords[0] = str(classes.index(coords[0]))
        coords[3] -= coords[1]
        coords[4] -= coords[2]
        x_diff = int(coords[3]/2)
        y_diff = int(coords[4]/2)
        coords[1] = coords[1]+x_diff
        coords[2] = coords[2]+y_diff
        coords[1] /= int(shape[1])
        coords[2] /= int(shape[0])
        coords[3] /= int(shape[1])
        coords[4] /= int(shape[0])
        coords[1] = str( coords[1])
        coords[2] = str( coords[2])
        coords[3] = str( coords[3])
        coords[4] = str( coords[4])

        return coords

    except ValueError:
        print("class not available")


def main(path):

    label_path = os.path.join(path, "labels")
    for file in os.listdir(label_path):
        data = os.path.join(label_path, file)

        img_name = "images/" + str.split(file, ".")[0] + ".jpg"
        image = cv2.imread(os.path.join(path, img_name))
        with open(data, 'r+') as f:
            arrays = []
            for line in f:
                labels = line.split(sep=" ")
                if labels[0] == "Vehicle":
                    c_labels = [labels[0], float(labels[3]), float(labels[4]), float(labels[5]), float(labels[6])]
                else:

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
    parser.add_argument("--path")
    args = parser.parse_args()
    main(str(args.path))
