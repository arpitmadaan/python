nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# for element in nums:
#     if element == 0:
#         nums.remove(element)
#         nums.append(element)
# print(nums)
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
print(nums)