
# Types
## Types
_Jacob_
What data type is returned from this function?

```python
def mathematics(x):
  y = x+4/2
  return y+x

print(mathematics(6))


```

Remember, the data type and not the output. -Jacob

<details>
<summary>Answers</summary>

float

</details>

# Arithmetic Operators

# Functions

## Another little function question
_Liya_
What is wrong with this code?

```python
maths = 2

def maths(a):
  b = (a+2)*3/4
  return b

print(maths(maths))
```

<details>
<summary>Answers</summary>

Don’t name your function and variable the same thing!

```python
num = 2

def maths(a):
  b = (a+2)*3/4
  return b

print(maths(num))
```

</details>


## What is the output

_Emir_ 

```python
def math():
  a = 2
  b = 0 
  if b < 10:
    a += 2
    a += b
  return a
print(math())
```
You can have more text after

<details>
<summary>Answers</summary>

4

</details>

## A little function question

_Liya_
What is wrong with this code?

```python
a = 2
def counta():
  a += 1
  return a

print(counta())
```

<details>
<summary>Answers</summary>

“a” is a global variable, so it can not be redefined in the function. This problem can be fixed by adding an input to the function. The local variable in the function should also be different.

```python
a = 2
def counta(b):
  b += 1
  return b

print(counta(a))
```
There is also another (simpler) way:

```python
a = 2
def counta():
  global a
  a += 1
  return a

print(counta())
```

</details>


# Conditionals

# While Loops
## Math
_Stephen_
Find the output

```python
x = 1
while x < 4:
  print(x)
  x +=1

```

<details>
<summary>Answers</summary>

1
2
3

</details>


# For Loops
## For Loops
_Jacob_
Write the output for the following loop

```python
x = 12

for i in range(1,x,2):
  print(i+2)

```

Input numbers only with a space in between each of them, no commas.

<details>
<summary>Answers</summary>

3 5 7 9 11 13

</details>

# Strings

## What would this return? Good luck heeeheeeheehaha
_gamble_
Question text

```python
cool_person = 'Thomas Gamble'
print(len(str(cool_person.count('a'))))
```

You can have more text after

<details>
<summary>Answers</summary>

1

</details>

# Lists
## What is the output of the following code?
_Alex_
```python
lst=[1,2,3,4,5,6,7,8,9,0,10,11]
new_lst=[]

for item in lst:
  if item % 2.5 == 0:
    new_lst.append(item)
  else:
    lst.remove(item)
if len(lst)+len(new_lst) in new_lst:
  x=new_lst.pop(0)

print(x)
```
<details>
<summary>Answers</summary>

5

</details>


## What is the output of this function?
_Sean_
```python
def happy(list2d):
  for row in list2d:
    for i in row:
      print(i)
    

(happy([[12, 44, 54], [67, 45, 15]]))



```

<details>
<summary>Answers</summary>


12
44
54
67
45
15
</details>




# For Each loops
