import time, math

def judge_stupid(n):
    if n <= 1: return False
    if n == 2: return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def judge_root(n):
    if n <= 1: return False
    if n == 2: return True
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def judge_root_clev(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

judges = [judge_stupid, judge_root, judge_root_clev]
results = []
if __name__ == '__main__':
    for judge in judges:
        start = time.time()
        lis = []
        for i in range(1,1001):
            lis.append(judge(i))
        results.append(lis)
        print(f"[{judge.__name__}]elapsed: {time.time() - start} Correct:{results[0]==results[-1]}")

