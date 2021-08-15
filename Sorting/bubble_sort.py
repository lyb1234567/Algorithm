import random
"""
冒泡排序，每个元素每一轮遍历之中两两比较，进行交换，复杂度为O(N^2)
"""
def bubble(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
    return lst

if __name__=="__main__":
    lst=[]
    for i in range(100):
        lst.append(random.randint(1,100))
    print(bubble(lst))