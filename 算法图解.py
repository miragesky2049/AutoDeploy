#!/usr/bin/python
# -*- coding: UTF-8 -*-


# ##******************************************
# # 贪婪算法
# states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# stations = {}
# stations["kone"] = set(["id", "nv", "ut"])
# stations["ktwo"] = set(["wa", "id", "mt"])
# stations["kthree"] = set(["or", "nv", "ca"])
# stations["kfour"] = set(["nv", "ut"])
# stations["kfive"] = set(["ca", "az"])
# final_stations = set()
#
# def search(states_needed):
#     while states_needed:
#         best_statiion = None
#         states_covered = set()
#         for station, states_for_station in stations.items():
#             covered = states_needed & states_for_station
#             if len(covered) > len(states_covered):
#                 best_statiion = station
#                 states_covered = covered
#         states_needed -= states_covered
#         final_stations.add(best_statiion)
#
#
# search(states_needed)
# print(final_stations)


# ##******************************************
# # 狄克斯特拉算法
# graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
# graph["a"] = {}
# graph["a"]["fin"] = 1
# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5
# graph["fin"] = {}

# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity

# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None

# processed = []


# graph = {}
# graph["yuepu"] = {}
# graph["yuepu"]["changpian"] = 5
# graph["yuepu"]["haibao"] = 0
# graph["changpian"] = {}
# graph["changpian"]["jita"] = 15
# graph["changpian"]["jiazigu"] = 20
# graph["haibao"] = {}
# graph["haibao"]["jita"] = 30
# graph["haibao"]["jiazigu"] = 35
# graph["jita"] = {}
# graph["jita"]["gangqin"] = 20
# graph["jiazigu"] = {}
# graph["jiazigu"]["gangqin"] = 10
# graph["gangqin"] = {}
#
# infinity = float("inf")
# costs = {}
# costs["changpian"] = 5
# costs["haibao"] = 0
# costs["jita"] = infinity
# costs["jiazigu"] = infinity
# costs["gangqin"] = infinity
#
# parents = {}
# parents["changpian"] = "yuepu"
# parents["haibao"] = "yuepu"
# parents["jita"] = None
# parents["jiazigu"] = None
# parents["gangqin"] = None
#
# processed = []
#
#
# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
#
#
# def search():
#     node = find_lowest_cost_node(costs)
#     while node is not None:
#         cost = costs[node]
#         neighbors = graph[node]
#         for n in neighbors.keys():
#             new_cost = cost + neighbors[n]
#             if costs[n] > new_cost:
#                 costs[n] = new_cost
#                 parents[n] = node
#         processed.append(node)
#         node = find_lowest_cost_node(costs)
#
#
# def print_tree(st, ed):
#     parent = parents[ed]
#     if parent != st:
#         tmp = print_tree(st, parent) + "——>" + parent
#         return tmp
#     else:
#         return parent
#
#
# search()


# start, end = "start", "fin"
# ret = print_tree(start, end)
# ret = ret + "——>" + end
# print(ret)

# start, end = "yuepu", "gangqin"
# ret = print_tree(start, end)
# ret = ret + "——>" + end
# print(ret)


# ##******************************************
# from collections import deque
# # 广度优先搜索
# graph = {}
# graph["you"] = ["alice", "bob", "claire"]
# graph["bob"] = ["anuj", "peggy"]
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []
#
#
# def person_is_seller(name):
#     return name[-1] == 'm'
#
#
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 print person + " is a mango seller!"
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
#
# search("you")


# ##******************************************
# # 快速排序 O(n㏒n)
# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)
#
#
# my_list = [3, 9, 111, 0, 322, 5]
# print(quick_sort(my_list))


# ##******************************************
# # 选择排序 O(n²)
# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
#
# def select_sort(arr):
#     new_arr = []
#     for i in range(1,len(arr)):
#         smallest_index = find_smallest(arr)
#         new_arr.append(arr.pop(smallest_index))
#     return new_arr
#
#
# my_list = [3, 2, 5, 7, 0, 9]
# print(select_sort(my_list))

# ##******************************************
# # 二份查找 O(㏒n)
# def binary_search(lst, item):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = (high+low)/2
#         guess = lst[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# my_list = [1, 3, 5, 7, 9]
#
# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))
