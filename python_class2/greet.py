"""Module greet contains function greet"""
import sys
import argparse

def greet(text="World", phrase=''):
    """Prints Hello {text} and if phrase, prints it on another line"""
    if not text:
        text = "World"
    print(f"Hello {text}!")
    if phrase:
        print(phrase)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text', nargs='?', help="Text to output after Hello")
    parser.add_argument('-p','--phrase', nargs='?', help="Phrase to print on next line")
    args = parser.parse_args()
    greet(args.text, args.phrase)
