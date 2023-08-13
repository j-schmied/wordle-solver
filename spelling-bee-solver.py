import argparse
import keyboard
import time


def load_words():
    with open("./word_lists/en.txt") as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--definitive", "-d", type=str, required=True)
    parser.add_argument("--letters", "-l", type=str, required=True)
    parser.add_argument("--autosolve", action="store_true")
    return parser.parse_args()


def main():
    english_words = load_words()
    args = parse_args()

    definitive: str = args.definitive
    letters: list = sorted(list(args.letters))
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

