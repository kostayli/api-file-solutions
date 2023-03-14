import os

path = "gaga.txt"
path_dirname = path.split('/')
print(path_dirname)
for i in path_dirname:
    if i.__contains__('.'):
        path_dirname.remove(i)
if not os.path.exists('/'.join(path_dirname)) and len(path_dirname) != 0:
    os.makedirs('/'.join(path_dirname))
