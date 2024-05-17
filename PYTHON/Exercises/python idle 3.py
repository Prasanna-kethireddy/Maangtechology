Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tup=(12,23,34,45,56,67,78,89,90)
tip
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tip
NameError: name 'tip' is not defined. Did you mean: 'tup'?
print("tup")
tup
print(tup)
(12, 23, 34, 45, 56, 67, 78, 89, 90)
tup[1]
23
tup.index(56)
4
data={1:"prassu",2:"sai",3:"usha",4:"maa"}
data
{1: 'prassu', 2: 'sai', 3: 'usha', 4: 'maa'}
data(keys)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data(keys)
NameError: name 'keys' is not defined
data.keys()
dict_keys([1, 2, 3, 4])
data.values()
dict_values(['prassu', 'sai', 'usha', 'maa'])
data.items()
dict_items([(1, 'prassu'), (2, 'sai'), (3, 'usha'), (4, 'maa')])
len(data)
4
data.get(1)
'prassu'
data.get(5)
print(data.get(5))
None
data.get(1,'not found')
'prassu'
data.get(5,'nit found')
'nit found'
data["devi"]=5
data
{1: 'prassu', 2: 'sai', 3: 'usha', 4: 'maa', 'devi': 5}
data[6]="amma"
data
{1: 'prassu', 2: 'sai', 3: 'usha', 4: 'maa', 'devi': 5, 6: 'amma'}
data['devi']
5
del data['devi']
data
{1: 'prassu', 2: 'sai', 3: 'usha', 4: 'maa', 6: 'amma'}
da=[1,2,3,4,5]
li=["prassu","dada","mama","papa","kaka"]
pras=dict(zip(da,li))
pras
{1: 'prassu', 2: 'dada', 3: 'mama', 4: 'papa', 5: 'kaka'}
prog=
SyntaxError: invalid syntax
prog={"prasanna":["prassu","chinnu","peddha"],"usha":{"scl":"sissu","clg":"sri"},"sai":"kanna"}
prog
{'prasanna': ['prassu', 'chinnu', 'peddha'], 'usha': {'scl': 'sissu', 'clg': 'sri'}, 'sai': 'kanna'}
prog["prasanna"]
['prassu', 'chinnu', 'peddha']
prog["usha"]
{'scl': 'sissu', 'clg': 'sri'}
prog["usha"]["clg"]
'sri'
prog["prasanna"][1]
'chinnu'
id(prog)
1533212255808
prog(data)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    prog(data)
TypeError: 'dict' object is not callable
>>> id(data)
1533253050944
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,20))
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(2,100,5))
[2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]
>>> list(range(1,100,5))
[1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
>>> list(range(5,100,5))
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=4
>>> b=9
>>> temp=a
>>> a=b
>>> b=temp
>>> a
9
>>> b
4
>>> a=1
>>> b=2
>>> a=a^b
>>> b=a^b
>>> a=a^b
>>> a
2
>>> b
1
>>> a=8
>>> b=0
>>> a,b=b,a
>>> a
0
>>> b
8
