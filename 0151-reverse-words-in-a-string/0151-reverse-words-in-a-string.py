class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_words = words[::-1]
        reversed_string = ' '.join(reverse_words)
        return reversed_string

if __name__ == "__main__":
    solution = Solution()

    s = "the sky is blue"
    x = solution.reverseWords(s)
    print(x)

    s = "  hello world  "
    cleaned_s = ' '.join(s.split())
    x = solution.reverseWords(cleaned_s)
    print(x)

    s = "a good   example"
    cleaned_s = ' '.join(s.split())
    x = solution.reverseWords(cleaned_s)
    print(x)