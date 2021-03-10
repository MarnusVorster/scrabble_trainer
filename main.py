"""Tool to scrabble your sentence and returns.

Usage:
python main.py "your sentence"
"""
import argparse

from scrabbler import scrabble_sentence

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        dest='sentence',
        type=str,
        help="The scrabble sentence"
    )
    args = parser.parse_args()
    result = scrabble_sentence(args.sentence)
    print(f"""     Your sentence: {args.sentence}\nScrabbled sentence: {result}""")
