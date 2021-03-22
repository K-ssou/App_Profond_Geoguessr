import os
from PIL import Image
import os
import sys
from datetime import datetime

cpt = 1
for image_file_name in os.listdir('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\images\\Paris'):

    im = Image.open('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\images\\Paris\\'+image_file_name)
    new_width  = 150
    new_height = 150
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    im.save('C:\\Users\\Cassandra\\Desktop\\cours\\2A\\App_Profond\\Projet\\App_Profond_Geoguessr\\Images_resize\\Paris\\' + 'Paris_' +str(cpt) + '.tif')
    cpt +=1

print("All done")
print(str(cpt-1))