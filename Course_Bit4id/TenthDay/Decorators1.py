def decor(func):
    def funcInterna():
        print("---------------------------")
        func()
        print("---------------------------")
    return funcInterna()

@decor
def funcDecorata():
    print("Salve signor Pasquale")

funcDecorata
