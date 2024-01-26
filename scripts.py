from functools import reduce
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x*x, nums))
filtered_nums = list(filter(lambda x: x>10, squared_nums))
sum_filtered = reduce(lambda a, b: a + b, filtered_nums)
squared_nums, filtered_nums, sum_filtered
print(squared_nums)
print(filtered_nums)
print(sum_filtered)
