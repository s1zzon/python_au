+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
+ [Max Consecutive Ones](#max-consecutive-ones)
<!-----solution----->

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:      
.    count = maxCount = 0      
.    for i in range(len(nums)):
.        if nums[i] == 1:
.            count += 1
.        else:
.            maxCount = max(count, maxCount)
.            count = 0                
.    return max(count, maxCount)
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, A: List[int]) -> List[int]:
.    return sorted(map(lambda x :x**2, A))
```