# Example Input:
list1 = [3, 1, 4]
list2 = [2, 5, 0]
list1.extend(list2)
list1.sort()
print(list1)
# Example Output:
# [0, 1, 2, 3, 4, 5]''''''
# Example Input:
s = "abc"
n = 3
result = "".join([char * n for char in s])
print(result)
# Example Output:
# "aaabbbccc"