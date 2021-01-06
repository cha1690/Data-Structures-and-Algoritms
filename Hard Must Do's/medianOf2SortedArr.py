def median(arr1,arr2):
    '''

    :param arr1: [1 6 | 7 8 9]
    :param arr2: [12 14 | 15 18]
    :return:
    '''

    if len(arr2)< len(arr1):
        return median(arr2,arr1)

    lo, hi = 0, len(arr1)

    while lo<=hi:
        div_arr1= (lo+hi)//2
        div_arr2= (len(arr1)+len(arr2)) - div_arr1

        left_arr1= arr1[div_arr1-1] if div_arr1 > 0 else float(-'inf')
        right_arr1= arr1[div_arr1] if div_arr1 != len(arr1) else float('inf')
        left_arr2= arr2[div_arr1-1] if div_arr1 > 0 else float(-'inf')
        right_arr2= arr1[div_arr2] if div_arr1 != len(arr2) else float('inf')

        if left_arr1 <= right_arr2 and left_arr2 <= right_arr1:
            if len(arr1)+len(arr2) % 2:
                return min(right_arr1, right_arr2)
            else:
                return (max(left_arr1, left_arr2) + min(right_arr1, right_arr2)) / 2

        elif left_arr1 > right_arr2:
            hi = div_arr1-1
        else:
            lo = div_arr1+1
