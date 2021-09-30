import zipfile
with zipfile.ZipFile('main.zip') as my_zip:
    my_zip.extractall('.')

import os, glob
with open("answ3.txt", 'a') as f:
    for root, dirs, files in os.walk('main'):
        for file in files:
            if file.endswith(".py"):
                f.write('{}\n'.format(root))


