n = int(input("_gram? - "))
s = input("words: ")

grams = []

for i in range(len(s)):
    op = ""
    for x in range(i, i + n):
        if x >= len(s):
            op = ""
            break
        op += s[x]
    if op != "":
        grams.append(op)
        print(op)

grams.sort()
print(grams)
