+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Move Zeroes](#move-zeroes)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
<!-----solution----->

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
def imageSmoother(self, M):
    R, C = len(M), len(M[0])
    ans = [[0] * C for _ in M]

    for r in range(R):
        for c in range(C):
            count = 0
            for nr in (r-1, r, r+1):
                for nc in (c-1, c, c+1):
                    if 0 <= nr < R and 0 <= nc < C:
                        ans[r][c] += M[nr][nc]
                        count += 1
            ans[r][c] = floor(ans[r][c]/count)

    return ans  
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    data = []
	for i in range(len(nums)):
		for j in range(len(nums[i])):
			data.append(nums[i][j])

	if len(data) != r * c:
		return nums

	result = []
	for i in range(r):
		result.append([])

	i = 0
	for item in data:
		if len(result[i]) == c:
			i += 1
		result[i].append(item)
	return result
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A):
     sol = []

     for c in range(len(A[0])):
         tmp = []
         for r in range(len(A)):
             tmp.append(A[r][c])

         sol.append(tmp)

     return sol
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

     for row in A:
         row.reverse()
         for i in range(len(row)):
             row[i] = 1 - row[i]

     return A
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: List[int]) -> None:
     i = 0
     for j in range(len(nums)):
 	    if nums[j] != 0:
             nums[i],nums[j] = nums[j],nums[i]
             i = i+1
```

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:      
     count = maxCount = 0      
     for i in range(len(nums)):
         if nums[i] == 1:
             count += 1
         else:
             maxCount = max(count, maxCount)
             count = 0                
     return max(count, maxCount)
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, A: List[int]) -> List[int]:
     return sorted(map(lambda x :x**2, A))
```
