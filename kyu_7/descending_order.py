#Input: 42145 Output: 54421
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


print(descending_order(84913040596))