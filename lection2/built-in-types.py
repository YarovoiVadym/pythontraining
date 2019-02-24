import random

arr = []
length = int(input())
i = 0

while i < length:
    arr.append(int(random.random() * 100))
    i += 1

arrSum = sum(arr)
arrAverage = arrSum / length

print('list -', arr)
print('sum of list elements -', arrSum)
print('average of list elements -', arrAverage)
