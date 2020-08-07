def has_negatives(a):
    
    cache = {}
    result = []

    # loop through given list
    for num in a:
        # if it's not in cache, and it's not 0 (range uses 0 and it counts itself as a pos and a neg)
        if num not in cache and num != 0:
            # add to cache
            cache[num] = num
            # check if the neg of num is in cache
            if -num in cache:
                # add it to results (abs so it is positive)
                result.append(abs(num))

    return result


if __name__ == "__main__":
    a = list(range(500))
    a += [-1,-2,-3]
    print(has_negatives(a))