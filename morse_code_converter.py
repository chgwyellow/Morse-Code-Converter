# Morse Code Rule
# 1. The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit. (AI said no)
# 4. The space between letters is three units.
# 5. The space between words is seven units. (AI said use / to indicate it)

morse_code_rules = {
    "a": "·−",
    "b": "−···",
    "c": "−·−·",
    "d": "−··",
    "e": "·",
    "f": "··−·",
    "g": "−−·",
    "h": "····",
    "i": "··",
    "j": "·−−−",
    "k": "−·−",
    "l": "·−··",
    "m": "−−",
    "n": "−·",
    "o": "−−−",
    "p": "·−−·",
    "q": "−−·−",
    "r": "·−·",
    "s": "···",
    "t": "−",
    "u": "··−",
    "v": "···−",
    "w": "·−−",
    "x": "−··−",
    "y": "−·−−",
    "z": "−−··",
    "0": "−−−−−",
    "1": "·−−−−",
    "2": "··−−−",
    "3": "···−−",
    "4": "····−",
    "5": "·····",
    "6": "−····",
    "7": "−−···",
    "8": "−−−··",
    "9": "−−−−·",
    " ": "/",
}

keep_going = True
while keep_going:
    input_msg = input(
        "Morse Code Converter\nType text to convert to Morse Code!\nEnter 'exit' to leave\n"
    ).lower()
    if input_msg == "exit":
        keep_going = False
        break

    words = input_msg.split()
    output_list = []
    previous_char = None

    for word in words:
        for char in word:
            if char not in morse_code_rules:
                print(f"There is a illegal letter: {char}\n")
                output_list = []  # clean the current result
                break  # break this loop
            # Add the char interval (Not the first letter nor the word beginning)
            if previous_char is not None:
                output_list.append(" " * 3)  # the interval is 3 units
            output_list.append(morse_code_rules[char])
            previous_char = char
        # Add the word interval while it's legal, it must occur
        else:
            output_list.append(morse_code_rules[" "])
            previous_char = None
            continue
        # break the outer loop due to the illegal char, or the remaining words will keep going.
        break

    if output_list:
        # get rid of the last / due to the else must work
        output_list.pop()
        print(f"The Morse Code is {''.join(output_list)}\n")
