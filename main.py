path = "./books/frankenstein.txt"

def main():
    book_contents = get_book(path)
    word_count = get_wordcount(book_contents)
    letter_count = get_letter_count(book_contents)
    report = get_report(letter_count)
    #print(letter_count)

def get_book(path):
        with open(path) as f:
            return f.read()

def get_wordcount(file_contents):
    words = file_contents.split()
    return(len(words))

def get_letter_count(file_contents):
    alpha = {} #.split()
    for word in file_contents:
        letters = word.lower()
        letters = list(letters)
        for letter in letters:
            if letter in alpha:
                alpha[letter] = alpha[letter] + 1
            else:
                alpha[letter] = 1
    return alpha

def sort_on(dict):
    return dict["count"]

def get_report(letter_count):
    rep_list = []
    letter = (letter_count)
    file = (path.split('/'))[-1]
    print(f"The following is a letter count report for the file {file}")
    for letter in letter_count:
        #print(letter)
        if letter.isalpha():
            list_o_dicts = {}
            #print(letter)
            list_o_dicts["letter"] = letter
            list_o_dicts["count"] = letter_count[letter]
            rep_list.append(list_o_dicts)
        else:
            pass
    rep_list.sort(reverse=True, key=sort_on)
    for l in rep_list:
        lt = l["letter"]
        ct = l["count"]
        print(f"The \'{lt}\' character was found {ct} times ")
    
    
    
    
main()