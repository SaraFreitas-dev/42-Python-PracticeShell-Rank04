def sliding_window_sum(nums: list[int], k: int) -> list[int]:
    res: list[int] = []
    if not nums or k <= 0 or k > len(nums):
        return res
    for i in range(len(nums) - k + 1):
        res.append(sum(nums[i:(i + k)]))
    return res


if __name__ == "__main__":
    print(sliding_window_sum([1, 2, 3, 4, 5], 2))  # [3, 5, 7, 9]
    print(sliding_window_sum([4, -1, 2, 7, 0], 3))  # [5, 8, 9]
    print(sliding_window_sum([5, -1, 3], 1))  # [5, -1, 3]
    print(sliding_window_sum([1, 2, 3], 3))  # [6]
    print(sliding_window_sum([1, 2], 3))  # []
    print(sliding_window_sum([], 2))  # []
    print(sliding_window_sum([1, 2, 3], 0))  # []