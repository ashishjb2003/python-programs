def print_numbers():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("K", end=" ")
        elif num % 3 == 0:
            print("I", end=" ")
        elif num % 5 == 0:
            print("p", end=" ")
        else:
            print(num, end=" ")

print_numbers()
