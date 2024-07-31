#!/usr/bin/python3

"""
Determines if all lockboxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all lockboxes can be unlocked.

    Args:
      boxes (list): A list of lists representing the lockboxes.
      Each inner list contains the keys to other lockboxes.

    Returns:
      bool: True if all lockboxes can be unlocked, False otherwise.
    """

    def dfs(lockbox):
        if visited[lockbox]:
            return
        visited[lockbox] = True
        for key in boxes[lockbox]:
            dfs(key)

    n = len(boxes)
    visited = [False] * n
    dfs(0)

    return all(visited)
