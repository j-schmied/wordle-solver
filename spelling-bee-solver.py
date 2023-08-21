import argparse
import keyboard
import os
import time


def load_words(language: str):
    word_file = "de.txt" if language == "de" else "en.txt"

    with open(os.path.join("word_lists", word_file)) as _word_file:
        valid_words = set(_word_file.read().split())

    return valid_words


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--definitive", "-d", help="Specfiy a letter that must occur in the word", type=str, required=True)
    parser.add_argument("--letters", "-l", help="Specify letters that can occur in the word", type=str, required=True)
    parser.add_argument("--language", "-L", type=str, choices=["en", "de"], default="en")
    parser.add_argument("--autosolve", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    english_words = load_words(args.language)

    definitive: str = args.definitive.lower()
    letters: list = sorted(list(args.letters.lower()))
    letters.append(definitive)

    valid_word = list()

    for word in english_words:
        if len(word) >= 4 and definitive in word:
            distinct_letters = sorted(list(set(word.lower())))

            if set(distinct_letters).issubset(set(letters)):
                valid_word.append(word)

    print("-"*50)
    print("SPELLING BEE SOLVER")
    print("-"*50)

    if args.autosolve:
        print("Starting AutoSolve")
        print("Navigate to the browser windows within 5 seconds!")
        print("-"*50)
        time.sleep(5)

    for word in sorted(valid_word):
        if args.autosolve:
            keyboard.write(word, delay=0.1)
            keyboard.press_and_release('enter')
            time.sleep(0.75)

        print(word)


if __name__ == '__main__':
    main()

