
from typing import List

def bubble_sort(nums: List[int]) -> None:
	swap = True
	rng = 0
	while swap:
		swap = False 
		for i in range(1, len(nums) - rng):
			if nums[i] < nums[i-1]:
				nums[i], nums[i-1] = nums[i-1], nums[i]
				swap = True
		rng += 1

nums = [4,1,5,7,12,9,16,21,19]
bubble_sort(nums)

print(nums)
