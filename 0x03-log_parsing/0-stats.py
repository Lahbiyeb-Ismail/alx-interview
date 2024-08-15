#!/usr/bin/python3

"""
This function prints the file size and the count of each status code.
It takes no arguments and has no return value
"""

import re
import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

# Regular expression to match the log line format
log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_statistics():
    """Print the statistics.

    This function prints the file size and the count of each status code.
    It takes no arguments and has no return value.

    Example usage:
    >>> print_statistics()
    File size: 1024
    200: 10
    404: 5
    500: 2
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    pass
finally:
    # Print final statistics
    print_statistics()
