## Introduction to Python
<p>Yesterday while picking a prefered language to learn DSA, I introduced some concepts about Python that makes it a go-to language for me. I will not go indepth about those concepts or start Python from sratch as I am already a regular user and there are tons of tutorials online that go from A-Z about Python, including the documentation &#128522;.</p>

<p>Instead, this will be a refresher on more specific topics such as the language syntax, control structures, functions and Object Oriented Programming (OOP) basics.</p>

<P>This is because, as I said yesterday, memory management is done at the class level (an OOP concept) through constructors and destructors. Getting a refresher on these would make the work way easier as I go along my DSA journey.</P>

<p>Let's get started</p>

### 1. Python syntax
<p>Syntax defines a set of rules used to create a Python program. While learning DSA, I will use purely script mode programming i.e creating a <i>.py</i> file and writing my code in it.</p>

<p>In the file <i>python_syntax.py</i>, I will brush over the various rules in Python programming. To run the script, on the command-line do `python3 python_syntax.py` or `./python_syntax.py` (the first line in the file allows us to use the second option)</p>

<p>Without any errors, python_syntax.py produces the following output:</p>

```
$ ./python_syntax.py 
abc123_
123abc
Enter True or False: False
Goodbye, World!
3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0]
```

<p>With the errors included, the following output will be generated</p>

```
$ ./python_syntax.py 
  File "/home/remmy/Documents/projects/100DaysofALXSE/Day 3/./python_syntax.py", line 33
    print("Learning DSA")
IndentationError: unexpected indent
```

<p>As long as it hits an error, it won't execute. To run the file error free, comment out the problematic blocks.</p>

### 2. Control Structures
<p>Python has 3 main control flow structures:<br>
1. if...else<br>
2. while loop<br>
3. for loop<br>
</p>

<p>In the file <i>control_structures.py</i>, I will go over the major control statements. Python documentation handles the rests very well, no need repeating those.</p>

<p>On execution, this is the expected output:</p>

```
$ ./control_structures.py 
Enter temperature in Celsius: 40
It is quite hot outside!
cat 3
window 6
defenestrate 12
1
2
3
4
5
----------
1
3
5
7
```

### 3. Functions
<p>Functions are resusable blocks of code that must be called to be used. Their primary purpose is to help organize programs into chunks of code that match how a solution to a problem is thought </p>

<p>Functions can either be built-in or user defined. So far I have been using built-in functions such as print()</p>

<p>In the file <i>functions.py</i>, I will explore more on user defined functions</p>


#### References
1. [Python Syntax](https://www.tutorialspoint.com/python/python_basic_syntax.htm)
2. [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)