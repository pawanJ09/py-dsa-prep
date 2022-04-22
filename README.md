# Data Structures and Algorithms

This project can be used to learn about the Data structures and algorithms concepts using Python.

## Requirements

For building and running the application you need:

- [Python3](https://www.python.org/downloads/)

```shell
pip3 install -r requirements.txt
```

## Running the application locally

You can run the main.py program to get started. This file has the __main__ method.

```shell
python main.py
```

## Data Structure Complexities

<table>
<tr>
<td></td>
<td style="text-align:center">Arrays</td>
<td style="text-align:center">Singly Linked Lists</td>
<td style="text-align:center">Doubly Linked Lists</td>
<td>Description</td>
</tr>
<tr>
<td style="text-align:center">Search</td>
<td style="text-align:center">O(1)</td>
<td style="text-align:center">O(N)</td>
<td style="text-align:center">O(N)</td>
<td>Arrays can access the elements by index but linked lists have to perform linear search.</td>
</tr>
<tr>
<td style="text-align:center">Insert at Start</td>
<td style="text-align:center">O(N)</td>
<td style="text-align:center">O(1)</td>
<td style="text-align:center">O(1)</td>
<td>Arrays have to rearrange the indexes of subsequent elements after inserting at start but 
linked lists only update the reference to head node.</td>
</tr>
<tr>
<td style="text-align:center">Insert at End</td>
<td style="text-align:center">O(1)</td>
<td style="text-align:center">O(N)</td>
<td style="text-align:center">O(1)</td>
<td>Arrays can access the last element by index. Singly Linked list has to perform linear 
search to get to the last node. Doubly linked list can directly access the last element using 
tail node.</td>
</tr>
<tr>
<td style="text-align:center">Space</td>
<td style="text-align:center">0</td>
<td style="text-align:center">O(N)</td>
<td style="text-align:center">O(2N)</td>
<td>Arrays do not need any extra space. Singly linked list need extra space for data and the 
reference to head node. Doubly linked list need extra space for data, reference to head node and 
reference to the tail node.</td>
</tr>
</table>

## Binary Trees

### Binary Trees Complexities

<table>
<tr>
<td></td>
<td style="text-align:center">Binary Search Tree</td>
<td style="text-align:center">AVL Tree</td>
<td style="text-align:center">Red Black Trees</td>
<td style="text-align:center">Description</td>
</tr>
<tr>
<td style="text-align:center">Space</td>
<td style="text-align:center">Best Case: O(N), Worst Case: O(N)</td>
<td style="text-align:center">Best Case: O(N), Worst Case: O(N)</td>
<td style="text-align:center">Best Case: O(N), Worst Case: O(N)</td>
<td style="text-align:center">All of these have similar space complexity because we need to 
store the node details.</td>
</tr>
<tr>
<td style="text-align:center">Insertion</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(N)</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(logN)</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(logN)</td>
<td>Since there is no reordering in Binary Tree the worst case space complexity goes up.</td>
</tr>
<tr>
<td style="text-align:center">Deletion</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(N)</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(logN)</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(logN)</td>
<td>Since there is no reordering in Binary Tree the worst case space complexity goes up.</td>
</tr>
<tr>
<td style="text-align:center">Search</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(N)</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(logN)</td>
<td style="text-align:center">Best Case: O(logN), Worst Case: O(logN)</td>
<td>Since there is no reordering in Binary Tree the worst case space complexity goes up.</td>
</tr>
</table>

### Binary Trees formulae:

Height of tree:
1. max(left child height, right child height) + 1
2. Leaf node's height is -1

Balance:
1. Null Node is 0
2. balance = (left child height - right child height) - 1
3. The balance has to be more than 1 for the reordering to happen. If the balance is positive 
   then it is a left heavy binary tree and if it is negative then it is a right heavy binary tree.

## Heap formulae:

### Heap Complexities:

<table>
<tr>
<td style="text-align:center">Operation</td>
<td style="text-align:center">Time complexity</td>
</tr>
<tr>
<td style="text-align:center">Find min/max</td>
<td style="text-align:center">O(1)</td>
</tr>
<tr>
<td style="text-align:center">Remove min/max</td>
<td style="text-align:center">O(logN)</td>
<tr>
<td style="text-align:center">Insert item</td>
<td style="text-align:center">O(logN)</td>
</tr>
</table>


### Heap Type Complexities:

<table>
<tr>
<td>Operation</td>
<td style="text-align:center">Binary</td>
<td style="text-align:center">Binomial</td>
<td style="text-align:center">Fibonacci</td>
<td style="text-align:center">Description</td>
</tr>
<tr>
<td style="text-align:center">Space</td>
<td style="text-align:center">O(N)</td>
<td style="text-align:center">O(N)</td>
<td style="text-align:center">O(N)</td>
<td style="text-align:center">All of these have similar space complexity because we need to 
store the heap elements.</td>
</tr>
<tr>
<td style="text-align:center">Find min</td>
<td style="text-align:center">O(1)</td>
<td style="text-align:center">O(1)</td>
<td style="text-align:center">O(1)</td>
<td>Min/Max values can be found as the root node.</td>
</tr>
<tr>
<td style="text-align:center">Delete min</td>
<td style="text-align:center">O(logN)</td>
<td style="text-align:center">O(logN)</td>
<td style="text-align:center">O(logN)</td>
<td>Since after removing root node heapify operation takes place to reorder the tree</td>
</tr>
<tr>
<td style="text-align:center">Insertion</td>
<td style="text-align:center">O(logN)</td>
<td style="text-align:center">O(1)</td>
<td style="text-align:center">O(1)</td>
<td>Since there is heapify in Binary Heap the time complexity goes up.</td>
</tr>
<tr>
<td style="text-align:center">Decrease key</td>
<td style="text-align:center">O(logN)</td>
<td style="text-align:center">O(logN)</td>
<td style="text-align:center">O(1)</td>
<td>Since there is heapify in Binary Heap the time complexity goes up.</td>
</tr>
<tr>
<td style="text-align:center">Merge</td>
<td style="text-align:center"></td>
<td style="text-align:center">O(logN)</td>
<td style="text-align:center">O(1)</td>
<td></td>
</tr>
</table>

### Heap formulae:

Find index of child nodes:
if i is the index of the root/parent node then left child = 2i+1 and right child = 2i+2

Similarly, find index of root/parent:
If i is the index of the node then from left child = (i-1)/2 and right child = (i-2)/2

