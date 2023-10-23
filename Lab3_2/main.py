import os
import shutil
import csv

def copy_dataset(source, destination):
    for root, dirs, files in os.walk(source):
        for filename in files:
            class_name = os.path.basename(root)
            new_filename = f"{class_name}_{filename}"
            source_file = os.path.join(root, filename)
            destination_file = os.path.join(destination, new_filename)
            shutil.copy2(source_file, destination_file)

def create_annotation(dataset_path, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
        for root, _, files in os.walk(dataset_path):
            for file in files:
                absolute_path = os.path.join(root, file)
                relative_path = os.path.relpath(absolute_path, start=dataset_path)
                class_label = os.path.basename(root)
                writer.writerow([absolute_path, relative_path, class_label])


os.chdir("..")
if not os.path.isdir("Dataset"):
    os.mkdir("Dataset")

source_dir = "C:/Users/ivanc/PycharmProjects/Lab2/dataset/rose"
destination_dir = "C:/Users/ivanc/PycharmProjects/Dataset"
copy_dataset(source_dir, destination_dir)

os.chdir('C:/Users/ivanc/PycharmProjects/Lab3_2')
dataset_path = 'C:/Users/ivanc/PycharmProjects/Dataset'
output_file = 'annotation.csv'
create_annotation(dataset_path, output_file)