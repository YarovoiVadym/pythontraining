import random


def create_random_array():
    tempArr = []
    length = int(input())
    i = 0

    while i < length:
        tempArr.append(int(random.random() * 100))
        i += 1

    return tempArr


def get_sum_of_array(array):
    sum = 0

    for item in array:
        sum += item

    return sum


def get_average_of_array(array):
    return get_sum_of_array(array) / len(array)


arr = create_random_array()
arrSum = get_sum_of_array(arr)
arrAverage = get_average_of_array(arr)

print('list -', arr)
print('sum of list elements -', arrSum)
print('average of list elements -', arrAverage)
