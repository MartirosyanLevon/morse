from morse_dict import MORSE_CODE_DICT, REVERSE_MORSE_CODE_DICT

def text_to_morse(text):
    """Convert text to Morse code."""
    morse_list = [MORSE_CODE_DICT.get(char, '') for char in text.upper()]
    return ' '.join(morse_list)  # Join with spaces between letters

def morse_to_text(morse):
    """Convert Morse code to text."""
    text_list = [REVERSE_MORSE_CODE_DICT.get(code, '') for code in morse.split(' ')]
    return ''.join(text_list)  # Join letters without spaces
