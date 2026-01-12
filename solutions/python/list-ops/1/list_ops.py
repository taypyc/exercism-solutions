def append(list1, list2):
    result = list1[:]
    for item in list2:
        result += [item]
    return result

def concat(lists):
    result = []
    for sublist in lists:
        for item in sublist:
            result += [item]
    return result

def filter(predicate, list):
    result = []
    for item in list:
        if predicate(item):
            result += [item]
    return result

def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result

def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc

def foldr(function, list, initial):
    acc = initial
    for item in reverse(list):
        acc = function(acc, item)
    return acc

def reverse(list):
    result = []
    for item in list:
        result = [item] + result
    return result