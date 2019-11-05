from Tkinter import *
from PIL import Image
from PIL import ImageTk
from checker import *
import tkFileDialog

# Initialization
pointer = 0
root = Tk()
n = Scale(root, from_ = 1, to = 10, orient = HORIZONTAL)
n.set(3)
mode = IntVar(root)
load()

def select_image():
    # Select image to be compared
    global panelA, panelB, path

    path = tkFileDialog.askopenfilename()
    if (len(path) > 0):
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        panelA.configure(image = image)
        panelA.image = image

def find_similar():
    # Finding images that are similar, using the compare function (euclidean distance or cosine similarity)
    global path, res, pointer
    print(path, mode.get(), n.get())
    res = compareImage(path, mode.get(), n.get())
    pointer = 0
    print(res)
    display_result()
    return pointer

def display_result():
    # Displaying results
    global res, pointer, panelB
    image = cv2.imread(res[pointer])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    
    panelB.configure(image = image)
    panelB.image = image
    counter.config(text = str(pointer + 1))
    return pointer

def decrease_pointer():
    # Decrease pointer, will normalize if out of bounds
    global pointer
    pointer -= 1
    if (pointer < 0):
        pointer += n.get()
    if (pointer >= n.get()):
        pointer -= n.get()
    display_result()
    counter.config(text = str(pointer + 1))
    return pointer

def increase_pointer():
    # Increase pointer, will normalize if out of bounds
    global pointer
    pointer += 1
    if (pointer < 0):
        pointer += n.get()
    if (pointer >= n.get()):
        pointer -= n.get()
    display_result()
    counter.config(text = str(pointer + 1))
    return pointer

# Set default black colour to both panels
black = cv2.imread('black.jpg')
black = Image.fromarray(black)
black = ImageTk.PhotoImage(black)
panelA = Label(image = black)
panelA.image = black
panelA.pack(side = "left", padx = 10, pady = 10)
panelB = Label(image = black)
panelB.image = black
panelB.pack(side = "left", padx = 10, pady = 10)

# Navigation buttons
navFrame = Frame(root)
navFrame.pack(side = "bottom")
leftButton = Button(navFrame, text = "<", command = decrease_pointer)
leftButton.pack(side = "left")
counter = Label(navFrame)
counter.config(text = str(pointer + 1))
counter.pack(side = "left")
rightButton = Button(navFrame, text = ">", command = increase_pointer)
rightButton.pack(side = "left")

# Mode selection
radioGroup = LabelFrame(root, text = "Choose mode")
radioGroup.pack()
mode0 = Radiobutton(radioGroup, text = "Euclidean Distance", variable = mode, value = 0)
mode0.pack(anchor = W)
mode1 = Radiobutton(radioGroup, text = "Cosine Similarity", variable = mode, value = 1)
mode1.pack(anchor = W)

# Slider for n (number of similar images to display)
n.pack()

# Calculate and image select button
btn = Button(root, text = "Calculate!", command = find_similar)
btn.pack(side = "top", fill = "both", expand = "yes", padx = "10", pady = "10")

btn = Button(root, text = "Select an image", command = select_image)
btn.pack(side = "bottom", fill = "both", expand = "yes", padx = "10", pady = "10")

root.mainloop()