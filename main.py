# Lists for addition
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
# Adding corresponding elements using map() and lambda
added_list = list(map(lambda x, y: x + y, list1, list2))
print("Sum of elements from two lists:", added_list)
# List for squaring
list3 = [2, 4, 6, 8]
# Getting the square of each element using map() and lambda
squared_list = list(map(lambda x: x ** 2, list3))
print("Squares of elements in list3:", squared_list)