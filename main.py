def main():
    book_path = "books/frankestein.txt"
    book = get_book(book_path)
    words = total_words(book)
    characters = count_char(book)
    list = convert_to_list(characters)
    list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document\n")
    for d in list:
        print(f"The '{d["name"]}' character was found {d["num"]} times")
    print("--- End report ---")

def get_book(path):
    with open(path) as f:
        return f.read()

def total_words(book):
    words = book.split()
    return len(words)

def count_char(book):
    result = {}
    for c in book:
        if c.lower() in result:
            result[c.lower()] += 1
        else:
            result[c.lower()] = 1
    return result

def convert_to_list(dict):
    list = []
    for c in dict:
        if c.isalpha():
            list.append({"name": c, "num": dict[c]})
    return list
    
def sort_on(dict):
    return dict["num"]
        
main()