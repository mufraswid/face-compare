import os, sys
from Tkinter import *
from PIL import Image
from PIL import ImageTk

def button_click_exit_mainloop (event):
    event.widget.quit() # this will cause mainloop to unblock.

root = Tk()

f = 'title.jpg'
image1 = Image.open(f)
image1 = image1.resize((600, 500), Image.ANTIALIAS)
root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
tkpi = ImageTk.PhotoImage(image1)
label_image = Label(root, image=tkpi)
label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])

windowWidth = image1.size[0]
windowHeight = image1.size[1]

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))


root.overrideredirect(1)
root.after(2125, lambda: root.destroy())
root.mainloop()