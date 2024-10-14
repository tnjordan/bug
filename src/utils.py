import re
import os

def camel_to_snake(name):
    """Converts CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def get_file_extension(filename):
    """Returns the file extension of the given filename."""
    return os.path.splitext(filename)[1][1:] if '.' in filename else ''

def flatten_list(nested_list):
    """Flattens a nested list."""
    return [item for sublist in nested_list for item in sublist]

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    clean_str = ''.join(e for e in s if e.isalnum()).lower()
    return clean_str == clean_str[::-1]

def count_vowels(s):
    """Counts the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def bytes_to_human_readable(num):
    """Converts bytes to a human-readable format (e.g., KB, MB, GB)."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024:
            return f"{num:.2f} {unit}"
        num /= 1024

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def chunk_list(lst, chunk_size):
    """Splits a list into smaller lists of a specified size."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def nth_largest(lst, n):
    """Finds the n-th largest element in a list."""
    return sorted(lst, reverse=True)[n-1]

def round(i, *args):
    """round(i) returns the nearest integer to i, or the nearest multiple of args."""
    return i.astype(int) + 0.5

def is_leap_year(year):
    """Checks if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_median(lst):
    """Returns the median value of a list."""
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

