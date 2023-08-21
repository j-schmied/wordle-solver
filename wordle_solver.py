import argparse
import os


def load_words(language: str, length: int):
    word_file = "de.txt" if language == "de" else "en.txt"

    with open(os.path.join("word_lists", word_file)) as _word_file:
        valid_words = set(_word_file.read().split())

    return [word for word in valid_words if len(word) == length]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", "-l", type=int, required=True)
    parser.add_argument("--language", "-L", type=str, choices=["en", "de"], default="de")
    return parser.parse_args()


def main():
    args = parse_args()
    valid_words = load_words(args.language, args.length)

    input_words = list()
    input_word = None

    print("-"*50)
    print("WORDLE SOLVER")
    print("-"*50)
    print("Enter words inserted, one per line. Enter an empty line to finish.")
    print("Comma separated, enter the correctness template.\n")
    print("Use:\t- to indicate a wrong letter\n\to to indicate a correct letter in the wrong location\n\tx to indicate a correct letter in the correct location")
    print("\nExample: musik, ooxo-")
    print("-"*50, "\n")

    # Get input words
    while input_word != "":
        input_word = input()

        if input_word != "":
            input_words.append(input_word)

    # Parse input words
    correct_letters_right_location = list()
    correct_letters_wrong_location = list()

    for word in input_words:
        word, pattern = word.split(",")
        word, pattern = word.strip(), pattern.strip()

        for idx, p in enumerate(pattern):
            if p not in ["-", "o", "x"] or len(pattern) != len(word):
                raise ValueError("Invalid pattern")

            if p == "x":
                correct_letters_right_location.append((word[idx], idx))
            if p == "o":
                correct_letters_wrong_location.append(word[idx])

    correct_letters_right_location = set(correct_letters_right_location)
    correct_letters_wrong_location = set(correct_letters_wrong_location)

    # Filter words
    possible_words = list()

    for word in valid_words:
        match = True
        for letter, idx in correct_letters_right_location:
            if word[idx] != letter:
                match = False

        if not correct_letters_wrong_location.issubset(set(word)):
            match = False

        if match:
            possible_words.append(word)

    print("-"*50)
    print("SOLUTION")
    print("-"*50)

    for word in sorted(possible_words):
        print(word.upper())

    return 0


if __name__ == "__main__":
    main()

