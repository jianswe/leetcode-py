from src.isPalindrome import Solution

def test_isPalindrome():
    test_cases = [
        ("A man, a plan, a canal: Panama", True), 
        ("race a car", False), 
        (" ", True)
    ]
    solution = Solution()
    for s, output in test_cases: 
        assert solution.isPalindrome(s) == output
