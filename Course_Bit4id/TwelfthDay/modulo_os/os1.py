# Il modulo os è utile per manipolare directories, files e processi.
# ~

import os

# os.path

path1 = os.path.join("C:\\Users\\Student-004\\Desktop")               # \\
print(path1)
path2 = os.path.join("C:/Users/Student-004/Desktop")                  # /
print(path2)

print("\nos.path.expanduser:")
print(os.path.expanduser("~"))                                # 'tilde' per visualizzare la home directory.
home_dir = os.path.expanduser("~")

print(os.listdir(home_dir))
print(os.listdir(path1))
print(os.listdir(path2))
