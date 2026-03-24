def commands(binary_string):
    number = int(binary_string, 2)
    actions = ["wink", "double blink", "close your eyes", "jump"]
    handshake = []

    for i in range(4):
        if number & (1 << i):
            handshake.append(actions[i])

    if number & 16:
        handshake.reverse()

    return handshake