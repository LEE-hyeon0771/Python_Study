class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1-i]:
            raise NotPalindromeError
    print(word)

try:
    word = input()
    palindrome(word)

except NotPalindromeError as e:
    print(e)
