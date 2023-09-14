def multi(base:int, power:int, mod:int):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        result = multi(base, power // 2, mod)
        result = (result ** 2) * (base if power % 2 else 1) % mod
        return result

base, power, mod = map(int, input().split())

print(multi(base, power, mod) % mod)