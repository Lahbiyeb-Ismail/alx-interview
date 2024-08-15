#!/usr/bin/python3

import sys


def print_statistics(status_code_counts, total_file_size):
    """
    Print the statistics.

    Args:
        status_code_counts (dict): Dictionary of status codes and their counts.
        total_file_size (int): Total file size.
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


def parse_log_line(line):
    """
    Parse a log line and extract the status code and file size.

    Args:
        line (str): A single log line.

    Returns:
        tuple: (status_code, file_size) if the line is valid,
        otherwise (None, None).
    """
    parts = line.split()
    if len(parts) < 2:
        return None, None
    try:
        file_size = int(parts[-1])
        status_code = parts[-2]
        return status_code, file_size
    except ValueError:
        return None, None


total_file_size = 0
line_count = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        status_code, file_size = parse_log_line(line)
        if status_code and file_size is not None:
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1

            if line_count == 10:
                print_statistics(status_code_counts, total_file_size)
                line_count = 0

except KeyboardInterrupt:
    pass
finally:
    print_statistics(status_code_counts, total_file_size)
