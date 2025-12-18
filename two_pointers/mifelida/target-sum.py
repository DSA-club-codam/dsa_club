#!/usr/bin/env python3

import sys
from typing import Tuple


def target_sum(nums: list[int], target: int) -> Tuple[int, int] | None:
    n_sorted = sorted(nums)
    left, right = 0, len(n_sorted) - 1
    while left < right:
        current_sum = n_sorted[left] + n_sorted[right]
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return (left, right)
    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: target-sum.py array_of_integers target_sum")
        sys.exit(1)
    nums = list(map(int, sys.argv[1].split(",")))
    target = int(sys.argv[2])
    result = target_sum(nums, target)
    if result:
        print(f"Pair found: {result[0]}, {result[1]}")
    else:
        print("No pair found")
