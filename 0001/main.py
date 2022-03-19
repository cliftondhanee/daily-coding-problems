def check_sum(array, k):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                if (array[i] + array[j]) == k:
                    return True
    return False
