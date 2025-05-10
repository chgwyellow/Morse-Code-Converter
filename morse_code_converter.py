# Morse Code Rule
# The length of a dot is one unit.
# A dash is three units.
# The space between parts of the same letter is one unit.
# The space between letters is three units.
# The space between words is seven units.

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

input_msg = input("Morse Code Converter\nType text to convert to Morse Code!\n")
output_list = []