def is_paired(input_string):
    pairs = {")": "(", "]": "[", "}": "{"}
    openers = pairs.values()
    stack = []

    for char in input_string:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0
