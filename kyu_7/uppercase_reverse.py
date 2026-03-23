'''напиши функцию, которая принимает список слов и возвращает
новый список где каждое слово написано заглавными буквами, в обратном порядке.'''

def uppercase_reverse(word_list):

    new_list = [i.upper() for i in word_list][::-1]
    return new_list


print(uppercase_reverse(["hello", "world", "python"]))