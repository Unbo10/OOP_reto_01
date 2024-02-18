def is_palindrome(s: str) -> bool:
    n: int = (len(s) // 2)
    i: int = 0
    count: int = 0
    while i < n:
        if s[i] == s[len(s) - i - 1]:
            count += 1
        i += 1
    return count == n

if __name__ == "__main__":
    word: str = input("Enter a string: ")
    if (is_palindrome(word)):
        print("The word {} is a palindrome.".format(word))
    else:
        print("The word {} is not a palindrome.".format(word))