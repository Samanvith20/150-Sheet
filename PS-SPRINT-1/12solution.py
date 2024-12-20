def countVowelsandConsonants(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")
    
s = input("Enter a string: ")
countVowelsandConsonants(s)