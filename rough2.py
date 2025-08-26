def vowels(text):
    count = 0
    vow = ["a", "e", "i", "o", "u"]
    for char in text.lower():  # convert to lowercase to handle uppercase too
        if char in vow:
            count += 1
    return count

text = "hello world"
print("Vowels in the string:", vowels(text))
