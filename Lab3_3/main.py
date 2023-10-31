import os
import shutil
import random

os.chdir("..")
if not os.path.isdir("Dataset_copy"):
    os.mkdir("Dataset_copy")

source_dir = 'C:/Users/ivanc/PycharmProjects/Dataset'
destination_dir = 'C:/Users/ivanc/PycharmProjects/Dataset_copy'

for root, dirs, files in os.walk(source_dir):
    for filename in files:
        random_number = random.randint(0, 10000)
        new_filename = f"{random_number}.jpg"
        source_file = os.path.join(root, filename)
        destination_file = os.path.join(destination_dir, new_filename)
        shutil.copy2(source_file, destination_file)