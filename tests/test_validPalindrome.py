from src.validPalindrome import Solution

def test_validPalindrome():
    test_cases = [
        ("aba", True), 
        ("abca", True), 
        ("abc", False) 
    ] 
    solution = Solution()
    for s, output in test_cases: 
        assert solution.validPalindrome(s) == output
