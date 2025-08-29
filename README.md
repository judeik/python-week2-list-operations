# Python Week 2 Assignment - List Operations

## Description
This repository contains the solution for Week 2 Python assignment focused on **list operations**.  
The goal is to practice Python list methods such as `append()`, `insert()`, `extend()`, `pop()`, `sort()`, and `index()` while writing clean and efficient code.

---

## Assignment Instructions
1. Create an empty list called `my_list`.  
2. Append the elements `10, 20, 30, 40` to `my_list`.  
3. Insert the value `15` at the second position in the list.  
4. Extend `my_list` with another list: `[50, 60, 70]`.  
5. Remove the last element from `my_list`.  
6. Sort `my_list` in ascending order.  
7. Find and print the index of the value `30` in `my_list`.

---

## Solution Code
```bash
# Week Two Assignment - Python List Operations

# Step 1: Create an empty list
my_list = []

# Step 2: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()  # removes 70

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

# Optional: Print the final list
print("Final sorted list:", my_list)
```