def intersection(arrays):

    master = []
    cache = {}
    result = []

    # create one array with from all the arrays given
    for arr in arrays:
        master.extend(arr)
    # loop through all numbers
    for num in master:
        # if it's in the cache
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1

        # the numbers we are looking for will equal as many lists as we have, thats the overlap
        if cache[num] >= len(arrays):
            result.append(num)
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
