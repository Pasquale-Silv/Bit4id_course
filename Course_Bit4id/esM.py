# def my_str(num):
#     q = num
#     string_num = ''
#     while(q > 10):
#         string_num += q % 10
# str

def my_str(num):
    dict_num = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
    }
    return "".join([dict_num[i] for i in dict_num])

ss = my_str(3334)
print(ss)
print(type(ss))

def my_str2(num):
    list_ = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    