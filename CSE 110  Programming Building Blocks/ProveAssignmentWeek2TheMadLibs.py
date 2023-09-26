name = input("Please, type your name: ")
print("Hello {}. Wecome to this activity!".format(name))
print("It is a pleasure to have you here today.")
print("Today we are going to have fun, creating an Mad Libs together!")
print("Lets get started!")
print()
adjective = input("Please type an adjective of your choice: ")
animal = input("Please type an aquatic animal name: ")
verb = input("Please type the first verb that comes to your mind: ")
Exclamation = input("Please type an exclamation sentence that you would like to say
now: ")
verb1 = input("Please type a verb that starts with the letter (r): ")
verb2 = input("Please type the last verb you will like  to use on our story: ")
title = input("To finish the story we are creating, please type the story title: ")
print()
print("We completed our Mad Libs!") ,print("\U0001F603")
print()
print("Lets see how our story turned out:")
print()
print("" ,title)
print()
print("The other day, I was really in trouble. It all started when I saw a very 
{adjective.format()} {animal.format()} {verb.format()} down the hallway. 
{Exclamation!.upper()} I yelled. But all I could think to do was to 
{verb1.format()} over and over. Miraculously, that caused it to stop, but not 
before it tried to {verb2.format()} right in front of my family.")
print()
print("Good job {}!".format(name))