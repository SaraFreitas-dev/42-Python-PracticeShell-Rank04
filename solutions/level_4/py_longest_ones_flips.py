def longest_ones_flips(nums: list[int], k: int) -> int:
    if not nums:
        return 0
    if k < 0:
        k = 0

    zero_counter: int = 0
    res: int = 0
    left: int = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_counter += 1
        while zero_counter > k:
            if nums[left] == 0:
                zero_counter -= 1
            left += 1
        if (right - left + 1) > res:
            res = right - left + 1

    return res


if __name__ == "__main__":
    print(longest_ones_flips([1, 1, 0, 0, 1, 1, 1, 0, 1], 1))  # 5
    print(longest_ones_flips([1, 1, 0, 0, 1, 1, 1, 0, 1], 2))  # 7
    print(longest_ones_flips([0, 0, 0], 2))  # 2
    print(longest_ones_flips([1, 1, 1], 0))  # 3
    print(longest_ones_flips([0, 1, 0], 0))  # 1
    print(longest_ones_flips([], 3))  # 0
