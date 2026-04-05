# Python - Everything is Object

This project focuses on one of Python’s most important ideas: **everything is an object**.

It explores how Python handles:
- object identity
- object type
- mutable and immutable objects
- equality versus identity
- variable assignment
- how arguments are passed to functions

Through short answer files and small functions, the project helps build a strong understanding of how objects behave in Python and why some changes affect other variables while others do not.

## Learning Objectives

At the end of this project, you should be able to explain:

- What an object is
- The difference between `type` and `id`
- What mutable and immutable objects are
- The difference between `==` and `is`
- How assignment works in Python
- How Python passes arguments to functions
- Why lists can change across references but integers and strings usually do not

## Project Structure

Most tasks in this project are answered using:
- `.txt` files for conceptual questions
- `.py` files for short function implementations

## Main Concepts Covered

### Object identity
Each object in Python has an identity. You can get it with:

```python
id(obj)