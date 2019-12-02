digitList = [str(i) for i in range(0, 10)]
alphaList = [chr(i) for i in range(65, 91)]
full_list = digitList + alphaList

def sum(a, b, base):
    if (base > 36 or base < 2):
        return None
    new_l = full_list[0: base]
    return sumIntra(a, b, base, new_l)

def sumIntra(a, b, base, new_l):
    i1 = full_list.index(a)
    i2 = full_list.index(b)
    report = ""
    for i in range(i1):
        i2 += 1
        if i2 == len(new_l):
            i2 = 0
            report = "1"
    if report:
        return report + full_list[i2]
    else:
        return full_list[i2]


if __name__ == "__main__":
    print(digitList)
    print(digitList.index("7"))
    print(alphaList)
    print(full_list)
    print(full_list[24])
    print("base length:", len(full_list))
    print(full_list[9 + 8])                       # H