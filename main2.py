# Define two sample list
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]
# 1. Zipped list from two lists
zipped_list = list(zip(list1, list2))
print("Zipped list:", zipped_list)
# 3. Zipped into a dictionary
zipped_dict = dict(zip(list1, list2))
print("Zipped into dictionary:", zipped_dict)