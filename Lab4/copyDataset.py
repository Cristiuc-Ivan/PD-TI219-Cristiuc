import os
import shutil
import annotation


def copy_dataset(source, destination):
    global class_name
    for root, dirs, files in os.walk(source):
        for filename in files:
            class_name = os.path.basename(root)
            new_filename = f"{class_name}_{filename}"
            source_file = os.path.join(root, filename)
            destination_file = os.path.join(destination, new_filename)
            shutil.copy2(source_file, destination_file)

    annotation.create_annotation(destination, 'annotationOf-' + class_name + '-Copy.csv')

