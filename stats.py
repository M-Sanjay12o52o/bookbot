def get_num_words(string):
  words = string.split()
  length = len(words)

  return length

def get_char_count(string):
  char_count_dict = {}
  for word in string:
    for char in word:
      if char.lower() in char_count_dict:
        char_count_dict[char.lower()] += 1
      else:
        char_count_dict[char.lower()] = 1

  return char_count_dict

def myFunc(e):
  return e["count"]

def get_sorted_list(input_dict):
  list_of_dict = []

  for char, count in input_dict.items():
    if char.isalpha():
      list_of_dict.append({"char": char, "count": count})

  return sorted(list_of_dict, key=myFunc, reverse=True)