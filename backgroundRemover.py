# use PIP install rembg before using
# use PIP install tkinter before using

from tkinter import *
from tkinter import filedialog
from rembg import remove
from PIL import Image
import os.path


def Main():
    try:
        input_path = GetInputFile()
        output_path = input_path[:str.rindex(input_path, '.')] + '_output.png'
        RemoveBackground(input_path, output_path)
        if not os.path.isfile(output_path):
            print('Operation unsuccessful!')
        else:
            print('Operation successful!')
    except FileNotFoundError:
        print('File ' + input_path + ' not found!')
    except Exception as e:
        if e.__cause__ == 'RGBA':
            print(
                "Please change extension of your output file. Acceptable format is png.")
        else:
            print(e.args)


def RemoveBackground(input_path, output_path):
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)


def GetInputFile():
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    return root.filename


Main()
