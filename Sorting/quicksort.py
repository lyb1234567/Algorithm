"""
首先确定一个分界值，然后建立两个空列表，分别放在左边和右边。将大的往右边放，小的往左边放。然后每轮各自对左边和右边的列表进行自我排序，
每个列表小于0是递归自动就停止。
理想状况下为O(nlogn)
"""
def quick_sort(lst):
    if len(lst)>=2:
        left,right=[],[]
        key=lst[0]
        lst.remove(key)
        for num in lst:
            if key<num:
                right.append(num)
            elif key>num:
                left.append(num)
        return quick_sort(left)+[key]+quick_sort(right)

    else:
        return lst

if __name__=="__main__":
    lst=[2,3,4,1,7,6,8,9,12]
    quick_sort(lst)