import sys

from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_list

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  # TODO: filepath from argv as argument for fn call
  result = get_book_text(sys.argv[1])
  return result


# TODO: filepath from argv into the string
file_path = sys.argv[1]
string = get_book_text(file_path)
total_words = get_num_words(string)
character_count = get_char_count(string)
sorted_char_counts = get_sorted_list(character_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")

for item in sorted_char_counts:
    print(f"{item['char']}: {item['count']}")

print("============= END ===============")


main()