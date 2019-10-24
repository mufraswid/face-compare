from pathlib import Path
import os

pathlist = Path("").glob('**/*.jpg')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)
    commandString = "magick \"" + path_in_str + "\" -trim -resize 299x299^ -extent 299x299 -gravity center \"" + path_in_str + "\""
    os.system('cmd /c ' + commandString)