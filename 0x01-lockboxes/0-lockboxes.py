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

    opened = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < len(boxes):
                    stack.append(key)

    return len(opened) == len(boxes)
