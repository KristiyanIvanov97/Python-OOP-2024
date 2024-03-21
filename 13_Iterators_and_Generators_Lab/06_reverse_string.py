def reverse_text(string):
    curr_index = len(string) - 1
    while curr_index >= 0:
        yield string[curr_index]
        curr_index -= 1


for char in reverse_text("step"):
    print(char, end='')
