# *args       ------->   tuple
# **kwargs    ------->   dict

def example_function(arg_1, arg_2, **kwargs):
    "Usa il **kwargs per collezionare diversi parametri!"
    print(arg_1)
    print(arg_2)
    for key, value in kwargs.items():
        print('arg_3kwargs value:', value)
        print("kwargs[{}] = {}".format(key, kwargs[key]))

example_function(1, 20, nome="Pasquale", cognome='Silvestre', età=23)

help(example_function)
