import os

import uuid



filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path = "/images/textbook/"
filepath += path

print(filepath)

counter = 1
for filename in os.listdir(filepath):
    
    old_file = os.path.join(filepath, filename)
    
    
    myuuid = uuid.uuid4()
    myuuid = ''.join(str(myuuid).split('-'))

    new_file = os.path.join(filepath, myuuid + "-1" + "-" + str(counter) + ".png")


    os.rename(old_file, new_file)
    counter+= 1