import os
from PIL import Image
import os
import sys
from datetime import datetime

for image_file_name in os.listdir('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\Images\\'):

    name, other = image_file_name.split(".")
    im = Image.open('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\Images\\'+image_file_name)
    new_width  = 300
    new_height = 300
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    im.save('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\Images_Resize\\' + name +'_resize' + '.tif')

print("All done")