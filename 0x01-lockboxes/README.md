# Lockboxes

The Lockboxes programming problem is a classic algorithm challenge involving graphs and depth-first search (DFS) or breadth-first search (BFS).

## Problem Statement
You are given n lockboxes, each numbered sequentially from 0 to n-1. Each lockbox can contain keys to other lockboxes. The goal is to determine if all lockboxes can be opened, starting with lockbox 0, which is initially unlocked.

## Details:
### Input:

An array of lockboxes, where each lockbox contains a list of keys. Each key is represented by an integer indicating which lockbox it can open.
You start with lockbox 0 opened.
Output:

A boolean value True if all lockboxes can be opened, otherwise False.

### Example:
Consider the following input:

```
lockboxes = [[1], [2], [3], []]
```

Lockbox 0 contains a key to lockbox 1.
Lockbox 1 contains a key to lockbox 2.
Lockbox 2 contains a key to lockbox 3.
Lockbox 3 contains no keys.

Starting with lockbox 0, you can open lockbox 1, then lockbox 2, and finally lockbox 3. Therefore, the output should be True.
