numbers = [2, 7, 11, 15]
target_number = 9
list_of_found_indexes = []

for index in range(0, len(numbers)-1):
    current_sum = int(numbers[index]) + int(numbers[index + 1])
    if current_sum == target_number:
        list_of_found_indexes.append(index)
        list_of_found_indexes.append(index + 1)
        break

print(list_of_found_indexes)

# OR

nums = [2, 7, 11, 15]
target_number = 9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_of_found_indexes = []
        for index in range(0, len(numbers) - 1):
            current_sum = int(nums[index]) + int(nums[index + 1])
            if current_sum == target_number:
                list_of_found_indexes.append(index)
                list_of_found_indexes.append(index + 1)
                return list_of_found_indexes
