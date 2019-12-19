def test():
    return "Hello" + msg

def main():
    global msg
    msg = input()
    rtn = test()
    print(rtn)

main()
