import image_slicer
import os
import sys
import shutil
import uuid

# generate a random name for folder
folder = str(uuid.uuid4().hex)

# make 2 folder 1) source folder 2) raw folder for original PNG file
os.mkdir(str(folder))
os.mkdir(str(folder) + "/raw/")

# move PNG file in to random folder
shutil.move(sys.argv[1], str(folder))

# slice PNG file in * image
image_slicer.slice(str(folder) + '/'+sys.argv[1], int(sys.argv[2]))

# move PNG file in  to raw folder
shutil.move(str(folder) + '/'+sys.argv[1], str(folder) + '/raw/')
