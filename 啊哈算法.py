#!/usr/bin/python
# -*- coding: UTF-8 -*-
from TestCase import random_nums


# # 冒泡排序
# def bubble_sort(a):
#     length = len(a)
#     for i in range(length):
#         for j in range(0, length-1-i, 1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#
#
# a = [5, 2, 1, 9]
# bubble_sort(a)
# print(a)


# 快速排序
def quick_sort(a, left, right):
    if left > right:
        return
    i, j = left, right
    # temp中存的就是基准数
    temp = a[left]
    while i != j:
        # 顺序很重要，要先从右往左找
        while a[j] >= temp and i < j:
            j -= 1
        while a[i] <= temp and i < j:
            i += 1
        # 交换两个数在数组的位置
        # 当哨兵i和哨兵j没有相遇时
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[left] = a[i]
    a[i] = temp
    # 继续处理左边的，这里是一个递归的过程
    quick_sort(a, left, i-1)
    # 继续处理右边的，这里是一个递归的过程
    quick_sort(a, i+1, right)
    return


a = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
quick_sort(a, 0, len(a)-1)
print(a)
