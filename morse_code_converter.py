# Morse Code Rule
# 1. The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is three units.
# 5. The space between words is seven units.

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

    input_msg_list = list(input_msg)
    output_list = []

    previous_char = " "
    for char in input_msg_list:
        if char in morse_code_rules:
            # if the space is between two words.
            if char == " ":
                output_list.append(morse_code_rules[char] * 7)
                previous_char = char
                continue
            # if the previous char is original space, skip comparison.
            elif previous_char == " ":
                output_list.append(morse_code_rules[char])
                previous_char = char
                continue
            # if the char is equal to the previous char
            elif char == previous_char:
                output_list.append(morse_code_rules[" "])
            # if the char is not the previous char
            elif char != previous_char:
                output_list.append(morse_code_rules[" "] * 3)

            output_list.append(morse_code_rules[char])
            previous_char = char
        else:
            print(f"There are illegal marks in the original input: {char}")
            exit()  # Force to leave the loop
    print(f"The Morse Code is: {output_list}\n")
