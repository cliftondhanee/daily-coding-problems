def get_lowest_positive_int(array):
    array.sort()
    result = 1
    if max(array) <= 0:
        return result

    while True:
        if result not in array:
            return result
        else:
            result = result + 1

