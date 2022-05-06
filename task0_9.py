def print_vowels(input_string):
    return_list = []
    for char in input_string:
        if (char.lower() in ["a", "e", "i", "o", "u"]) and (return_list.count(char.lower()) == 0) : 
            return_list.append(char.lower())
    print(",".join(return_list))

print_vowels("Umuzi")
print_vowels("supercalifragilisticexpialidocious")