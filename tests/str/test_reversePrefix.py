from str.reversePrefix import reversePrefix

def test_reversePrefix():
    test_cases = [
        ("abcdefd", "d", "dcbaefd"), 
        ("xyxzxe", "z", "zxyxxe"), 
        ("abcd", "z", "abcd")
    ]
    for word, ch, output in test_cases: 
        assert reversePrefix(word, ch) == output