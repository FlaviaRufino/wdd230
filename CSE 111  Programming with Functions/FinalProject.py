# This program counts the number of times a word occurs in a text file. 
# You can count all or a certain number of words.

import collections

def main():
	try:	
		# user inputs file to be read
		filename = input("What text file would you like to access? ")

		# Open file in reading mode
		with open(filename, "rt") as file:	
			# read and title the file contents
			file_contents = file.read().title()

			# split the contents of the file
			contents_as_list = file_contents.split()

			# count each instance of each word in the file
			occurrence_count = collections.Counter(contents_as_list)

		question = input("""Would you like to count ALL the words in this file or a CERTAIN number of words?
Type ALL or CERTAIN to respond: """)

	except FileNotFoundError as file_not_found_err:
		# This code will be executed if the user enters
		# the name of a file that does not exist.
		print()
		print(type(file_not_found_err).__name__, file_not_found_err, sep=": ")
		print(f"The file {filename} doesn't exist.")
		print("Run the program again and enter the name of an existing file.")

	except PermissionError as perm_err:
		# This code will be executed if the user enters the name
		# of a file and does not have permission to read that file.
		print()
		print(type(perm_err).__name__, perm_err, sep=": ")
		print(f"You don't have permission to read {filename}.")
		print("Run the program again and enter the name of a file that you are allowed to read.")

	except ValueError as val_err:
		# This code will be executed if the user enters
		# an invalid integer instead of a given option.
		print()
		print(type(val_err).__name__, val_err, sep=": ")
		print("You entered an invalid integer for the given options.")
		print("Run the program again and enter an integer for a given option.")

	except Exception as excep:
		# This code will be executed if some other type of exception occurs.
		print()
		print(type(excep).__name__, excep, sep=": ")
		
	def print_counted_words():
		# print the occurence count in a dictionary inside a tuple called "Counter"
		print(occurrence_count)

	def print_certain_words(word):
		if word in occurrence_count:
			# pull out a word from the dictionary
			word_count = occurrence_count[word.title()]
			# print the word and its number of occurences in the file
			print(f"Word: {word}. Count: {word_count}")
		else:
			# if the word is not in the file, display this message
			print("Sorry. That word isn't available in this file.")

	def list_keys():
		# list the keys, each to a line
		for key in occurrence_count:
			print(key)

	if question == "ALL":
		# call the count_words function
		print_counted_words()
	elif question == "CERTAIN":
		num_words = int(input("How many words would you like to count? "))
		# list the options to be counted
		list_keys()
		for _ in range(num_words):
			# User inputs a specific word to be pulled from occurence_count and it is capitalized
			word = input("What word would you like to count? ").title()
			# call function that counts the occurrences of multiple words
			print_certain_words(word)



# Call the main function safely
if __name__ == "__main__":
	main()