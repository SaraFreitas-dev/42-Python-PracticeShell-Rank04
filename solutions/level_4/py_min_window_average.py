def min_window_average(nums: list[int], k: int) -> int:
    if not nums or k <= 0 or k > len(nums):
        return -1
    
    smallest: int = sum(nums[:k]) + 1
    index: int = -1

    for i in range(len(nums)):
        size: int = i + k
        if size > len(nums):
            break
        window_sum: int = sum(nums[i:size])
        if window_sum < smallest:
            smallest = window_sum
            index = i
    return index


if __name__ == "__main__":
    print(min_window_average([4, 2, 1, 3, 5], 2))  # 1
    print(min_window_average([3, 7, 90, 20, 10, 50, 40], 3))  # 3
    print(min_window_average([1, 1, 1], 2))  # 0
    print(min_window_average([5], 1))  # 0
    print(min_window_average([1, 2], 3))  # -1
    print(min_window_average([], 1))  # -1
