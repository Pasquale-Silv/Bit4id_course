if(not(0)):                              # not(False) is True
    print("avvia l'exit()")
    exit((-3) ** 4)                      # l'exit(-1) viene beccato con tutti i numeri, non solo con -1
else:
    print("L'exit() non viene toccato!")

print("Se exit(-1) viene beccato, non vedrò mai la luce!")
