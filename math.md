+ [Fibonacci Number](#fibonacci-number)
+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Sqrt(x)](#sqrtx)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
<!-----solution----->

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A: List[int]) -> int:
     A.sort()
     A.reverse()
     n = len(A)
     for i in range(n-2):
         if A[i] < A[i+1] + A[i+2]:
             return  A[i] + A[i+1] + A[i+2]
     return 0
```

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num: int) -> str:
     if num == 0:
         return('0')
     out = ''
     abs_num = abs(num)
     while abs_num > 0:
         out = str(abs_num % 7) + out
         abs_num = abs_num // 7
     if num < 0:
         out = '-' + out
     return(out)   
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n: int) -> List[str]:
     return ['FizzBuzz' if i%15 == 0 else 'Buzz' if i%5 == 0 else 'Fizz' if i%3 == 0 else str(i) for i in range(1,n+1)]
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x: int) -> float:
     left = 0
     right = x
     while left <= right:
         sqrt_x = (left+right)/2
         if abs(sqrt_x**2 - x ) <= 10**(-6):
             return sqrt_x
         if sqrt_x**2 < x:
             left = (left+right)/2
         else:
             right = (left+right)/2
     return sqrt_x
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
     original_x = x
     reversed_x = 0
     while x > 0:
         reversed_x = (reversed_x * 10) + (x % 10)
         x = x // 10
     return original_x == reversed_x
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x: int) -> int:
     if x > 0:
         ans = int("".join(reversed(str(x))))
         return ans if ans < 2**31 else 0
     ans = - int("".join(reversed(str(x)))[:-1])
     return ans if ans > - 2**31 else 0
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
     return int((((1+sqrt(5))/2)**N - ((1-sqrt(5))/2)**N)/sqrt(5))
```
