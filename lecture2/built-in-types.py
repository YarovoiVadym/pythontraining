import random

arr = []
arrSum = 0
length = int(input())
i = 0

while i < length:
    arr.append(int(random.random() * 100))

    arrSum += arr[i]

    i += 1

arrAverage = arrSum / length

print('list -', arr)
print('sum of list elements -', arrSum)
print('average of list elements -', arrAverage)
