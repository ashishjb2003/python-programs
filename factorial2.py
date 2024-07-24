def count_character_frequency(s):
    frequency_dict = {}

    for char in s:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

input_string = "hello"
frequency = count_character_frequency(input_string)
print(frequency)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
