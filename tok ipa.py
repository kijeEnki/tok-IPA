import re

def tok_IPA(word: str):
    word = word.lower()

    # punctuation
    word = re.sub(r"[,:;]", r" |", word)
    word = re.sub(r"[.!?]", r"", word)

    # coda N
    word = re.sub(r"n([mnptkswlj]|\b)", r"N\1", word)

    # syl. breaks
    word = re.sub(r"([aeiou])([mptkswlj])", r"\1.\2", word)
    word = re.sub(r"N\b", r"n", word)
    word = re.sub(r"N\B", r"n.", word)

    # stress
    word = re.sub(r"( |^)", r"\1ˈ", word)
    word = re.sub(r"ˈ\|", r"|", word)

    # formed IPA
    word = "/" + word + "/"
    return(word)

# def test(words: dict):
#     passed = 0
#     for word in words:
#         if tok_IPA(word) == words[word]:
#             print("✓")
#             passed += 1
#         else:
#             print("✗")
#     print(f"{passed} out of {words.__len__()} tests passed.")
        
# tok_IPA("jan Sonja li toki e ni: kijetesantakalu tonsi li lanpan e soko anu seme?")