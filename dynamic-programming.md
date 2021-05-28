+ [House Robber](#house-robber)
+ [House Robber II](#house-robber-ii)
<!-----solution----->

## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
def rob(self, nums):
    if len(nums)==0:
        return 0
    if len(nums)==1:
        return nums[0]
    if len(nums)==2:
        return max(nums)
    
    def house_robber(nums):
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            print(dp)
        return max(dp)

    return max(house_robber(nums[1:]), house_robber(nums[:-1]))
```

## House Robber

https://leetcode.com/problems/house-robber/

```python
def rob(self, nums):
    length = len(nums)
    if length==0:
        return 0
    if length==1:
        return nums[0]
    if length==2:
        return max(nums)
    
    dp = [0]*length
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, length):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])
    return max(dp)
```