import random

"""
插入排序，遍历一个已知列表，没到一个元素，就与该元素前面的已经排序好的子列表进行查询，如果找到比自己小的，就将该元素与那个比自己大的元素进行替换
最坏情况为O(N^2)
"""
def insertion_sort_ascedning(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        # 从当前位置前面n-1个元素开始遍历，每当发现前面一个元素笔记大，那么就进行，直到前面的元素比自己小，然后跳出循环
        j=i-1
        while(j>=0 and lst[j]>key):
            lst[j+1]=lst[j]
            j=j-1
        # 在此插入迭代元素
        lst[j+1]=key
    return lst

def insertion_sort_descedning(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        # 从当前位置前面n-1个元素开始遍历，每当发现前面一个元素笔记大，那么就进行，直到前面的元素比自己小，然后跳出循环
        j=i-1
        while(j>=0 and lst[j]<key):
            lst[j+1]=lst[j]
            j=j-1
        # 在此插入迭代元素
        lst[j+1]=key
    return lst

if __name__=="__main__":
    lst=[]
    for i in range(10):
        lst.append(random.randint(1,10))
    print(insertion_sort_descedning(lst))
    print(insertion_sort_ascedning(lst))