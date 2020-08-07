def finder(files, queries):
    
    cache = {}
    result = []

    # for each of the paths
    for path in files:
        # split the path so you have just the file name
        name = path.split('/')[-1]
        if name not in cache:
            # add the file name as the key to the cache and the whole path and the value
            cache[name] = [path] 
        else:
            # if the key is already there, add another path to key
            cache[name].append(path)

    # is what we are looking for in the cache
    for query in queries:
        if query in cache:
            # go through each spot in case there were multiple paths for the file name
            for path in cache[query]:
                # add each path to the result
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo.txt',
        '/bin/bar.txt',
        '/usr/bin/baz.txt',
        '/usr/local/share/foo.txt',
        '/usr/bin/ls',
        '/home/davidlightman/foo.txt',
        '/bin/su'
    ]
    queries = [
        'foo.txt',
        'qux.txt',
        'baz.txt',
        'ls',
        'nosuchfile.txt'
    ]
    print(finder(files, queries))
