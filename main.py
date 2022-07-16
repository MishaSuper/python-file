# напиши код под задачку:какле количество повторяющихся элементов и каких)

arr = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0]

result = []

i = 0
prev = arr[i]
i += 1
counter = 1
while i != len(arr):
    nxt = arr[i]

    if nxt != prev:
        result.append([prev, counter])
        counter = 1
    else:
        counter += 1
    prev = nxt
    i += 1
if arr[-2] != nxt:
    result.append([nxt, 1])
print(result)
