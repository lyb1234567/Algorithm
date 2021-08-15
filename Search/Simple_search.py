def simple_search(lst,target):
    for i in range(len(lst)):
        if lst[i]==target:
            return i
    return -1

if  __name__== "__main__":
    lst=[1,6,7,2,8,9]
    target=9
    lst.sort()
    print(simple_search(lst,target))