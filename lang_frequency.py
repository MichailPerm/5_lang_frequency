import argparse
import re
from collections import Counter

PUNCTUATION_MARK_PATTERN = re.compile(r"\W+", re.UNICODE)
WORDS_TO_RETURN = 10


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        text_data = text_file.read()
        return text_data


def get_most_frequent_words(text_data):
    text_data_without_marks = PUNCTUATION_MARK_PATTERN.sub(text_data, " ")
    text_data_without_marks = re.sub("–", "", str(text_data_without_marks))
    text_data_list = text_data_without_marks.lower().strip().split(" ")
    for i, text_data in enumerate(text_data_list):
        if text_data == "":
            text_data_list.pop(i)
    return Counter(text_data_list).most_common(WORDS_TO_RETURN)


def create_args_parser(argument):
    parser = argparse.ArgumentParser()
    parser.add_argument(argument)
    return parser.parse_args()


if __name__ == '__main__':
    args = create_args_parser('filepath')
    try:
        text_data = load_data(args.filepath)
    except IOError:
        print("Unable to read file {}.".format(args.filepath))
    most_frequent_words = get_most_frequent_words(text_data)
    for word in most_frequent_words:
        print(word[0])
