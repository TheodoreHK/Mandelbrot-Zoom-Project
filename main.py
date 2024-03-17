import MandelbrotMain
import tkinter as tk
import time as clock
import numpy as np
import imageio

root = tk.Tk()
root.title("Mandelbrot Visualizer")
root.geometry("560x350")


def create_clickbutton():
    global size
    global fps
    global seconds
    global a_c
    global b_c
    size = int(text.get())
    fps = int(fpsin.get())
    seconds = int(numsecs.get())
    a_c = float(a_coord.get())
    b_c = float(b_coord.get())
    if size > 512:
        errorSize()
    else:
        createVideo()


def errorSize():
    sizeerror = tk.Label(root, text="This size is quite large, this could take a while. Do you still want to continue?")
    sizeerror.place(x=44, y=275)
    sizeerror.configure(background="wheat2")
    confirm = tk.Button(root, text="Yes", command=createVideo)
    confirm.place(x=250, y=300)
    confirm.configure(highlightbackground="wheat2")


def createVideo():
    root.destroy()
    num_images = fps * seconds
    width = 3
    image_array = []
    for i in range(num_images):
        image_array.append(MandelbrotMain.make_image((a_c, b_c), width, size))
        width = 0.98*width
    imageio.mimsave("C:\\Users\\adamf\\Videos\\Mandelbrot\\fergusen.mp4", image_array, fps=fps)

    # MandelbrotMain.make_image((-0.75, 0), 3, size)


label = tk.Label(root, text="Please give the square pixel size of the image you would like generated")
label.place(x=60, y=20)

text = tk.Entry(root)
text.place(x=180, y=40)

labelfps = tk.Label(root, text="Preferred FPS")
labelfps.place(x=180, y=60)
labelfps.configure(background="wheat2")

fpsin = tk.Entry(root)
fpsin.place(x=180, y=80)
fpsin.configure(highlightbackground="wheat2")

secs = tk.Label(root, text="Specify the number of seconds")
secs.place(x=180, y=100)
secs.configure(background="wheat2")

numsecs = tk.Entry(root)
numsecs.place(x=180, y=120)
numsecs.configure(highlightbackground="wheat2")

alabel = tk.Label(root, text="A Coordinate")
alabel.place(x=180, y=140)
alabel.configure(background="wheat2")

a_coord = tk.Entry(root)
a_coord.place(x=180, y=160)
a_coord.configure(highlightbackground="wheat2")

blabel = tk.Label(root, text="B Coordinate")
blabel.place(x=180, y=180)
blabel.configure(background="wheat2")

b_coord = tk.Entry(root)
b_coord.place(x=180, y=200)
b_coord.configure(highlightbackground="wheat2")

button = tk.Button(root, text="Render", command=create_clickbutton)
button.place(x=240, y=230)

# label2 = tk.Label(root, text="(Please do not generate anything above 1024 square pixels)")
# label2.place(x=85, y = 120)


root.configure(bg="wheat2")
label.configure(background="wheat2")
button.configure(background="wheat2")
button.configure(highlightbackground="wheat2")
text.configure(highlightbackground="wheat2")
# label2.configure(background="wheat2")

root.mainloop()