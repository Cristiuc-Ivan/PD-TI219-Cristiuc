import os

def get_next_instance(class_label, dataset_dir):
    file_paths = os.listdir(dataset_dir)
    for a in file_paths:
        print(f"{dataset_dir}/{a}")

    return print("None")

label = "rose"
dir = 'C:/Users/ivanc/PycharmProjects/Dataset_copy'
get_next_instance(label, dir)
