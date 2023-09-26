#
#from numpy import argmax

chapters=[]
books=[]
with open("books_and_chapters.txt") as file: # open the file
    largest=0
    for line in file:                       # read line by line
        parts=line.strip().split(":")
        scripture=parts[2]
        book=parts[0]
        books.append(book)
        chapter=int(parts[1])
        #
        if chapter>largest:
            largest=chapter
            largest_book=book
        #
        chapters.append(chapter)
        # print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")
    #
    # largest=max(chapters)
    # index=argmax(chapters)
    # largest_book=books[index]
    #
    print('')
    print(f"The largest chapter is: {largest}")
    # print(books)
    #
    print('')
    print(f"The largest chapter is in the book: {largest_book}")
