# def first_repeated_value(list):
#     for i in range(0, len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] == list[j]:
#                 return list[i]
#     return None

# def first_repeated_value(list):
#     # create a Set to keep track of values we've seen
#     number_set = set()
#     # iterate over element from the list
#     for i in range(0, len(list)):
#         #if we've already seen a value, we've found the duplicate
#         if list[i] in number_set:
#             return list[i]
#         # otherwise add the value to our set
#         number_set.add(list[i])
#     # return None if we reach the end and haven't found our value
#     return None
