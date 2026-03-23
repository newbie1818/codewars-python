#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
'''Given a random non-negative number,
you have to return the digits of this number within an array in reverse order.'''
#convert to str
#iterate over each element with for loop
#append to new list
#convert to int
#reverse order
def digitize(n):
    new_list = []
    for i in str(n):
        new_list.append(int(i))
    new_list.reverse()
    print(new_list)


digitize(8467290012)