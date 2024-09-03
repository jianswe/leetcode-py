def reversePrefix(word: str, ch: str) -> str:
    ind = word.find(ch)
    if ind == -1: 
        return word 
    return word[ind::-1]+word[ind+1:]