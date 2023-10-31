import os


def get_next_instance(class_label, dataset_dir):
    file_paths = os.listdir(dataset_dir)
    for a in file_paths:
        print(f"{dataset_dir}/{a}")

    return print("None")


label = "rose"
direct = 'C:/Users/ivanc/PycharmProjects/Lab2/dataset/rose'
get_next_instance(label, direct)
