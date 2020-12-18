+ [Insert Interval](#insert-interval)
+ [Merge Intervals](#merge-intervals)
+ [Non-overlapping Intervals](#non-overlapping-intervals)
<!-----solution----->

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    p = intervals[0]
    deleted = 0
    for c in range(1, len(intervals)):
        s, e = intervals[c]
        if s < p[1]:
            deleted + = 1
        if e < p[1]:
            p = intervals[c]
    else:
        p = intervals[c]
    return(deleted)
```

##Insert Interval

https://leetcode.com/problems/insert-interval/

```python
 def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []      
        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                result.append(interval)      
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                return result+intervals[index:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])              
        result.append(newInterval)
        return result
```

##Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        result = [intervals[0]]
        for s in intervals[1:]:
            if s[0]<=result[-1][1]:
                result[-1][1] = max(result[-1][1], s[1])
            else:
                result.append(s)
        return result
```
