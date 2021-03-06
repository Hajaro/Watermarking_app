import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


# TODO watermark position
# TODO default watermark
# TODO gui


def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    #img_tk = ImageTk.PhotoImage(file=filename)
    img = Image.open(filename).convert("RGBA")


def upload_watermark():
    global watermark
    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    watermark = Image.open(filename).convert("RGBA")


def merge(img, watermark):
    width, height = img.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(img, (0, 0))
    watermark.putalpha(127)
    transparent.paste(watermark, (0, 0), mask=watermark)
    transparent.show()

# --------------UI-------------- #


window = tk.Tk()
window.title("Watermark your photo")
window.config(padx=25, pady=10)

my_font1=('times', 18, 'bold')
l1 = tk.ttk.Label(window, text='Add photo to watermark', width=30, font=my_font1)
l1.grid(row=1, column=1)


b1 = tk.ttk.Button(window, text='Upload File',
   width=20, command=lambda: upload_file())
b1.grid(row=2, column=0)


b2 = tk.ttk.Button(window, text='Upload Watermark',
   width=20, command=lambda: upload_watermark())
b2.grid(row=2, column=1)


b3 = tk.ttk.Button(window, text='Merge',
   width=20, command=lambda: merge(img=img, watermark=watermark))
b3.grid(row=2, column=2)


window.mainloop()
