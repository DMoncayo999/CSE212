class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(string):
    stack = Stack()
    reversed_string = ""

    # Push each character onto the stack
    for char in string:
        stack.push(char)

    # Pop characters from the stack to reverse the string
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python"))  # Output: "nohtyp"
print(reverse_string("stacks"))  # Output: "skcats"