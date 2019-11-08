def remove_symbol(symbol_passed, string_passed):
    index = string_passed.find(symbol_passed)
    if 0 < index < len(string_passed) - 1:
        string_passed = string_passed[0:index] + string_passed[index + 1:]
        return string_passed

    elif index == 0:
        string_passed = string_passed[1:]
        return string_passed

    elif index == len(string_passed) - 1:
        string_passed = string_passed[0:index]
        return string_passed


def remove_numbers(p_string):
    # code here
    p_string


str1 = 'This gets the car from 0 to 60 miles per hour (that is, to 97 kilometers per hour) in 3.2 seconds.'
str1 = str1.split()
string_arr = []
for word in str1:
    while '(' in word or ')' in word or '[' in word or ']' in word or '.' in word or '\"' in word or ',' in word:
        if '(' in word:
            word = remove_symbol('(', word).upper()

        elif ')' in word:
            word = remove_symbol(')', word).upper()

        elif '[' in word:
            word = remove_symbol('[', word).upper()

        elif ']' in word:
            word = remove_symbol(']', word).upper()

        elif ',' in word:
            word = remove_symbol(',', word).upper()

        elif '.' in word:
            word = remove_symbol('.', word).upper()

        elif '\"' in word:
            word = remove_symbol('\"', word).upper()

    string_arr.append(word.upper())

print(string_arr)

