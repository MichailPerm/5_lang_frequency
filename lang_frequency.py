import argparse
import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, "r") as text_file:
        text_data = text_file.read()
        return text_data


def get_most_frequent_words(text_data):
    the_most_common_words_quantity = 10
    punctuation_mark_pattern = re.compile(r"\w{1,}")
    words = punctuation_mark_pattern.findall(text_data.lower())
    return Counter(words).most_common(the_most_common_words_quantity)


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    return parser.parse_args()


if __name__ == "__main__":
    args = create_args_parser()
    try:
        text_data = load_data(args.filepath)
    except IOError:
        sys.exit("Unable to read file {}.".format(args.filepath))
    most_frequent_words = get_most_frequent_words(text_data)
    for word, count in most_frequent_words:
        print(word)
