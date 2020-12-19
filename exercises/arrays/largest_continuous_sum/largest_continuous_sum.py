def largest_continuous_sum(arr):
    # brute force n^3
    max = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)+1-i):
            sum = 0
            if i == j:
                sum = arr[i]
            else:
                for k in range(i,j):
                    sum = sum + arr[k]
            if sum > max:
                max = sum
    return max

# 14:32 done 3/4
# 27:00 4/4 boundary case on for k loop
            

