Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> x+5
10
>>> y=9
>>> x+y
14
>>> x=1
>>> x
1
>>> a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> x+10
11
>>> _+y
20
>>> name="prassi"
>>> name
'prassi'
>>> name+"sai"
'prassisai'
>>> name[0]
'p'
>>> name[-1]
'i'
>>> name[10]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name[10]
IndexError: string index out of range
>>> name[::-1]
'issarp'
>>> nmae[1:4]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    nmae[1:4]
NameError: name 'nmae' is not defined
>>> name[1:4]
'ras'
>>> name
'prassi'
>>> name[1:5]
'rass'
nmae[:5]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    nmae[:5]
NameError: name 'nmae' is not defined
name[:5]
'prass'
name[2:10]
'assi'
'sai'+name[0:3]
'saipra'
'hii'+name[3:]
'hiissi'
len(name)
6
nums=[12,232,34,45,56,78,99]
nums[0]
12
nums[-1]
99
names=['prassu','sai','maa']
names
['prassu', 'sai', 'maa']
values=[12,'prassu',12.23]
values
[12, 'prassu', 12.23]
add=[nums,names]
add
[[12, 232, 34, 45, 56, 78, 99], ['prassu', 'sai', 'maa']]
nums.append(544)
nums
[12, 232, 34, 45, 56, 78, 99, 544]
nums.insert(2,34)
nums
[12, 232, 34, 34, 45, 56, 78, 99, 544]
nums.insert(2,123)
nums
[12, 232, 123, 34, 34, 45, 56, 78, 99, 544]
nums.remove(34)
nums
[12, 232, 123, 34, 45, 56, 78, 99, 544]
nums.pop(2)
123
nums
[12, 232, 34, 45, 56, 78, 99, 544]
nums.pop()
544
nums
[12, 232, 34, 45, 56, 78, 99]
del nums[0:2]
nums
[34, 45, 56, 78, 99]
nums.extend(12,23,3454,456)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    nums.extend(12,23,3454,456)
TypeError: list.extend() takes exactly one argument (4 given)
nums.extend([12,345,567,687])
nums
[34, 45, 56, 78, 99, 12, 345, 567, 687]
min nums()
SyntaxError: invalid syntax
min(nums)
12
max(nums)
687
sum(nums)
1923
nums.sort()
nums
[12, 34, 45, 56, 78, 99, 345, 567, 687]
