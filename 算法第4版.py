#!/usr/bin/python
# -*- coding: utf-8 -*-

from TestCase import sorted_nums, random_nums



# # 插入排序
# class Insertion:
#     @staticmethod
#     def sort(a):
#         length = len(a)
#         i = 1
#         while i < length:
#             j = i
#             while j > 0 and a[j] < a[j-1]:
#                 a[j], a[j-1] = a[j-1], a[j]
#                 j -= 1
#             i += 1
#
#
# # 调用demo
# random_nums = [4, 2, 1, 0, 94]
# Insertion.sort(random_nums)
# print(random_nums)

# # 选择排序 O(n²)
# class Selection:
#     @staticmethod
#     def sort(a):
#         length = len(a)
#         for i in range(length):
#             min_idx = i
#             for j in range(i+1, length, 1):
#                 if a[j] < a[min_idx]:
#                     min_idx = j
#             a[i], a[min_idx] = a[min_idx], a[i]
#         return a
#
# random_nums = [5, 2, 8, 5, 0, 1]
# Selection.sort(random_nums)
# print(random_nums)

# # 二分查找 O(log2n)
# class BinarySearch:
#     @staticmethod
#     def rank(key, a):
#         lo, hi = 0, len(a)+1
#         while lo <= hi:
#             mid = lo + (hi - lo) // 2
#             if key < a[mid]:
#                 hi = mid - 1
#             elif key > a[mid]:
#                 lo = mid + 1
#             else:
#                 return mid
#         return -1
#
#
# if __name__ == "__main__":
#     sorted_nums = [1, 5, 8, 9, 10]
#     print(BinarySearch.rank(9, sorted_nums))


