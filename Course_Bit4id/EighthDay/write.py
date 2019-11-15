with open('fileNuovo.txt', 'w') as file:
    for i in range(10):
        line = 'Line' + str(i) + '\n'
        file.write(line)

    file.writelines("appeso")
    file.writelines("\nUn'altra riga appesa")
    file.writelines("\n\ne ancora un'altra riga appesa!")
