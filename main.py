#!/usr/bin/python3

import tkinter as tk
from snownlp import SnowNLP
from utils import download_moving, save_result


def _download_moving():
    cookies = e.get()
    download_moving(cookies)
    e.delete(0, 'end')
    e.insert(0, 'please copy you cookie')


def analyse_moving():
    global image_file
    sentence = e.get()
    path = './results/moving.png'
    save_result(qq_msgs='./inputs/msgs.txt', path=path)
    image_file = tk.PhotoImage(file=path)
    canvas.itemconfig(image, image=image_file)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('emotion judge')
    window.geometry('800x600')

    e = tk.Entry(window, width=60)
    e.insert(0, 'please copy you cookie')
    e.grid(row=0, column=0, columnspan=2)

    b = tk.Button(window, text='get moving', width=20,
                  height=3, command=_download_moving)
    b.grid(row=1, column=0)

    b1 = tk.Button(window, text='analyse', width=20,
                   height=3, command=analyse_moving)
    b1.grid(row=1, column=1)
    canvas = tk.Canvas(window, height=500, width=700)
    image_file = tk.PhotoImage(file='./welcome.gif')
    image = canvas.create_image(0, 0, anchor="nw", image=image_file)
    canvas.grid(row=5, column=0, columnspan=2)

    window.mainloop()
