def is_palindrome(word: str) -> bool:
    return (word == word[::-1])


def longest_palindrome_length(s: str) -> int:
    if not s:
        return 0
    if is_palindrome(s):
        return (len(s))
    max_p: int = 0

    for end in range(len(s) + 1):
        for start in range(end):
            if is_palindrome(s[start:end]):
                max_p = max(max_p, (end - start))
    return max_p


if __name__ == "__main__":
    print(longest_palindrome_length("babad"))  # 3
    print(longest_palindrome_length("cbbd"))  # 2
    print(longest_palindrome_length("racecar"))  # 7
    print(longest_palindrome_length("forgeeksskeegfor"))  # 10
    print(longest_palindrome_length("abc"))  # 1
    print(longest_palindrome_length(""))  # 0
