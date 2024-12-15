#!/usr/bin/python3
'''
A module to read stdin line by line and compute metrics
'''
import sys


# Initialize variables
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
valid_status_codes = set(status_codes_count.keys())


def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract the file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update metrics
            total_size += file_size
            if status_code in valid_status_codes:
                status_codes_count[status_code] += 1
        except (ValueError, IndexError):
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interruption
    print_stats()
    raise

# Print stats at the end of input
print_stats()
