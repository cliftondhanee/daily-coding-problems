def get_product(array):
    if len(array) == 1:
        return None

    result =[1] * len(array)
    product = 1
    for i in range(len(array)):
        for j in range(len(result)):
            if i != j:
                product = product * array[j]
        result[i] = product
        product = 1
    return result
