#https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
def binary_array_to_number(arr):
    joined_number = ''.join(map(str, arr))
    return int(joined_number, 2)

print(binary_array_to_number([1, 1, 0, 0, 0, 0, 0, 1,1,1,0]))

