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

# The space between two different letters
LETTER_SEP = " " * 3

keep_going = True
while keep_going:
    input_msg = input(
        "Morse Code Converter\nType text to convert to Morse Code!\nEnter 'exit' to leave\n"
    ).lower()
    if input_msg == "exit":
        keep_going = False
        continue

    illegals = set(input_msg) - set(morse_code_rules.keys())
    if illegals:
        print(f"There are illegal letters: {', '.join(illegals)}")
        continue

    output_list = []
    previous_char = None

    for char in list(input_msg):
        # previous char is space; previous char is None; current char is equal to previous char; current char is space;
        # not need to add LETTER_SEP
        if (
            previous_char == " "
            or previous_char is None
            or char == previous_char
            or char == " "
        ):
            output_list.append(morse_code_rules[char])
        else:
            output_list.append(LETTER_SEP)
            output_list.append(morse_code_rules[char])
        previous_char = char

    print(f"The Morse Code is {''.join(output_list)}\n")
