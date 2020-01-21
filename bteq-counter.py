import os
cor = 0
wro = 0
win = 3
i = ""
memo = []
while i != "q":
    i = input()
    os.system("cls")
    if i == "o":
        cor += 1
        if cor >= win:
            win += 1
            cor = 0
            print(f"Win!! Next Norma->{win}")
            continue
    elif i == "o-":
        cor -= 1
    elif i == "x":
        wro += 1
    elif i == "x-":
        wro -= 1
    elif i == "w":
        win += 1
    elif i == "w-":
        win -= 1
    elif i == "r":
        cor = 0
    elif i == "wr":
        win = 0
    elif i.startswith("w:"):
        memo.append(i[2:])
    for m in memo:
        print(m)
    print(f"Now status > {cor} / {win}")


