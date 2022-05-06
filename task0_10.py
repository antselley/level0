def common_letters(string1, string2):
    return_list = []
    for char in string1:
        if char.lower() in string2.lower() and return_list.count(char.lower()) == 0: 
            return_list.append(char.lower())
    print("Common letters:", ",".join(return_list))
    
common_letters("House", "Computers")
common_letters("House", "School")
