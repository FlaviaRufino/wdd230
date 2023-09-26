
import collections
def main(filename):
	# Open file in reading mode
    with open(filename, "rt") as file:	
        # read and title the file contents
        file_contents = file.read()

        # split the contents of the file
        contents_as_list = file_contents.split()
        for i in range(0, len(contents_as_list)):
            contents_as_list[i] = contents_as_list[i].title()

        # count each instance of each word in the file
        occurrence_count = collections.Counter(contents_as_list)
        # word = input('Count which word? ')
        # count_certain_words(word, occurrence_count)
        list_keys(occurrence_count)
        return contents_as_list

def print_counted_words(occurrence_count):
    # print the occurence count in a dictionary inside a tuple called "Counter"
    print(occurrence_count)
    return occurrence_count


def print_certain_words(word, occurrence_count):
    word = word.title()
    if word in occurrence_count:
        # pull out a word from the dictionary
        word_count = occurrence_count[word.title()]
        # print the word and its number of occurences in the file
        print(f"Word: {word}. Count: {word_count}")
        return word_count
    else:
        # if the word is not in the file, display this message
        print("Sorry. That word is not available in this file.")
        return "Sorry. That word is not available in this file."

def list_keys(occurrence_count):
    # list the keys, each to a line
    keys_list = []
    for key in occurrence_count:
        print(key)
        keys_list.append(key)
    return keys_list 

def answer_question(question):
    # input statement "ALL" or "CERTAIN"
    if question == "ALL":
        return "ALL"
    elif question == "CERTAIN":
        return "CERTAIN"
    else:
        return "Not valid input"

main("sample.txt")