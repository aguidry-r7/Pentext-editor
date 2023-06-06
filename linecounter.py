#! /usr/bin/python
import sys

def count_lines(file_path):
    line_counts = {}  # Dictionary to store line counts
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line == "":
                line = "::blank::"  # Replace any empty line with placeholder
            if line in line_counts:
                line_counts[line] += 1
            else:
                line_counts[line] = 1
    return line_counts

# Check if the input file is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please, provide an input file in the following format: '<command> <input file>'")
    sys.exit(1)  # Exit the script with a non-zero status code

# Get the input file from the command-line arguement
input_file_path = sys.argv[1]

# Count the occurrences of each line
line_counts = count_lines(input_file_path)

# Sort the lines by occurrence count in descending order
sorted_lines = sorted(line_counts.items(), key=lambda x: x[1], reverse=True)

# Print the lines and their counts
for line, count in sorted_lines:
    if count >= 2:
     print(f"{line} {count} occurrences")
