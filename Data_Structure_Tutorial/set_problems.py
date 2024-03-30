
#Problem 1 Solution
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(find_common_elements(list1, list2))  # Output: [3, 4]



#Problem 2 Solution
def find_subsets_with_sum(input_list, target_sum):
    subsets = []
    n = len(input_list)

    for i in range(1 << n):
        subset = [input_list[j] for j in range(n) if (i & (1 << j))]
        if sum(subset) == target_sum:
            subsets.append(subset)
    return subsets

# Example usage
nums = [2, 4, 6, 8]
target = 10
print(find_subsets_with_sum(nums, target))  # Output: [[2, 8], [4, 6]]