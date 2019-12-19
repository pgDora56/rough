import pathlib

path  = pathlib.Path("nhigh.jpg")
print(path.suffix)

flag = True
while flag:
    ipt = input("Continue?[Y/n] :")
    flag = not ipt.lower() in ["y", "yes"]


