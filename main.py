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
if counter == 1:
    result.append([nxt, 1])
elif counter > 1:
    result.append([nxt, counter])
print(result)
