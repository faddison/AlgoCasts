# Given an integer array, output all the unique pairs that sum up to a specific value k.
def pair_sum(arr,k):
    pairs = []
    for i in range(0,len(arr)):    
        for j in range(i+1,len(arr)):
            ix = arr[i]
            jx = arr[j]
            if ix+jx == k:
                pair = [min(ix,jx),max(ix,jx)]
                if pair not in pairs:
                    pairs.append(pair)
    return len(pairs)

# 7:38 all pass