def palindrome(*args):
    word = args[0]
    index = args[1]
    is_palindrome = True

    for x in range(index, int(len(word)/2)):
        if word[x] == word[len(word) - x - 1]:
            palindrome(word, x + 1)
        else:
            is_palindrome = False
            break

    if is_palindrome:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))