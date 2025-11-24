# ord() function converts a character into its ASCII notation and chr() converts the ASCII to character.
#print(chr(ord('A')))

#li = ['a', 'b', 'c', 'd']
#print("".join(li))
#abcd

#lambda
# y = 8
# z = lambda x : x * y
#  print(z(6))
# 48 (Lambda multiplies input by outer scope variable y = 8, so z(6) is 6*8 = 48.)

#When a function is defined inside a class then it is called Method.
#The method is accessible to data that is contained within the class.

#def func(a, b=[]):
#    b.append(a)
#    return b
#print(func(1))
#print(func(2))
#[1], [1,2]
# -----In Python, default mutable arguments like lists retain their state across function calls. The list b is initialized only once when the function is defined, not each time it's called. Therefore:
#
# func(1) appends 1 to the default list b, resulting in [1].
# func(2) appends 2 to the same list b, which already contains [1], resulting in [1, 2].
# This behavior can lead to unexpected results if not carefully managed. To avoid this, it's common practice to use None as the default value and initialize the list inside the function:
# def func(a, b=None):
#     b.append(a)
#     return b

#Suppose li is [3, 4, 5, 20, 5, 25, 1, 3], what is li after li.pop(1)?
#[3, 5, 20, 5, 25, 1, 3]
#pop(i) removes ith index el from the list

