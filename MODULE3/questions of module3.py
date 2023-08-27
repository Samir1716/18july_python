1) What is List? How will you reverse a list? 
--> In Python, a built-in function called reverse() is used to reverse the list. This simple and quick way to reverse a list in Python requires little memory. Syntax: list_name. reverse() Here, list_name means you have to write the list's name, which has to be reversed.

3) Differentiate between append () and extend () methods?
--> Effect: .append() adds a single element to the end of the list while . extend() can add multiple individual elements to the end of the list.
Argument: .append() takes a single element as argument while . extend() takes an iterable as argument (list, tuple, dictionaries, sets, strings

5) How will you compare two lists? 
--> The methods of comparing two lists are given below.
    1)The cmp() function.
    2)The set() function and == operator.
    3)The sort() function and == operator.
    4)The collection.counter() function.
    5)The reduce() and map() function.

17) What is tuple? Difference between list and tuple.

-------::List::---------

--->It is mutable	
--->The implication of iterations is time-consuming in the list.	
--->Operations like insertion and deletion are better performed.	
--->Consumes more memory.	

-------::Tuple::--------

--->It is immutable
--->Implications of iterations are much faster in tuples.
--->Elements can be accessed better.
--->Consumes less memory.

33) How Do You Traverse Through A Dictionary Object In Python?
--> To iterate a dictionary using a specified order, use Python's sorted() method. The item will initially be sorted before being traversed through by a for a loop. Dictionary keys are sorted by the function sorted(dictionary. keys()), and for iterates through the keys that were returned. 

41) Why Do You Use the Zip () Method in Python? 
--> The zip() function in Python is used to combine two or more iterable dictionaries into a single iterable, where corresponding elements from the input iterable are paired together as tuples. When using zip() with dictionaries, it pairs the keys and values of the dictionaries based on their position in the dictionary.

50) How Many Basic Types Of Functions Are Available In Python? 
--> Two Types: 
	There are mainly two types of functions in Python.
	1)Built-in library function: These are Standard functions in Python that are available to use. 
	2)User-defined function: We can create our own functions based on our requirements

51) How can you pick a random item from a list or tuple?
--> Using random.
Create a tuple and add some dummy data to it. Generate a random item from the tuple using random. choice() method(This function returns a random element from the specified sequence i.e tuple here) by passing the input tuple as an argument to the choice() function.

52) How can you pick a random item from a range?
--> 1) Using random.randrange() function.
    2) Using random.randint() function.
    3) Using random.random() function.
    4) Using random.sample()

53) How can you get a random number in python?
--> Generating a random integer within a given range – randint()
Firstly, import the random module of Python.Then, we call the randint(min, max) method to get a random integer within the given range      and store it in the variable n.Print the randomly generated number.

54) How will you set the starting value in generating random numbers? 
--> The seed() method is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number. By default the random number generator uses the current system time.

55) How will you randomizes the items of a list in place?
--> The shuffle() method randomizes the items of a list in place.