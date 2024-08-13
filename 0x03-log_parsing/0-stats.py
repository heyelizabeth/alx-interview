#!/usr/bin/python3
import sys
import re
from collections import defaultdict
from signal import signal, SIGINT
from sys import exit


def signal_handler(signal_received, frame):
    """ Handle SIGINT (CTRL+C) """
    print_stats()
    exit(0)

def print_stats():
    """ Print the collected statistics """
    global file_size, status_codes

    print("File size: {}".format(file_size))
    for status_code in sorted(status_codes):
        print("{}: {}".format(status_code, status_codes[status_code]))

def process_line(line):
    """ Process a single log line """
    global file_size, status_codes

    # Regex pattern to match the log line format
    pattern  = r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)

    if match:
        ip_address, status_code, file_size_value = match.groups()
        status_code = int(status_code)
        file_size_value = int(file_size_value)
        
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status_code] += 1
            file_size += file_size_value

def main():
    """ Main function to read input and print statistics """
    global file_size, status_codes

    # Initialize statistics
    file_size = 0
    status_codes = defaultdict(int)

    # Set up signal handling
    signal(SIGINT, signal_handler)

    line_count = 0

    try:
        for line in sys.stdin:
            process_line(line.strip())
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        # Handle the end of the input (CTRL+C)
        print_stats()


if __name__ == "__main__":
    main()
