#!/usr/bin/env python3

import sys


def longest_sub_array(arr: list[int], target: int) -> int:
    left = right = 0
    curr = 0
    max_length = 0
    while right < len(arr):
        curr += arr[right]
        if curr > target:
            curr -= arr[left]
            left += 1
        else:
            max_length = right - left + 1
        right += 1
    return max_length


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python books.py <array> <target>")
        sys.exit(1)
    arr = list(map(int, sys.argv[1].split(",")))
    target = int(sys.argv[2])
    result = longest_sub_array(arr, target)
    print(result)
