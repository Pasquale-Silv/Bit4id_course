def words_to_marks(s):
    """
    If　a = 1, b = 2, c = 3 ... z = 26
    Then l + o + v + e = 54
    and f + r + i + e + n + d + s + h + i + p = 108
    So friendship is twice stronger than love :-)
    The input will always be in lowercase and never be empty.
    """
    dict_letters = {chr(i + 96):i for i in range(1, 27)}
    res = 0
    for letter in s:
        for k in dict_letters:
            if letter == k:
                res += dict_letters[k]
    return res

print(words_to_marks('attitude'))                        # 100
print(words_to_marks('friends'))                         # 75
print(words_to_marks('family'))                          # 66
print(words_to_marks('selfness'))                        # 99
print(words_to_marks('knowledge'))                       # 96
