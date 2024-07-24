def unique_elements(lst):
    unique_set = set(lst)
    unique_list = list(unique_set)
    return unique_list
example_list = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(example_list))
