def deco(func): # funcの中にラップした関数全体が入るイメージ
    def wrapper(*args, **kwargs):
        print("--start--")
        func(*args, **kwargs)
        print("--end--")
    return wrapper

@deco
def test(x):
    i = input()
    print(i + x)

test("ABC")
test("DEF")
