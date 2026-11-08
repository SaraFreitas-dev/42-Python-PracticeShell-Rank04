def longest_unique_substring(s: str) -> int:
    if not s:
        return 0
    longest_s: int = 1
    seen: set[str] = set()
    left: int = 0

    seen.add(s[0])
    for right in range(1, len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest_s = max(longest_s, len(seen))
    return longest_s


if __name__ == "__main__":
    print(longest_unique_substring("abcabcbb"))  # 3
    print(longest_unique_substring("bbbbb"))  # 1
    print(longest_unique_substring("pwwkew"))  # 3
    print(longest_unique_substring("dvdf"))  # 3
    print(longest_unique_substring("abba"))  # 2
    print(longest_unique_substring("abcdef"))  # 6
    print(longest_unique_substring(""))  # 0
