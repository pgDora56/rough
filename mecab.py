import MeCab, re

data = "私のお気に入りの楽曲は『フワリ、コロリ、カラン、コロン』です。"

m = MeCab.Tagger().parse(data)
lines = m.split("\n")
items = (re.split('[\t,]', line) for line in lines)

print(m)
for i in items:
    print(i)

