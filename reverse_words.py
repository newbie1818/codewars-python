#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(text):
    new_text = text.split(" ")
    reversed_word = [i [::-1] for i in new_text]
    return ' '.join(reversed_word)
print(reverse_words(" This is an example! "))