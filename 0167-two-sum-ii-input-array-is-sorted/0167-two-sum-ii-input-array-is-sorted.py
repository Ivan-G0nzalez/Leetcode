class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0;
        end = len(numbers) - 1
        
        
        while start < end:
            tem_sum = numbers[start] + numbers[end]
            if tem_sum == target:
                return [start+1, end+1]
            elif tem_sum < target:
                start += 1
            else:
                end -= 1
        
        return []