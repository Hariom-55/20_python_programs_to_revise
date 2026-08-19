# 20 Python Programs to Revise

A practical Python revision journey focused on **learning Python through problem-solving** rather than memorizing syntax.

The objective of this repository is to build 20 progressively challenging programs that strengthen Core Python concepts and gradually connect them with **Data Science and Machine Learning workflows**.

> **Learning Rule:** For every important concept, the manual implementation is practiced first. Only after understanding the underlying logic do we look at Python's built-in functions, methods, or more Pythonic approaches.

---

## Progress

**6 / 20 Programs Completed**

```text
[██████░░░░░░░░░░░░] 30%
```

| Program | Topic                             | Status      |
| ------- | --------------------------------- | ----------- |
| 01      | Student Marks Analyzer            | ✅ Completed |
| 02      | Prediction Probability Manager    | ✅ Completed |
| 03      | Customer Purchase History Manager | ✅ Completed |
| 04      | Product Inventory Management      | ✅ Completed |
| 05      | Student Attendance Analyzer       | ✅ Completed |
| 06      | ML Configuration Manager          | ✅ Completed |
| 07      | Coming Soon                       | ⬜           |
| 08      | Coming Soon                       | ⬜           |
| 09      | Coming Soon                       | ⬜           |
| 10      | Coming Soon                       | ⬜           |
| 11      | Coming Soon                       | ⬜           |
| 12      | Coming Soon                       | ⬜           |
| 13      | Coming Soon                       | ⬜           |
| 14      | Coming Soon                       | ⬜           |
| 15      | Coming Soon                       | ⬜           |
| 16      | Coming Soon                       | ⬜           |
| 17      | Coming Soon                       | ⬜           |
| 18      | Coming Soon                       | ⬜           |
| 19      | Coming Soon                       | ⬜           |
| 20      | Coming Soon                       | ⬜           |

---

# How This Journey Works

Each program is designed to introduce or reinforce Python concepts through a practical problem.

For every important concept, the learning process follows:

```text
Problem
   ↓
Constraint
   ↓
Manual Implementation
   ↓
Understand the Logic
   ↓
Python Built-in / Better Alternative
   ↓
Understand When to Use It
   ↓
Important Notes
```

### Why avoid built-ins initially?

If we immediately use:

```python
max(values)
```

we know **how to get the answer**, but we may not understand **how the logic works**.

Instead, we first implement:

```python
highest = values[0]

for value in values:
    if value > highest:
        highest = value
```

Once the logic is understood, we learn:

```python
highest = max(values)
```

This approach helps develop both:

* **Problem-solving ability**
* **Practical Python knowledge**

---

# Program 01 — Student Marks Analyzer

## Objective

Build a student marks analysis system that accepts marks for multiple students and generates useful academic statistics.

---

## Concepts Learned

### 1. Variables

**Constraint:**
Before using complex structures, store individual values using simple variables.

**What is it?**

A variable is a name that refers to a value stored in memory.

```python
student_name = "Hariom"
marks = 85
average = 82.5
```

**Important points:**

* Python variables do not require explicit type declarations.
* A variable can reference different types of values.
* Use meaningful variable names.
* Variable names are case-sensitive.

**Useful built-ins/functions:**

```python
type(value)
```

can be used to determine the type of a value.

---

### 2. Data Types

The program works with several fundamental Python data types:

```text
int
float
str
list
```

Examples:

```python
age = 22
percentage = 85.5
name = "Hariom"
marks = [80, 85, 90]
```

**Important points:**

* `int` → whole numbers
* `float` → decimal numbers
* `str` → text
* `list` → collection of values

**Useful built-in:**

```python
type(value)
```

---

### 3. User Input

**Constraint:**
Accept input through `input()` and manually convert it to the required type.

```python
marks = int(input("Enter marks: "))
```

**What is `input()`?**

`input()` accepts data from the user.

By default, the returned value is a string.

```python
age = input("Enter age: ")
```

Therefore:

```python
age = int(input("Enter age: "))
```

converts the input into an integer.

**Important point:**

`input()` always initially returns a string.

---

### 4. Lists

**Constraint:**
Store multiple values inside a list and manually process them using loops before relying on built-in operations.

```python
marks = [80, 75, 91, 88]
```

A list is an ordered, mutable collection.

**Important points:**

* Lists are ordered.
* Lists are mutable.
* Lists can contain duplicate values.
* Indexing starts from `0`.

```python
marks[0]
```

**Useful methods:**

```python
marks.append(95)
marks.remove(75)
marks.sort()
```

---

### 5. `for` Loop

**Constraint:**
Use a loop to manually process every value instead of directly using aggregate functions.

```python
for mark in marks:
    print(mark)
```

A `for` loop is used when we want to iterate over elements of an iterable.

**Important points:**

* It processes elements one by one.
* It works with lists, tuples, strings, sets, dictionaries, and more.
* Nested loops can process multidimensional data.

---

### 6. Nested Loops

**Constraint:**
Use nested loops when data has multiple levels instead of trying to flatten the data immediately.

```python
for student in students:
    for subject in student:
        ...
```

A nested loop is simply a loop inside another loop.

**Important point:**

If the outer loop runs `n` times and the inner loop runs `m` times, the operation may execute approximately `n × m` times.

---

### 7. `while` Loop

Used when an operation needs to continue until a condition becomes false.

```python
while marks < 0 or marks > 100:
    marks = int(input("Enter valid marks: "))
```

**Important points:**

* Useful for validation.
* Make sure the condition eventually becomes false.
* Otherwise, an infinite loop can occur.

---

### 8. Conditional Statements

Used:

```python
if
elif
else
```

Example:

```python
if marks >= 40:
    result = "Pass"
else:
    result = "Fail"
```

**Important points:**

* `if` checks the first condition.
* `elif` checks additional conditions.
* `else` handles the remaining cases.
* Conditions produce Boolean results.

---

### 9. Input Validation

**Constraint:**
Do not assume that user input is valid.

For example:

```text
Marks must be between 0 and 100.
```

Validation prevents invalid values from entering the program.

**Important principle:**

```text
Input
 ↓
Validate
 ↓
Process
```

rather than:

```text
Input
 ↓
Process immediately
```

This principle becomes extremely important when working with real-world datasets.

---

### 10. Exception Handling

**Constraint:**
First understand what can go wrong before using exception handling.

```python
try:
    marks = int(input("Enter marks: "))
except ValueError:
    print("Invalid input")
```

**What is it?**

Exception handling allows a program to handle runtime errors without immediately crashing.

**Important points:**

* `try` contains potentially problematic code.
* `except` handles the error.
* `ValueError` commonly occurs when converting invalid input.
* Do not use `except:` blindly.

---

### 11. Sum and Average

**Constraint:**
Initially calculate totals and averages manually.

```python
total = 0

for mark in marks:
    total += mark

average = total / len(marks)
```

**Built-in alternatives:**

```python
total = sum(marks)
average = sum(marks) / len(marks)
```

**Key lesson:**

Understand aggregation manually first, then use `sum()` when appropriate.

---

### 12. Finding Maximum and Minimum

**Constraint:**
Do not use `max()` or `min()` initially.

Manual maximum:

```python
highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
```

Manual minimum:

```python
lowest = marks[0]

for mark in marks:
    if mark < lowest:
        lowest = mark
```

**Built-in alternatives:**

```python
highest = max(marks)
lowest = min(marks)
```

**Important point:**

Manual logic teaches the comparison algorithm. Built-ins make practical code shorter and clearer.

---

### 13. Sorting

**Constraint:**
Initially understand how values can be compared and rearranged manually.

After understanding the logic, Python provides:

```python
marks.sort()
```

or:

```python
sorted_marks = sorted(marks)
```

**Difference:**

```python
marks.sort()
```

modifies the existing list.

```python
sorted(marks)
```

returns a new sorted list.

**Important point:**

Use `sorted()` when you want to preserve the original collection.

---

# Program 02 — Prediction Probability Manager

## Objective

Build a system for storing and analyzing ML prediction probabilities.

Probabilities are represented between:

```text
0 and 1
```

---

## Concepts Learned

### 1. Range Validation

**Constraint:**
Do not assume that probability input is valid.

```python
while probability < 0 or probability > 1:
    ...
```

A probability must satisfy:

```text
0 ≤ probability ≤ 1
```

**Important point:**

Range validation is extremely common in real-world data processing.

---

### 2. Continuous Input

Use a `while` loop when the number of inputs is not predetermined.

```text
Input
 ↓
Validate
 ↓
Store
 ↓
Repeat
```

This pattern appears frequently in interactive programs.

---

### 3. `EOFError`

Used to safely terminate input when an end-of-file signal is encountered.

```python
try:
    value = input()
except EOFError:
    break
```

**Important point:**

`EOFError` is different from `ValueError`.

* `ValueError` → invalid value
* `EOFError` → no more input is available

---

### 4. Threshold-Based Classification

**Constraint:**
First implement classification using `if/elif/else`.

Example:

```python
if probability >= 0.8:
    category = "Very High"
elif probability >= 0.6:
    category = "High"
elif probability >= 0.4:
    category = "Medium"
else:
    category = "Low"
```

**Important points:**

* Conditions should be ordered carefully.
* Boundary values matter.
* Threshold-based logic is widely used in ML systems.

---

### 5. Duplicate Detection

**Constraint:**
Initially detect duplicates using manual comparison instead of immediately converting everything to a set.

```python
for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] == values[j]:
            print("Duplicate found")
```

**Built-in/data-structure alternative:**

```python
unique_values = set(values)
```

**Important point:**

A set automatically stores unique values.

---

### 6. List Comprehension

Example:

```python
high_confidence = [
    probability
    for probability in probabilities
    if probability >= 0.8
]
```

**What is it?**

List comprehension provides a concise way to create a new list from an iterable.

General structure:

```python
[new_value for value in collection if condition]
```

**Important point:**

Use list comprehensions when they improve readability, not simply because they are shorter.

---

### 7. `enumerate()`

Instead of manually maintaining a counter:

```python
rank = 1

for value in values:
    print(rank, value)
    rank += 1
```

Python provides:

```python
for rank, value in enumerate(values, start=1):
    print(rank, value)
```

**Key lesson:**

Learn the manual approach first, then use `enumerate()` to make iteration cleaner.

---

### 8. Sorting

**Manual learning:** Understand comparison and swapping.

**Built-in alternative:**

```python
sorted_values = sorted(values, reverse=True)
```

or:

```python
values.sort(reverse=True)
```

---

# Program 03 — Customer Purchase History Manager

## Objective

Build a customer purchase management system that demonstrates how raw customer information can be validated, cleaned, stored, searched, classified, and analyzed.

---

## Concepts Learned

### 1. Structured Records

Customer information can be represented as:

```python
[
    customer_id,
    customer_name,
    customer_email,
    purchase_amount
]
```

Multiple records can then be stored inside a list.

This introduces the idea of representing real-world entities using Python data structures.

---

### 2. String Cleaning

**Constraint:**
First understand how unwanted spaces and inconsistent capitalization affect data.

Example:

```python
name = "   hariom    tiwari "
```

Cleaning can be performed using:

```python
" ".join(name.strip().title().split())
```

This demonstrates three useful operations:

```text
strip()
 ↓
Remove outer whitespace

split()
 ↓
Separate words

join()
 ↓
Reconstruct normalized text
```

**Important points:**

* Real-world data is often inconsistent.
* Cleaning should happen before analysis.
* Normalization makes searching and comparison more reliable.

---

### 3. Generated IDs

Formatted strings can be used to generate consistent identifiers.

```python
customer_id = f"CUS{number:03d}"
```

Examples:

```text
CUS001
CUS002
CUS003
```

**Important concept:**

Formatted strings allow values to be embedded cleanly inside text.

---

### 4. Duplicate Detection

**Constraint:**
First understand duplicate detection using comparisons.

Later, sets and dictionaries can provide more efficient approaches depending on the requirement.

**Key idea:**

Duplicates can be identified using a unique attribute such as:

```text
Email
Customer ID
Phone number
```

---

### 5. Searching

**Constraint:**
Initially search manually using a loop.

```python
for customer in customers:
    if customer[1] == search_name:
        print(customer)
```

Built-in alternatives may include:

```python
search_name in names
```

or more advanced approaches using:

```python
next()
```

and comprehensions.

**Key lesson:**

The correct search technique depends on the data structure and the problem.

---

### 6. Boolean Flags

A Boolean variable can track whether something has been found.

```python
found = False
```

When a match is found:

```python
found = True
```

After the search:

```python
if not found:
    print("Customer not found")
```

**Important point:**

Boolean flags are simple but powerful tools for controlling program flow.

---

### 7. Classification

Customers can be classified based on purchase amount.

```text
Purchase Amount
      ↓
Threshold
      ↓
Customer Category
```

This reinforces conditional logic and threshold-based classification.

---

### 8. Revenue Calculation

Manual calculation:

```python
total_revenue = 0

for customer in customers:
    total_revenue += customer[3]
```

Built-in alternative:

```python
total_revenue = sum(customer[3] for customer in customers)
```

The second approach introduces a **generator expression**.

---

### 9. Ranking

**Constraint:**
Initially understand ranking through comparison and swapping.

Later:

```python
ranked_customers = sorted(
    customers,
    key=lambda customer: customer[3],
    reverse=True
)
```

This introduces:

* `sorted()`
* `key=`
* `lambda`
* `reverse=True`

These concepts will become increasingly important later.

---

# Program 04 — Product Inventory Management

## Objective

Build an inventory management system using dictionaries and nested dictionaries.

---

## Concepts Learned

### 1. Dictionaries

**Constraint:**
Understand key-value storage before using advanced data structures.

```python
products = {}
```

A dictionary stores information in:

```text
key → value
```

Example:

```python
products["P001"] = "Laptop"
```

**Important points:**

* Keys must be unique.
* Values can contain almost any Python object.
* Dictionaries provide fast key-based lookup.

---

### 2. Nested Dictionaries

A product can contain multiple attributes:

```python
products["P001"] = {
    "Name": "Laptop",
    "Category": "Electronics",
    "Price": 50000,
    "Stock": 10
}
```

This creates structured data similar to a record in a database.

---

### 3. Dictionary Membership

```python
if product_id in products:
    ...
```

This is preferred over manually searching through every product when the key itself identifies the record.

---

### 4. `.items()`

Used to iterate over keys and values:

```python
for product_id, details in products.items():
    print(product_id, details)
```

Related methods:

```python
products.keys()
products.values()
products.items()
```

---

### 5. Calculated Fields

Inventory analysis involves calculations such as:

```text
Remaining Stock
= Stock Quantity - Units Sold
```

and:

```text
Revenue
= Units Sold × Price
```

**Key lesson:**

Stored data and calculated data do not always need to be the same thing.

---

### 6. Category Analysis

Products can be grouped by category.

A dictionary can be used as a frequency counter:

```python
category_count = {}

for product in products.values():
    category = product["Category"]

    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1
```

**Built-in alternative:**

Later, this can be simplified using:

```python
from collections import Counter
```

and:

```python
Counter(categories)
```

---

### 7. Stock Classification

Use thresholds to classify inventory:

```text
High Stock
Medium Stock
Low Stock
Out of Stock
```

This reinforces conditional logic in a business context.

---

### 8. Ranking Products

**Manual approach:** Compare revenue values and swap records.

**Built-in approach:**

```python
sorted(
    products.items(),
    key=lambda item: item[1]["Revenue"],
    reverse=True
)
```

This introduces sorting structured data using a custom key.

---

# Program 05 — Student Attendance Analyzer

## Objective

Analyze student attendance across multiple classes and identify common, unique, and absent students.

---

## Concepts Learned

### 1. Sets

**Constraint:**
Initially understand duplicate handling and dataset comparison before relying on sets.

A set is an unordered collection of unique values.

```python
students = {"A", "B", "C"}
```

**Important points:**

* Duplicate values are automatically removed.
* Sets do not maintain normal list-style indexing.
* Sets are excellent for membership testing and comparison.

---

### 2. Duplicate Removal

Manual approach:

```python
unique_students = []

for student in students:
    if student not in unique_students:
        unique_students.append(student)
```

Built-in/data-structure approach:

```python
unique_students = set(students)
```

**Key lesson:**

Use manual logic to understand the problem; use a set when uniqueness is the actual requirement.

---

### 3. Set Union

Combines values from both sets.

```python
all_students = class_a | class_b
```

or:

```python
class_a.union(class_b)
```

Conceptually:

```text
A ∪ B
```

---

### 4. Set Intersection

Finds values common to both sets.

```python
common_students = class_a & class_b
```

or:

```python
class_a.intersection(class_b)
```

Conceptually:

```text
A ∩ B
```

---

### 5. Set Difference

Finds values present in one set but not another.

```python
only_a = class_a - class_b
```

Conceptually:

```text
A - B
```

---

### 6. Symmetric Difference

Finds values present in exactly one of the two sets.

```python
different_students = class_a ^ class_b
```

This is useful when comparing two datasets.

---

### 7. Finding Missing Records

If:

```python
all_students
```

contains every student and:

```python
present_students
```

contains students who attended, then:

```python
absent_students = all_students - present_students
```

This is a very useful data-analysis pattern:

```text
Complete Dataset
      -
Observed Dataset
      =
Missing Records
```

---

### 8. Set Membership

Instead of manually searching through a list:

```python
if student in students:
    ...
```

Sets are particularly useful for membership testing.

---

# Program 06 — ML Configuration Manager

## Objective

Build a configuration management system for Machine Learning model experiments.

Each configuration contains information such as:

```text
Model Name
Hyperparameter
Random State
```

---

## Concepts Learned

### 1. Tuples

**Constraint:**
Understand fixed collections before converting everything into dictionaries or custom objects.

Example:

```python
configuration = (
    model_name,
    hyperparameter,
    random_state
)
```

A tuple is an ordered and immutable collection.

**Important points:**

* Tuples are immutable.
* Tuples support indexing.
* They are useful for representing fixed groups of related values.

---

### 2. List of Tuples

Multiple configurations can be stored as:

```python
configurations = [
    ("Model A", 0.1, 42),
    ("Model B", 0.5, 42)
]
```

This creates a simple structured dataset.

---

### 3. Frequency Counting

**Constraint:**
Initially build the counting logic manually.

```python
model_count = {}

for configuration in configurations:
    model = configuration[0]

    if model in model_count:
        model_count[model] += 1
    else:
        model_count[model] = 1
```

Built-in alternative:

```python
from collections import Counter

model_count = Counter(
    configuration[0]
    for configuration in configurations
)
```

**Key lesson:**

Dictionaries teach the underlying counting mechanism; `Counter` provides a specialized tool for the same task.

---

### 4. `None`

`None` represents the absence of a value.

```python
first_configuration = None
```

It is different from:

```python
0
""
False
```

**Important point:**

Use `None` when a value has not been found, has not been assigned, or intentionally represents no value.

---

### 5. Searching Configurations

**Manual approach:**

```python
for configuration in configurations:
    if configuration[0] == model_name:
        ...
```

Later, this can be simplified with comprehensions:

```python
matches = [
    configuration
    for configuration in configurations
    if configuration[0] == model_name
]
```

---

### 6. Duplicate Configuration Detection

Two configurations can be compared field by field.

```python
if configuration_1 == configuration_2:
    print("Duplicate")
```

Because tuples support equality comparison, Python can compare the complete tuple directly.

---

### 7. Copying Lists

```python
ranked_configuration = configurations.copy()
```

creates a separate list containing the same elements.

**Important point:**

For nested mutable structures, `.copy()` performs a **shallow copy**.

Deeper copying requires:

```python
import copy

copy.deepcopy(data)
```

This distinction becomes important when working with complex datasets.

---

### 8. Ranking Configurations

**Constraint:**
First implement ranking manually using comparisons and swapping.

Later, Python provides:

```python
sorted(
    configurations,
    key=lambda configuration: configuration[1],
    reverse=True
)
```

This introduces one of the most useful Python patterns for data processing:

```text
sorted()
+
key=
+
lambda
```

---

### 9. Lambda Functions

A lambda is a small anonymous function.

Example:

```python
lambda configuration: configuration[1]
```

It means:

```text
Take a configuration
       ↓
Return its second element
```

This allows `sorted()` to know which value should be used for ranking.

---

# Concepts Learned So Far

After six programs, the following concepts have been practiced.

## Python Fundamentals

* Variables
* Data types
* Type conversion
* User input
* Operators
* Boolean values
* Conditional statements
* `if`
* `elif`
* `else`

## Loops

* `for`
* `while`
* Nested loops
* `break`
* `continue`

## Collections

* Lists
* Nested lists
* Tuples
* Dictionaries
* Nested dictionaries
* Sets

## List Operations

* Indexing
* Iteration
* `append()`
* `copy()`
* `sort()`
* List comprehension

## String Operations

* `strip()`
* `split()`
* `join()`
* `title()`
* String normalization
* Formatted strings / f-strings

## Dictionary Operations

* Creating dictionaries
* Key-value pairs
* Lookup
* Membership testing
* `.keys()`
* `.values()`
* `.items()`
* Frequency counting
* Nested dictionaries

## Set Operations

* Creating sets
* Duplicate removal
* Union
* Intersection
* Difference
* Symmetric difference
* Membership testing

## Exception Handling

* `try`
* `except`
* `ValueError`
* `EOFError`

## Built-ins and Pythonic Alternatives

* `len()`
* `sum()`
* `min()`
* `max()`
* `sorted()`
* `.sort()`
* `enumerate()`
* `set()`
* `Counter`
* `next()`
* List comprehensions
* Generator expressions
* `lambda`

## Problem-Solving Techniques

* Input validation
* Data cleaning
* Searching
* Aggregation
* Classification
* Duplicate detection
* Frequency counting
* Dataset comparison
* Ranking
* Manual sorting
* Swapping
* Boolean flags
* Structured data representation

---

# Manual Logic vs Python Built-ins

One of the major goals of this journey is understanding the difference between **learning an algorithm** and **writing practical Python code**.

| Concept           | Learn Manually        | Python Alternative              |
| ----------------- | --------------------- | ------------------------------- |
| Maximum           | Loop + comparison     | `max()`                         |
| Minimum           | Loop + comparison     | `min()`                         |
| Sum               | Loop + accumulator    | `sum()`                         |
| Sorting           | Comparison + swapping | `sorted()` / `.sort()`          |
| Counting          | Dictionary            | `Counter`                       |
| Duplicate removal | Manual comparison     | `set()`                         |
| Ranking           | Manual comparison     | `sorted(key=...)`               |
| Index + value     | Manual counter        | `enumerate()`                   |
| Filtering         | Loop + append         | List comprehension / `filter()` |
| Transformation    | Loop + append         | List comprehension / `map()`    |
| Searching         | Manual loop           | `in`, `next()`, comprehensions  |

### Learning Rule

> **Do not memorize the built-in without understanding the problem it solves.**

The objective is:

```text
Understand the logic
        ↓
Implement it manually
        ↓
Recognize the pattern
        ↓
Learn Python's built-in solution
        ↓
Use the appropriate approach
```

---

# Data Processing Pattern Learned

Across the first six programs, a common pattern is emerging:

```text
INPUT
  ↓
VALIDATION
  ↓
CLEANING
  ↓
STORAGE
  ↓
PROCESSING
  ↓
ANALYSIS
  ↓
CLASSIFICATION
  ↓
SEARCH / COMPARISON / RANKING
  ↓
OUTPUT
```

This pattern is directly relevant to Data Science.

Real-world data is rarely ready for analysis immediately.

---

# Data Structure Progression

The journey has gradually introduced different ways of representing data.

```text
Simple Values
      ↓
Lists
      ↓
Nested Lists
      ↓
Tuples
      ↓
Dictionaries
      ↓
Nested Dictionaries
      ↓
Sets
```

The goal is not to memorize every data structure.

The goal is to understand:

> **Which data structure is appropriate for which problem?**

---

# Connection to Data Science & Machine Learning

These programs are intentionally moving toward Data Science concepts.

The progression is:

```text
Core Python
     ↓
Data Structures
     ↓
Data Validation
     ↓
Data Cleaning
     ↓
Data Processing
     ↓
Data Analysis
     ↓
Experiment Configuration
     ↓
NumPy
     ↓
Pandas
     ↓
EDA
     ↓
Machine Learning
```

The first six programs already introduce several ideas that appear in real Data Science workflows:

* Data cleaning
* Missing data concepts
* Duplicate detection
* Dataset comparison
* Aggregation
* Classification
* Ranking
* Configuration management
* Structured data
* Frequency analysis

---

# Program Progression

The difficulty will increase throughout the 20 programs.

```text
Programs 01–05
Core Python + Collections
        ↓
Programs 06–10
Advanced Python + Data Processing
        ↓
Programs 11–15
Functions + Files + OOP + Advanced Concepts
        ↓
Programs 16–20
Data-Oriented Python + ML-Oriented Problems
```

The exact concepts will be introduced through the problems rather than treated as isolated theory.

---

# Revision Checklist

For every completed program, the following questions should be answerable:

* [ ] What problem does the program solve?
* [ ] What data structures were used?
* [ ] Why were those data structures chosen?
* [ ] What Python concepts were introduced?
* [ ] Can I explain each concept without looking at the code?
* [ ] Can I implement the important logic manually?
* [ ] Do I know the relevant Python built-in alternative?
* [ ] Do I know when to use the built-in?
* [ ] Can I modify the program without copying the original logic?
* [ ] Can I solve a similar problem independently?

---

# Final Goal

By completing all 20 programs, the goal is to become comfortable with Python to the point where I can:

* Solve programming problems independently
* Choose appropriate data structures
* Write clean and readable Python
* Validate and clean data
* Process structured datasets
* Perform basic analysis
* Understand Python built-ins and when to use them
* Write reusable code
* Understand Pythonic approaches
* Work comfortably with Python before moving into NumPy and Pandas
* Apply Python concepts to Data Science and Machine Learning problems

---

# Progress Tracker

* [x] Program 01 — Student Marks Analyzer
* [x] Program 02 — Prediction Probability Manager
* [x] Program 03 — Customer Purchase History Manager
* [x] Program 04 — Product Inventory Management
* [x] Program 05 — Student Attendance Analyzer
* [x] Program 06 — ML Configuration Manager
* [ ] Program 07
* [ ] Program 08
* [ ] Program 09
* [ ] Program 10
* [ ] Program 11
* [ ] Program 12
* [ ] Program 13
* [ ] Program 14
* [ ] Program 15
* [ ] Program 16
* [ ] Program 17
* [ ] Program 18
* [ ] Program 19
* [ ] Program 20

---

## Repository Philosophy

> **Don't just learn how Python does something. Understand how the problem itself is solved, implement the logic manually, and then learn how Python lets you solve it better.**

**6 / 20 completed — 30%**
