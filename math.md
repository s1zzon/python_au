+ [Fibonacci Number](#fibonacci-number)
+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Sqrt(x)](#sqrtx)
<!-----solution----->

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x: int) -> float:
.    left = 0
.    right = x
.    while left <= right:
.        sqrt_x = (left+right)/2
.        if abs(sqrt_x**2 - x ) <= 10**(-6):
.            return sqrt_x
.        if sqrt_x**2 < x:
.            left = (left+right)/2
.        else:
.            right = (left+right)/2
.    return sqrt_x
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
.    original_x = x
.    reversed_x = 0
.    while x > 0:
.        reversed_x = (reversed_x * 10) + (x % 10)
.        x = x // 10
.    return original_x == reversed_x
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x: int) -> int:
.    if x > 0:
.        ans = int("".join(reversed(str(x))))
.        return ans if ans < 2**31 else 0
.    ans = - int("".join(reversed(str(x)))[:-1])
.    return ans if ans > - 2**31 else 0
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
.    return int((((1+sqrt(5))/2)**N - ((1-sqrt(5))/2)**N)/sqrt(5))
```
