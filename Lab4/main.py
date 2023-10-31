import tkinter
from tkinter import *
from tkinter import filedialog
import annotation
import copyDataset
import os
import copyDsWithRandomNumb
from PIL import ImageTk, Image
import slideImages


# function for creating gradient in canvas
def create_gradient(element, x1, y1, x2, y2, start_color, end_color):
    height = y2 - y1

    for i in range(height):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / height)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / height)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / height)

        color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        element.create_rectangle(x1, y1 + i, x2, y1 + i + 1, fill=color, width=0)


# function for opening File Explorer and choosing directory
def open_folder_dialog():
    global dataset_path
    dataset_path = filedialog.askdirectory()  # open directory choosing
    pathText = canvas.create_text(270, 290, text='Dataset path is:\n' + dataset_path, font=('Roboto', 18))


def create_annotation():
    annotation.create_annotation(dataset_path, 'annotation.csv')


def copy_dataset():
    copy_path = filedialog.askdirectory()  # open directory choosing
    copyDataset.copy_dataset(dataset_path, copy_path)


def copy_dataset_with_random_numbers():
    copy_path = filedialog.askdirectory()  # open directory choosing
    copyDsWithRandomNumb.create_dataset_copy(dataset_path, copy_path)


def show_images():
    slideImages.slider()


# Main window
mainWindow = Tk()
mainWindow.title('Flowers')
mainWindow.geometry('650x700')
mainWindow.iconphoto(True, tkinter.PhotoImage(file="C:/Users/ivanc/PycharmProjects/Lab4/favicon.png"))
canvas = Canvas(mainWindow, width=650, height=700)
canvas.pack()
create_gradient(canvas, 0, 0, 650, 700, (255, 195, 113), (255, 95, 109))

# Button of directory choosing window
button = tkinter.Button(canvas, text="Select Folder", command=open_folder_dialog, bg='#16BFFD',
                        font=('Roboto', 14))
button_window = canvas.create_window(315, 50, anchor=tkinter.CENTER, window=button, height=70, width=590)

os.chdir("..")
if not os.path.isdir("DatasetCopy"):
    os.mkdir("DatasetCopy")

if not os.path.isdir("DatasetCopyRandom"):
    os.mkdir("DatasetCopyRandom")

# Main app buttons
annotationButton = tkinter.Button(canvas, text="Create annotation for dataset", command=create_annotation,
                                  bg='#16BFFD', font=('Roboto', 14))
annotationButton_window = canvas.create_window(165, 130, anchor=tkinter.CENTER, window=annotationButton, height=70,
                                               width=290)

copyDatasetButton = tkinter.Button(canvas, text="Copy dataset to new directory", command=copy_dataset,
                                   bg='#16BFFD', font=('Roboto', 14))
copyDatasetButton_window = canvas.create_window(465, 130, anchor=tkinter.CENTER, window=copyDatasetButton,
                                                height=70, width=290)

copyRandomDSButton = tkinter.Button(canvas, text="Create dataset copy\nwith random numbers",
                                    command=copy_dataset_with_random_numbers, bg='#16BFFD', font=('Roboto', 14))
copyRandomDSButton_window = canvas.create_window(165, 210, anchor=tkinter.CENTER, window=copyRandomDSButton,
                                                 height=70, width=290)

viewImages = tkinter.Button(canvas, text="View dataset instances", command=copy_dataset,
                            bg='#16BFFD', font=('Roboto', 14))
viewImages_window = canvas.create_window(465, 210, anchor=tkinter.CENTER, window=viewImages,
                                  height=70, width=290)

mainWindow.mainloop()
