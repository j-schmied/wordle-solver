import argparse


def load_words():
    with open("en.txt") as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--letters", "-l", type=str, required=True)
    parser.add_argument("--length", "-L", type=int, required=True)
    parser.add_argument("--template", "-t", type=str, required=True)
    parser.add_argument("--language", "-s", type=str, choices=["en", "de"], default="de")
    return parser.parse_args()


def main():
    args = parse_args()


if __name__ == "__main__":
    main()

