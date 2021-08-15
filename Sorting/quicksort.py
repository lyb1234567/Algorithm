def quick_sort(lst):
    if len(lst)>=2:
        left,right=[],[]
        key=lst[0]
        lst.remove(key)
        for num in lst:
            if key>num:
                right.append(num)
            elif key<num:
                left.append(num)
        return quick_sort(right)+[key]+quick_sort(left)

    else:
        return lst
