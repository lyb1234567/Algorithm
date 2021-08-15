"""
首先从待排序的列表中，遍历一边列表，从当前元素后面开始遍历，找寻到最小数，并记录索引，在每一回合结束后，最小数索引去和最开始第一个数进行比较，假如索引未曾发生变化，那么继续从下一个数后面
开始遍历一次类推，否则就交换。当所有数进行排序完成之后，列表也就排序完成了
最坏情况下为O(N^2)
"""
def selection_srot(nums):
    for i in range(len(nums)):
        min_index=i
        # 找出最小数
        for j in range(i+1,len(nums)):
            if nums[j]<=nums[min_index]:
                min_index=j
        #         如果与原先初始的最小索引一致，那么不发生变化，否则直接交换
        if i!= min_index:
            nums[i],nums[min_index]=nums[min_index],nums[i]

    return nums

if __name__=="__main__":
    nums=[3,6,8,7,4]
    print(selection_srot(nums))