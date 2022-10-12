# use PIP install rembg before using
# use PIP install tkinter before using

import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from rembg import remove
from PIL import Image
import os.path
from sys import exit


def Main():
    try:
        input_path = GetInputFile()
        if input_path == '':
            exit()
        output_path = input_path[:str.rindex(input_path, '.')] + '_output.png'
        RemoveBackground(input_path, output_path)
        if os.path.isfile(output_path):
            print('************* Operation successful!')
            print('************* Output directory:')
            print('************* ' +
                  output_path[:str.rindex(output_path, '/')])
            print('************* File name:')
            print('************* ' +
                  output_path[str.rindex(output_path, '/')+1:])
    except FileNotFoundError:
        print('Input file ' + input_path + ' not found!')
    except Exception as e:
        if e.__cause__ == 'RGBA':
            print(
                "Please change extension of your output file. Acceptable format is png.")
        else:
            print(e.args)
            print(e)


def RemoveBackground(input_path, output_path):
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)


def GetInputFile():
    response = False
    while response == False:
        root = Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(
            initialdir="/", title="Remove background from image : Select file to edit", filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg"), ("ICON", "*.ico"), ("ALL", '*.*')])
        if not root.filename:
            response = tkinter.messagebox.askyesno(
                "No file selected", "Do you want to quit?")
            if response:
                exit()
        else:
            response = True
    return root.filename


Main()
