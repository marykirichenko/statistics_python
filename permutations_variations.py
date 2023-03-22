def tree_permutation(nums):
    result = []
    if(len(nums)==1):
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = tree_permutation(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)

    return result

print(tree_permutation([1,2,3,4]))

def variation_with_repetition(nums, m):
    result = []
    if m == 0:
        return [[]]

    for num in nums:
        for sub_variation in variation_with_repetition(nums, m-1):
            result.append([num] + sub_variation)

    return result
print(variation_with_repetition([1,2,3,4],2))


def variation_without_repetition(nums, m):
    result = []
    if m == 0:
        return [[]]
    for i in range(len(nums)):
        num = nums[i]
        remaining = nums[:i] + nums[i+1:]
        for sub_variation in variation_without_repetition(remaining, m-1):
            result.append([num] + sub_variation)
    return result

print(variation_without_repetition([1,2,3,4],2))

def combination_without_repetition(nums, m):
    result = []
    if m == 0:
        return [[]]
    for i in range(len(nums)):
        num = nums[i]
        remaining = nums[i+1:]
        for sub_combination in combination_without_repetition(remaining, m-1):
            result.append([num] + sub_combination)
    return result
print(combination_without_repetition([1,2,3,4,5,6],4))
