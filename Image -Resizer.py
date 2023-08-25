
# import required module
import os
from PIL import Image

# assign directory
# use use Extra Backslash to escape it 
# Directory Path Example: 'C:\\foldername\\foldername2'
directory = 'DirectoryPath'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        image = Image.open(f)
        image.thumbnail((1920, 1080)) # new image dimesion to downsize image (width, heigth)
        image.save(f)
        print(image.size) # Output: (1920, 1080)