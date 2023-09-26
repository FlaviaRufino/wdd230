

#05 Prove: Milestone - Adventure Game
print("Welcome to the game!")
print()
print("We are going to create a game together and for that, I will need that you 
type for the following scenario: ")
print()
match_and_flashlight = (input("You are walking through a dark forest and find two 
items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? "))
run_and_hide = "run" or "hide"
follow_and_look = "follow" or "look"
if match_and_flashlight.lower() == 'match':
    input("You pick up the match and strike it, and for an instant, the forest 
around you is illuminated. You see a large grizzly bear, and then the match burns 
out. Do you want to RUN, or HIDE behind a tree? ")
    if run_and_hide.lower() == 'run':
        input("You pick up the run and you run from the bear, but while your are 
running you can not see anything because is everything dark. But to help, you can 
choose between two things to help you see better.")
    if run_and_hide.lower() == 'hide':
        print("You pick up the hide and you hide behind a tree, is everything dark 
anyway, so maybe if you keep quiet the bear will not find you. ")
    else:
        print("Answer does not correspond. " )
if match_and_flashlight.lower() == 'flashlight':
    input("You pick up the flashlight and turn it on. You see the pathway lit up in
front of you, but you thought you also heard something off to the side. Do you want
to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
    if follow_and_look.lower() == 'follow':
        input("You pick up the follow and you continue following the path, so 
finally you got on a safe place! Congratulations, you won the game! ")
        if follow_and_look.lower() == 'look':
            print("You pick up the look and, when you look in the trees for the 
thing that made the noise... Oh no! To bad! The bear was waiting for you behind the
tree. Now there is not place to go, you are cornered. The bear caught you! Game 
over! ")
    else:
        print("Oops, sorry, this option is not available. We will not be able to 
complete the game. ")
#The end!