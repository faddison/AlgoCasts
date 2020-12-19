def selection(arr):
    sorted = []
    for i in range(0, len(arr)):
        min = None
        minj = 0
        for j in range(0, len(arr)):
            x = arr[j]
            if min == None or x <= min:
                min = x
                minj = j
        sorted.append(min)
        arr = arr[0:minj]+arr[minj]

        