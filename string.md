+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [To Lower Case](#to-lower-case)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
<!-----solution----->

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
     vowels = set("AaEeIiOoUu")
     data = list(s)
     p1, p2 = 0, len(data) - 1
     while p1 < p2:
         if data[p1] in vowels and data[p2] in vowels:
             data[p1], data[p2] = data[p2], data[p1]
             p1 += 1
             p2 -= 1

             if data[p1] not in vowels:
             p1 += 1

             if data[p2] not in vowels:
             p2 -= 1

     return "".join(data)
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s: str) -> str:
    s = s.split(' ')
    for i in range(len(s)): s[i] = s[i][::-1]
    return " ".join(s)
```

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, str: str) -> str:
     return str.lower()
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s: List[str]) -> None:
         for i in range(len(s)//2):
             s[i],s[-i-1] = s[-i-1],s[i]
```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s: str, t: str) -> bool:
     return(sorted(s) == sorted(t))
```
