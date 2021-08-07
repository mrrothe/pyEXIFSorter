from exif import Image
import os
import datetime

directory = r'C:\Users\a'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        with open(os.path.join(directory, filename), "rb") as image_file:
            my_image = Image(image_file)
        image_taken= datetime.datetime.strptime(my_image.datetime_original, '%Y:%m:%d %H:%M:%S')
        if "canon" in (my_image.make).lower():
            newfilename = f'c:\\temp\photos\canon\{image_taken.year}\{image_taken.month}\{filename}'
        else:
            newfilename = f'c:\\temp\photos\{image_taken.year}\{image_taken.month}\{filename}'
        if os.path.isfile(newfilename):
            print("File already Exists: " + newfilename)
        else:
            print("Moving " + os.path.join(directory, filename) + " to " + newfilename)
#            os.path.join(*filename.split("\\")[:-1])
#            os.makedirs(os.path.dirname(newfilename)    , exist_ok=True)
#            os.rename(os.path.join(directory, filename), newfilename)
    else:
        continue
