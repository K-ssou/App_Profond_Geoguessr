import os
from PIL import Image
import os
import sys
from datetime import datetime

for image_file_name in os.listdir('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\images\\Tokyo\\'):

    name, other = image_file_name.split(".")
    im = Image.open('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\images\\Tokyo\\'+image_file_name)
    new_width  = 150
    new_height = 150
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    im.save('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\images\\Tokyo_resize\\' + name + '.tif')

print("All done")