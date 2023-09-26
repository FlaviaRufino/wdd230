import random 

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']

def main ():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    append_random_words(words, 2)
    print(words)

if __name__ == "__main__":
    main()

