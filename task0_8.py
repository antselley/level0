def show_vowels(text):
    text = text.lower()
    print("vowels: ", end="")
    for vowel in "aeiou":
        if vowel in text:
            print(vowel,end="," )
   


show_vowels("Umuzi")