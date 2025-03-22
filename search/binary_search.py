

from typing import List


def binary_search(nums: List[int], target: int) -> int:
	left, right = 0, len(nums) - 1

	while left <= right:
		mid = left + (right - left) // 2

		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	
	return -1

nums = [1,4,7,12,15,21,24,32,52]
target = 52
print(binary_search(nums, target))