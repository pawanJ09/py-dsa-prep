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

