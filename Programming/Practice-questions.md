# Types

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

_Steven_Han_

Find the output

```python
x = 3

for i in range(5):
  if x > 3:
    x+=2
    x%5
    print(x)
else:
    x+=4
    x*=2
    print(x)

```

<details>
<summary>Answers</summary>

14

</details>

---

_Joanne_

Find the surface area of a cube, when the length of a side is 8. 

```python
a = 8
surfacearea = 6*(a*a)
print("Surface area of cube is: ", surfacearea)

```


<details>
<summary>Answers</summary>

384

</details>

---

_Divyash_

What will the output be for the given inputs?

```python
a = int(input(1))
b = int(input(2))
c = int(input(3))

print((-b * (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
```


<details>
<summary>Answers</summary>

1

</details>

---

_Mystery_student_

What is the output
```python
A=5



while A %2 != 0:
  print(A + 67)
  A+=1


```

<details>
<summary>Answer</summary>

72

</details>


# Functions


_Jacob_
Find two errors with this code and suggest fixes for it.

```python
Years = (Y7, Y8, Y9)

def addingH1(lst):
  append.lst(H1)
  return lst
  
print(addingH1(list))
```

Spot an error then write a fix for it -Jacob

<details>
<summary>Answers</summary>

Brackets are not square brackets. Fix: [Y7, Y8, Y9]
Function is written incorrectly. Fix: lst.append(H1)

</details>

---


_Emir_ 

What is the output?

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

<details>
<summary>Answers</summary>

4

</details>

---

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

"a" is a global variable, so it can not be redefined in the function. This problem can be fixed by adding an input to the function. The local variable in the function should also be different.

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

---

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

# Conditionals

_Yu_Tang_

What is the output?

```python

a='there is going to be a typhon today'
if (len(a))!= (5 * min(7, 8)):
  print (a[9:])
else:
  print (pow(3,2))



```

<details>
<summary>Answers</summary>

9

</details>

---

_OscarS_

Find the errors (there are 2)

```python

Cash = int(input("How much money do you have : "))

if cash > 100:
  print("wow you have so much money!")
elif cash <= 50
  print("broke >:( ")
else: 
  print("that's an ok amount i guess")

```

<details>
<summary>Answers</summary>

all variables should be spelled the same , make Cash, cash. There should also be a colon after 50

</details>

---

_Liya_

What is wrong with this code?

```python
num = int(input("Give a number: "))

if num = 0:
  print("Really? Zero?")
elif num > 1 and num < 4:
  print("Starting small...")
elif num < 10:
  print("Getting big!")
```

<details>
<summary>Answers</summary>

```python
if num = 0:
  print("Really? Zero?")
```
One "=" defines something!
Use two "="’s (==) to check if the condition is true. 

```python
if num == 0:
  print("Really? Zero?")
```

</details>

---

# While Loops

_Carlos_

What is the output?!??!!?!?!?!?!!!?!?!? 

```python

number=0
i=1
while number!=5:
  print(i*"i")
  number+=1
  i+=1 
```


<details>
<summary>Answers</summary>

  
i
ii
iii
iiii
iiiii

</details>

---

_Roker_

What is the output?
```python
x = 10
while x < 20:
  print(x)
  x+=1

```



<details>
<summary>Answers</summary>

10
11
12
13
14
15
16
17
18
19

</details>

---

_Evil_Marcus_

What is the output?
```python
import random
import time
x=0
y=16

while x != y:
  if x == O:
    y+=2
  else:
    y+=5
print(y)

```


<details>
<summary>Answer</summary>

Error because
"O" not 0
</details>

---

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
_Millie_Yeh_
Rewrite the loop

```python

for i in range (10):
  print(a)

```

<details>
<summary>Answers</summary>

```python
a = 0  
while a <= 9:
a += 1
print(a)
```

Or 

```python
a = 0  
while a < 10:
a += 1
print(a)

```


</details>

---

_Karina_

(MWAHAHAHAHA)

Rewrite this as a while loop

```python

lst = [1, 2, 3, 4, 5, 6]

for item in lst:
   print(item)

```

<details>
<summary>Answers</summary>
```python
x = 0
while x < 6:
   print (lst[x])
   x += 1
```

</details>

---



_Almas_

What is the output of this code?

```python
number = 20
for i in range(number):
  if (i + number) % 2 == 0:
    print(i+5)

```


<details>
<summary>Answers</summary>


5
7
9
11
13
15
17
19
21
23


</details>

---

_Alex_

What is the output?

```python
x=4
y=0
for i in range(x):
  y+=x*2
  x+=42
  print(x)
  print(y)

```



<details>
<summary>Answers</summary>
46 
6
88
100
130
276
172
536

</details>

---

_Ferdi_

What is the output of the code below?

```python
lst = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lst)):
  if lst[i] % 2 == 0:
    print(lst[i])
  else:
    print(lst[i] * 2 / 10)
```

<details>
<summary>Answers</summary>

0.2
2
0.6
4
1.0
6
1.4
8
1.8
10

</details>

---

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
_YuTang_

What is the output?

```python

a=['dumb ways to die']
if len(a)!= (pow(2,3)):
  print ("BANANA")
else:
  print ("woo")


```

<details>
<summary>Answers</summary>

 BANANA

</details>

---

_Karina_

What is the error?

```python

print(""HI!, MY NAME IS OAUHWDIQO")

```

<details>
<summary>Answers</summary>

Double quote marks at the font

print("HI!, MY NAME IS OAUHWDIQO")

</details>

---

_Gamble_

What would this return? Good luck heeeheeeheehaha

```python
x = 'Stephen ist nicht der beste'

if x.count('e') == 7-2:
	print(':)')
else:
	print(':(')

```


<details>
<summary>Answers</summary>

:)

</details>

---

What would this return? Good luck heeeheeeheehaha

_Gamble_


```python
cool_person = 'Thomas Gamble'
print(len(str(cool_person.count('a'))))
```


<details>
<summary>Answers</summary>

1

</details>

---


# Lists

_Alex_

What is the output of the following code?
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

---

_Sean_

What is the output of this function?
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

---

_Evil_Dennis_

What is the output
> Note: This question is probably a bit too evil, but feel free to have a go if you fancy it.

```python
list = ([[7,2,3],[5,62,4]],[[1,5,0],[10,91,52]],[[0,1,2],[3,4,5]])
def very_simple_mathematics(list):
  test = [7,2,3,4,5]
  check = ''
  temp = []
  for i in range(len(list)):
    temp.append(list[i][i-1][i-1])
  for i in temp:
    check += str(i)
  for i in temp:
    for x in test:
      if i == x:
        check += str(x)
  return check

print(very_simple_mathematics(list))
```

You want to play? Let's play

<details>
<summary>Answers</summary>

41444

</details>

---

_StephenHan_
Find the 2 error

```python
Lst = (1,5,7,4,7)
print(lst.count(‘e’)
```


<details>
<summary>Answers</summary>

[   ] not ()

Missing bracket at the end of the code

</details>

---

_Steven_Yen_
What is the output?

```python

suxwy9ijthmnm=["FYI_+^#",3,"hi@#%","HeRe$!^",40,74,"QwErtY*&^",52,65,2,4,62,2,3]

print (suxwy9ijthmnm.pop(11))
print (suxwy9ijthmnm)
print (suxwy9ijthmnm.pop(3))
print (suxwy9ijthmnm)
```


<details>
<summary>Answers</summary>

62
["FYI",3,"hi","here",40,74,"qwerty",52,65,2,4,2,3] 
HeRe$!^
["FYI_+^#",3,"hi@#%",40,74,"QwErtY*&^",52,65,2,4,62,2,3]
</details>
 
 ---

_Sean_

What is the output of:  
```python
list = []
list2d = [1, 2, 3] 

list.append(list2d)

print(list[0][1])


```


<details>
<summary>Answers</summary>

2


</details>



# For Each loops


_Marcus_

Find the output

```python
workkakaka = ["Yo ", "Lol ", "Bye "]
worddadada = ["Bro", "Man", "Marcus"]
tootototo = ''
for i in worddadada:
  for x in workkakaka:
    tootototo += x + i
print(tootototo)

```

<details>
<summary>Answers</summary>

Yo BroLol BroBye BroYo ManLol ManBye ManYo MarcusLol MarcusBye Marcus

</details>

---

_Millie Yeh_
What’s the output??

```python

favfruit = [ "blueberry","strawberry","cherry","mango","peach","pineapple","kiwi" ]
mostfavfruit = []

for i in favfruit:
	if "a" in x:
		mostfavfruit.append(x)
print(mostfavfruit)

```

<details>
<summary>Answers</summary>

 ["strawberry", "mango", "pineapple"] 

</details>

---

_Ann_

What does this code print?

```python

gummy_bears = ["red", "purple", "orange", "blue", "green", "yellow"]
for bear in gummy_bears:
  if len(bear) >5:
    print(bear[:-1])
  else:
    text = ""
    for i in bear:
      text = i + text
    print(text)

```
Blue gummy bears taste good. 

<details>
<summary>Answers</summary>

 der
purpl
orang
eulb
neerg
yello

</details>

