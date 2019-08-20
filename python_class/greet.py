import sys
import argparse

def greet(text="World",phrase=''):
    if not text:
        text = "World"
        print(text)
    if phrase:
        print(phrase)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text',nargs='?',help = "text to output after Hello")
    args = parser.parse_args()
    greet(args.text)
#    if args.text:
#        greet(args.text)