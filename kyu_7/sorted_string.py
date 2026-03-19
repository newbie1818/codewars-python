#https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
def longest(a1, a2):
    # new combined string
    combined = a1 + a2

    # check distinct letters
    new_set = set(combined)

    # sort alphabetically ascending
    new_set_sorted = sorted(new_set)
    return ''.join(new_set_sorted)


print(longest('wkwjffopnannnnaopqfghel', 'kkalwmd'))
