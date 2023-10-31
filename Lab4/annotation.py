import csv
import os


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
