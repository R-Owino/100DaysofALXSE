## Choosing a language for DSA
<p>Yesterday, we learned that algorithms are a set of step-by-step procedure to solve a particular problem. This step-by-step procedure is implemented using a programming language.</p>

<p>In this light, choosing a programming language, of course, is essential in learning DSA. The language chosen should align with your goals and your path.</p>

<p>For example, if you're crazy about machine learning and artificial intelligence, Python would do the job for you. If your focus is on understanding each basic process precisely, or want to work with embedded systems, C is the language for you. If you want to become a master at competitive programming, C++ would absolutely do it for you.</p>

### Seriously, I need to pick a language
<p>My obssession with Python goes way back when I was told it easy to learn and grasp. The obssession got even worse when I learned that Python is the primary language in Data Science and Machine Learning, albeit there being other great languages like R.</p>

<p>From my little history, it's clear what my goals are and what path I am mostly interested in. For that reason, I will be tackling DSA using Python</p>

### But why Python, tho?
<p>Python is a high-level language used widely in various fields. It is both strongly and dynamically typed. This means that the type of an object does not change in unexpected ways and the interpreter does not assign a type to the variable because the type can change at runtime</p>

<p>Consider these code snippets: </p>
- Showing that Python is strongly typed

```
1 + "1" # produces a TypeError
```

- Showing that Python is dynamically typed:

```
var = 23
print(type(var)) # at this moment, the type of var is an integer

var = "remmy is awesome"
print(type(var)) # at this moment, the type of var is a string
```
<p>Python is an object-oriented programming. This therefore means that the management of memory is often done at a class level through constructors and destructors, a concept called <i>garbage collection</i>. The constructors and destructors in Python allocate and free the memory, literally doing most of the garbage collection for us</p>


#### References
1. [Best language for learning Data Structures and Algorithms](https://www.youtube.com/watch?v=7h2A3hGQSsI)
2. [Languages for Data Structures](https://www.baeldung.com/cs/languages-learn-data-structures)
