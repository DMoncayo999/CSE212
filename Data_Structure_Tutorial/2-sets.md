# Sets

<div style="margin-top: 20px; margin-bottom: 20px;">
  <img src="utensil_set.png" alt="Stack of Books" width="350">
</div>


## Introduction
A set in Python is an unordered collection of unique elements. This means that each element in a set appears only once, and the order of elements is not guaranteed. 

Sets are commonly used for tasks that involve checking membership, eliminating duplicate entries, and performing set operations like union, intersection, and difference.

## Characteristics of Sets
- Sets do not allow duplicate elements.
- Sets are unordered, so the elements are not indexed.
- Sets are mutable, meaning you can add or remove elements from a set.
- Sets can store various data types, including numbers, strings, and tuples, but not mutable objects like lists or other sets.

## Hashing and Sets
Sets in Python use a hash table implementation, which allows for efficient membership testing and set operations. The hash table uses hash values to store and retrieve elements quickly, making set operations such as checking membership very efficient.

## Diagrams and Tables
Let's visualize the operations and performance of sets using a table:

| Set Operation  | Description                                    | Performance (Big O) |
|----------------|------------------------------------------------|---------------------|
| add(element)   | Adds an element to the set                     | O(1)                |
| remove(element)| Removes an element from the set                | O(1)                |
| discard(element)| Removes an element from the set if present     | O(1)                |
| clear()        | Removes all elements from the set              | O(1)                |
| pop()          | Removes and returns an arbitrary element       | O(1)                |
| union(other_set)| Returns a new set with elements from both sets | O(n)                |

The "Performance (Big O)" column in the table represents the time complexity of each set operation using Big O notation. Big O notation is a way to describe the upper bound of the time complexity of an algorithm or operation in terms of its input size


### Examples

Let's demonstrate a problem solved using sets:

**Problem:** Count the number of unique elements in a list.

```python
def count_unique_elements(input_list):
    unique_set = set(input_list)
    return len(unique_set)


# Example usage
my_list = [1, 2, 3, 4, 1, 2, 5]
print(count_unique_elements(my_list))  # Output: 5 (unique elements: 1, 2, 3, 4, 5)

```
**Problem:** Given two lists, determine if one list is a subset of the other list.

```python
def is_subset(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.issubset(set2) or set2.issubset(set1)


# Example usage
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5]
list3 = [2, 3, 5]
print(is_subset(list1, list2))  # Output: True (list1 is a subset of list2)
print(is_subset(list1, list3))  # Output: False (list1 is not a subset of list3)
```


## Problem to Solve

**Problem 1:** Given two lists, find and print the common elements between them.

**Problem 2:** Given a list of integers, find all subsets of the list where the sum of elements in each subset is equal to a target sum.

## Problem Solution
You can check your code with the solution here: [Solution](set_problems.py)





[Back to Welcome Page](0-welcome.md)