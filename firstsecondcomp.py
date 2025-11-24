from operator import truediv

nums_x = [1, 5, 2, 4, 1, 2, 1]
nums_y = [1, 2, 3, 4, 5, 6, 7]

def comp(nums):
    print("zadani: ", nums)

    first = nums[0]
    last = nums[-1]

    if first == last:
        return True
    else:
        return False
print("rezultat: ", comp(nums_x))
print("rezultat: ", comp(nums_y))



