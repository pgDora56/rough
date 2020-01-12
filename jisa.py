import datetime as dt
import random
import locale
locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

class mydt:
    def __init__(self, month, day, hour):
        self.dt = dt.date(2018, month, day)
        self.h = hour

    def __str__(self):
        res = f"{self.dt.month}月{self.dt.day}日"
        if self.h < 12:
            res += f"午前{self.h}時"
        else:
            res += f"午後{self.h - 12}時"
        return res

    def __add__(self, v):
        return self.org_values(self.h + v, self.dt)

    def __sub__(self, v):
        return self.org_values(self.h - v, self.dt)

    def org_values(self, h, d):
        if h < 0:
            while h < 0:
                h += 24
                d -= dt.timedelta(days=1)
        elif h > 23:
            while h > 23:
                h -= 24
                d += dt.timedelta(days=1)
        return mydt(d.month, d.day, h)

def jisa(t1, t2):
    return int((t2-t1)/15)

def replace_all(text, lis):
    for l in lis:
        text = text.replace(l[0], str(l[1]))
    return text

def lat_print(num):
    op = "各地の緯度："
    for idx in range(num):
        if idx > 0: op += " / "
        if cities[idx][1] < 0:
            lat = f"西経{-1 * cities[idx][1]}度"
        else:
            lat = f"東経{cities[idx][1]}度"

        op += f"{cities[idx][0]}: {lat}"
    return op

class Qformat:
    def __init__(self, fmt, citnum, t2, t3, ans):
        self.format = fmt
        self.city_num = citnum
        self.cal_t2 = t2
        self.cal_t3 = t3
        self.cal_ans = ans
        # lambda t1, h1, h2, stay, c1, c2, c3: lambda-expression

    def make_question(self):
        random.shuffle(person)
        month = random.randint(1,12)
        if month in [1,3,5,7,8,10,12]:
             day = random.randint(1,31)
        elif month == 2:
             day = random.randint(1,20)
        else:
             day = random.randint(1,30)

        time = random.randint(0,23)

        random.shuffle(cities)

        t1 = mydt(month, day, time)
        h1 = random.randint(3,10)
        h2 = random.randint(3,10)
        stay = random.randint(10,24)
        t2 = self.cal_t2(t1, h1, h2, stay, cities[0][1], cities[1][1], cities[2][1])
        t3 = self.cal_t3(t1, h1, h2, stay, cities[0][1], cities[1][1], cities[2][1])
        # t2 = t1+h1+jisa(cities[0][1], cities[1][1])
        # t3 = t1+h1+stay+h2+jisa(cities[0][1],cities[2][1])

        rep_tuples = [
                ("{p}", person[0]),
                ("{p2}", person[1]),
                ("{1}", cities[0][0]),
                ("{2}", cities[1][0]),
                ("{3}", cities[2][0]),
                ("{t1}", t1),
                ("{t2}", t2),
                ("{t3}", t3),
                ("{h1}", h1),
                ("{h2}", h2),
                ("{stay}", stay)
                ]
        q_sent = replace_all(self.format, rep_tuples)

        print(q_sent)
        print(lat_print(self.city_num))
        return self.cal_ans(t1, h1, h2, stay, cities[0][1], cities[1][1], cities[2][1])

        # print(f"{cities[0][0]}{t1} + {h1}h -> {t1+h1} == {t1+h1+jisa(cities[0][1],cities[1][1])}")
        # print(f"{cities[1][0]}{t1+h1+jisa(cities[0][1],cities[1][1])} + {stay}h -> {t1+h1+jisa(cities[0][1],cities[1][1])+stay}")
        # print(f"{t1+h1+jisa(cities[0][1],cities[1][1])+stay} + {h2}h -> {t1+h1+jisa(cities[0][1],cities[1][1])+stay+h2}")
        # for elem in [person, cities,t1, t2,t3,h1,h2,stay]:
         #   print(elem)

cities = [["東京",135],
["ホノルル",-120],
["ニューヨーク",-75],
["シンガポール",105],
["マドリード",15],
["ロンドン",0],
["ヘルシンキ",30],
["モスクワ",45],
["パプアニューギニア",165],
["シドニー",150],
["北京",120],
["バングラデシュ",90],
["カザフスタン",75],
["ドバイ",60],
["グリーンランド",-15],
["リオデジャネイロ",-45],
["ベネズエラ",-60],
["フロリダ",-90],
["チワワ",-105],
["アラスカ",-135],
["ハワイ",-150],
["サモア",-165]]

formats = [
Qformat("{1}に住む{p}は、夏休みに{2}に行き、その後{3}へ向かいました。{p}を乗せた飛行機は{1}を{t1}に出発し、{2}の空港に現地時間の{t2}に到着しました。その{stay}時間後に{2}の空港を経ち、{3}に現地時間の{t3}に到着した。移動時間の合計を求めなさい。", 3,
lambda t1, h1, h2, stay, c1, c2, c3: t1+h1+jisa(c1, c2),
lambda t1, h1, h2, stay, c1, c2, c3: t1+h1+stay+h2+jisa(c1, c3),
lambda t1, h1, h2, stay, c1, c2, c3: h1+h2
),
Qformat("{1}に住む{p}は、{1}を{t1}に出発する{2}行きの飛行機に乗り、現地時間の{t2}に{2}に到着した。{p}が{1}から{2}まで飛行機に乗っていた時間は何時間か。", 2,
lambda t1, h1, h2, stay, c1, c2, c3: t1+h1+jisa(c1, c2),
lambda t1, h1, h2, stay, c1, c2, c3: 0,
lambda t1, h1, h2, stay, c1, c2, c3: h1
),
Qformat("{1}の空港を{t1}に出発した航空機が、{h1}時間後に{2}の空港に到着し、到着して{h2}時間してから{3}に電話を掛けた。このときの{3}の日時を答えなさい。", 3,
lambda t1, h1, h2, stay, c1, c2, c3: 0,
lambda t1, h1, h2, stay, c1, c2, c3: 0,
lambda t1, h1, h2, stay, c1, c2, c3: t1+h1+h2+jisa(c1,c3)
),
Qformat("{1}の空港を{t1}に出発した航空機はおよそ{h1}時間かかって{2}の空港に到着した。また、{3}の空港を現地時間の{t2}に出発した航空機は{h2}時間かかって{2}の空港に到着した。この２機が到着した時刻の時間差は何時間か答えなさい。", 3,
lambda t1, h1, h2, stay, c1, c2, c3: t1+h1+stay*random.choice([1,-1])-h2+jisa(c1,c3),
lambda t1, h1, h2, stay, c1, c2, c3: 0,
lambda t1, h1, h2, stay, c1, c2, c3: stay
),
Qformat("{1}に住む{p}は、{2}に住む{p2}と会い、その後{3}を訪れることにした。{p}は現地時間{t1}発の航空機で{1}の空港を出発し、{h1}時間掛けて{2}に到着した。{2}の空港で{p2}と会い、到着から{stay}時間後の航空機で{2}を出発、{h2}時間かけて{3}に到着した。{p}が{3}に到着した時刻は現地時間で何月何日の何時か。", 3,
lambda t1, h1, h2, stay, c1, c2, c3: 0,
lambda t1, h1, h2, stay, c1, c2, c3: 0,
lambda t1, h1, h2, stay, c1, c2, c3: t1+h1+stay+h2+jisa(c1,c3)
)
]

person = ["ももさん","天さん","椎菜さん","あきさん"]

answers = []
for i in range(100):
    print(f"\nQ{i+1}.")
    answers.append(formats[random.randint(0,4)].make_question())
print("\n")
for idx, ans in enumerate(answers):
    print(f"A{idx+1}. {ans}")

