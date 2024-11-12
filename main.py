from converter import text_to_morse, morse_to_text

def main():
    """Main program logic."""
    choice = input("Enter 1 for Text to Morse \nEnter 2 for Morse to Text \nYour choice:  ")

    if choice == '1':
        text = input("Enter text: ")
        print("Morse Code:", text_to_morse(text))
    elif choice == '2':
        morse = input("Enter Morse code (space between letters, / for space between words): ")
        print("Text:", morse_to_text(morse))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
