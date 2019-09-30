import os, zipfile

path = os.getcwd()

print(path)

list = []

for root, dirs, files in os.walk(path):
    for name in files:
        if '.zip' in name:
            list.append(os.path.join(root, name))

for item in list:
    fileName = os.path.basename(item)
    dirName = os.path.dirname(item)
    folder = os.path.join(dirName, fileName[:-4])
    zip_ref = zipfile.ZipFile(item)
    zip_ref.extractall(folder)
    zip_ref.close()