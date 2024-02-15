def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_chars = get_count_chars(text)
    list = dict_to_list(count_chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for letter in list:
        print(f"The '{letter['character']}' chcarecter was found {letter['num']} times")

    print("--- End report ---")
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_chars(text):
    counts = {}
    low = text.lower()
    for c in low:
        try:
            counts[c] += 1
        except KeyError:
            counts[c] = 1
    return counts

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    list = []
    for k in dict:
        list.append({"character": k,
                     "num": dict[k]})
    list.sort(reverse=True, key=sort_on)
    return list
    

main()