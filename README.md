# Pentext-editor
Usage: <command> <input file>
Use a basic txt file as input,
and provide it a list of terms which may have duplicates and be blank.
It will count them and give you a list sorted in descending order.

This script:
1. Takes a user file as input in the second position on the CLI after the command,
2. Tells you to input a file if you didn't, and exits,
3. Stores the lines in the file in a dictionary and counts the occurrences of each line,
4. Allows/counts blank lines but uses "::blank::" as a placeholder term,
5. Sorts dictionary entries by number of occurrences, and
6. Prints to standard output what it found.

I used this script to learn python and
count the number of passwords in a dump
file to discover the top passwords by occurrence.
