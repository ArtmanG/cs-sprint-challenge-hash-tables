def get_indices_of_item_weights(weights, length, limit):
    # create a cache
    cache = {}

    if len(weights) < 2:
        return None

    # index of weights stores as values in cache, start at index 0 with index counter
    index = 0
    # loop through array of weights
    for weight in weights:
        # look for (limit - weight) in cache
        if (limit - weight) in cache:
            # if found return the index we are on, the index of the other weight 
            return(index, cache[(limit - weight)])
        #if not in cache, add the weight:index (key:value) pair to the cache
        cache[weight] = index
        # move on to next index
        index += 1

# testing for myself
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
get_indices_of_item_weights(weights_4, 9, 7)