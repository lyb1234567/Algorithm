def binary_search(lst,target):
    low=0
    high=len(lst)
    while(low<high):
        mid = (low + high) >> 1
        if target==lst[mid]:
            return mid
        elif target>lst[mid]:
            low=mid

        elif target<lst[mid]:
            high=mid
    return -1


if  __name__== "__main__":
    lst=[1,6,7,2,8,9]
    target=9
    lst.sort()
    print(binary_search(lst,target))