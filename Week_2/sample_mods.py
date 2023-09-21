## Calculate the length of a iterable object
def calc_len(x):
    length = 0
    for i in x:
        length += 1
    return length


## print(calc_len([14, 19, 7, 13, 19, 6, 4, 19, 16, 19]))


## Create a set from a object
def make_set(y):
    good_set = []
    for n in y:
        if n not in good_set:
            good_set.append(n)
    return good_set


## print(make_set([24, 61, 4, 35, 32, 83, 38, 33, 40, 24]))
## print(len(make_set([24, 61, 4, 35, 32, 83, 38, 33, 40, 24])))

## Create a range function with start, stop, and step


def custom_range(stop, start=0, step=1):
    range_list = [start]
    while start + step < stop:
        start += step
        range_list.append(start)
    return range_list


##print(custom_range(6, 1, 2))
